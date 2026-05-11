import jieba
import logging
import json
import os
from datetime import datetime, date
from industry_map import (
    get_industries_for_keyword,
    map_keywords_to_industries,
    get_fundswap_url,
)
from config import CACHE_DIR, CACHE_KEEP_DAYS

logger = logging.getLogger(__name__)

# 情感詞典
POSITIVE_WORDS = {"漲", "突破", "創高", "樂觀", "成長", "需求旺", "升", "反彈", "強勁", "買進"}
NEGATIVE_WORDS = {"跌", "衰退", "崩", "警告", "下修", "疲軟", "降", "拋售", "恐慌", "賣出"}

# 中文停用詞（含財經公告雜訊）
ZH_STOPWORDS = {
    # 基本虛詞
    "的", "了", "在", "是", "我", "有", "和", "就", "不", "人", "都",
    "一", "一個", "上", "也", "很", "到", "說", "要", "去", "你",
    "會", "著", "沒有", "看", "好", "自己", "這", "那", "把",
    "為", "對", "與", "及", "或", "但", "而", "被", "所", "等",
    "由", "其", "此", "各", "已", "將", "並", "再", "後", "當",
    # 時間單位
    "月", "日", "年", "今日", "昨日", "本月", "本年", "近期",
    # 金融公告常見噪音字（來自 TWSE 類公告）
    "元", "億元", "萬元", "新台幣", "美元", "港元",
    "公司", "企業", "股份", "有限公司", "集團",
    "市場", "指數", "上市", "上櫃", "掛牌", "發行",
    "ETF", "基金", "淨值", "股票", "股價", "股東",
    "投資人", "投資者", "法人", "外資", "散戶",
    "產業", "行業", "類股", "盤面",
    "報告", "公告", "說明", "表示", "指出", "表示",
    "台灣", "中國", "美國", "美", "台",  # 太廣泛，無法代表主題
    # 促銷/消費類雜訊（Yahoo 股市有時混入非財經新聞）
    "買一", "一送", "送一", "折扣", "優惠", "活動", "推出",
    # 段落/文章結構常見詞
    "根據", "依據", "來自", "方面", "相關", "目前", "未來",
    "包括", "包含", "以及", "透過", "進行", "提供", "增加", "下降",
    "公布", "宣布", "發布", "顯示", "持續", "截至", "約為",
}

# 英文停用詞（基本 + 金融通用噪音）
EN_STOPWORDS = {
    # 基本功能詞
    "the", "a", "an", "is", "are", "was", "were", "in", "on", "at",
    "to", "for", "of", "and", "or", "but", "as", "by", "with",
    "from", "that", "this", "it", "its", "be", "has", "have", "had",
    "will", "would", "could", "should", "may", "might",
    "not", "no", "also", "just", "than", "then", "when", "how",
    "who", "what", "which", "all", "been", "about", "into", "over",
    "after", "before", "their", "they", "them", "these", "those",
    "more", "most", "new", "can", "two", "three", "one",
    # 動詞噪音（太泛用）
    "says", "said", "told", "reported", "plans", "plan", "set",
    "expected", "according", "amid", "following",
    "make", "made", "take", "taken", "using", "used",
    "including", "among", "back", "still", "even", "last",
    # 財經通用噪音
    "market", "markets", "stock", "stocks", "share", "shares",
    "company", "companies", "firm", "firms", "corp", "inc", "ltd",
    "percent", "billion", "million", "trillion", "dollar", "dollars",
    "quarter", "year", "years", "month", "months", "week", "weeks",
    "price", "prices", "rate", "rates", "value", "index", "fund",
    "report", "data", "number", "numbers", "growth", "rise", "fall",
}


def _extract_en_keywords(text: str, weight: float) -> dict[str, float]:
    """
    英文關鍵字萃取：
    1. 過濾停用詞後取單詞（4+ 字元）
    2. 提取連續非停用詞 bigram（如 "artificial intelligence"）
    回傳 {word: weighted_score} dict。
    """
    counter: dict[str, float] = {}
    words = text.lower().split()
    clean = [w.strip(".,!?\"':;()[]") for w in words]
    filtered = [w for w in clean if w and w not in EN_STOPWORDS and len(w) >= 4 and w.isalpha()]

    # 單詞
    for w in filtered:
        counter[w] = counter.get(w, 0) + weight

    # bigram：連續兩個有效詞
    for i in range(len(clean) - 1):
        w1 = clean[i].strip(".,!?\"':;()[]")
        w2 = clean[i + 1].strip(".,!?\"':;()[]")
        if (w1 and w2
                and w1 not in EN_STOPWORDS and w2 not in EN_STOPWORDS
                and len(w1) >= 4 and len(w2) >= 4
                and w1.isalpha() and w2.isalpha()):
            bigram = f"{w1} {w2}"
            counter[bigram] = counter.get(bigram, 0) + weight * 1.5  # bigram 加權 1.5×

    return counter


def extract_keywords_from_articles(articles: list[dict], top_n: int = 20) -> list[str]:
    """
    從文章標題與摘要中萃取高頻關鍵字（加權版）。
    中文用 jieba 斷詞，英文用空白分詞 + bigram，過濾停用詞後依各來源 weight 加權計頻。
    weight 越高的來源，其關鍵字對排名的影響越大（計數 × weight）。
    """
    weighted_counter: dict[str, float] = {}
    for article in articles:
        weight = article.get("weight", 1)
        text = article.get("title", "") + " " + article.get("summary", "")
        lang = article.get("lang", "zh")
        if lang == "zh":
            words = list(jieba.cut(text))
            filtered = [w.strip() for w in words if len(w.strip()) >= 2 and w.strip() not in ZH_STOPWORDS]
            for word in filtered:
                weighted_counter[word] = weighted_counter.get(word, 0) + weight
        else:
            for word, score in _extract_en_keywords(text, weight).items():
                weighted_counter[word] = weighted_counter.get(word, 0) + score

    sorted_words = sorted(weighted_counter.items(), key=lambda x: x[1], reverse=True)
    return [word for word, _ in sorted_words[:top_n]]


def merge_keywords(clarity_keywords: list[str], local_keywords: list[str], limit: int = 10) -> list[str]:
    """
    合併 Clarity API 與 RSS 本地萃取的關鍵字，去重後取前 limit 個。
    Clarity 關鍵字優先排在前面。
    """
    seen = set()
    merged = []
    for kw in clarity_keywords + local_keywords:
        kw_lower = kw.lower()
        if kw_lower not in seen:
            seen.add(kw_lower)
            merged.append(kw)
        if len(merged) >= limit:
            break
    return merged


def analyze_sentiment(titles: list[str]) -> str:
    """
    對一組新聞標題做情感分析。
    計算正面詞 vs 負面詞出現次數，回傳 '看漲'、'看跌' 或 '觀望'。
    """
    positive_count = 0
    negative_count = 0
    for title in titles:
        for word in POSITIVE_WORDS:
            if word in title:
                positive_count += 1
        for word in NEGATIVE_WORDS:
            if word in title:
                negative_count += 1

    if positive_count > negative_count:
        return "看漲"
    elif negative_count > positive_count:
        return "看跌"
    else:
        return "觀望"


def build_industry_analysis(keywords: list[str], articles: list[dict]) -> list[dict]:
    """
    根據關鍵字與文章，建立各產業的分析結果。
    每個產業包含：關聯關鍵字、情感、解釋文字、好好證券連結、相關文章。
    """
    industry_keywords = map_keywords_to_industries(keywords)
    result = []

    for industry, matched_kws in industry_keywords.items():
        # 找出與此產業相關的文章（標題含關鍵字）
        related_articles = []
        for article in articles:
            title_lower = article.get("title", "").lower()
            if any(kw.lower() in title_lower for kw in matched_kws):
                related_articles.append(article)

        related_titles = [a.get("title", "") for a in related_articles]
        sentiment = analyze_sentiment(related_titles) if related_titles else "觀望"

        # 組合解釋文字
        kw_str = "、".join(matched_kws[:3])
        sentiment_text = "偏向看漲" if sentiment == "看漲" else ("偏向看跌" if sentiment == "看跌" else "持觀望態度")
        explanation = (
            f"「{kw_str}」等關鍵字近期在市場討論中頻繁出現，"
            f"相關新聞共 {len(related_articles)} 篇，市場情緒{sentiment_text}。"
        )

        result.append({
            "industry": industry,
            "keywords": matched_kws,
            "sentiment": sentiment,
            "explanation": explanation,
            "fundswap_url": get_fundswap_url(industry),
            "related_articles": related_articles[:5],  # 最多顯示 5 篇
        })

    return result


def run_news_only(raw_data: dict) -> dict:
    """
    階段 1：僅保存原始新聞，不做任何 NLP 分析。
    適合在尚未設定產業對照表前快速瀏覽當日新聞。
    """
    articles = raw_data.get("articles", [])
    clarity_trends = raw_data.get("clarity_trends", [])
    clarity_keywords = [t.get("title", "") for t in clarity_trends if t.get("title")]
    return {
        "stage": "news",
        "articles": articles[:50],
        "top_keywords": [],
        "industries": [],
        "analyzed_at": datetime.now().isoformat(),
        "clarity_auth_ok": len(clarity_keywords) > 0,
    }


def run_keywords_only(raw_data: dict) -> dict:
    """
    階段 2：萃取關鍵字，不進行產業對應分析。
    適合在確認關鍵字後再決定是否執行產業分析。
    """
    articles = raw_data.get("articles", [])
    clarity_trends = raw_data.get("clarity_trends", [])
    clarity_keywords = [t.get("title", "") for t in clarity_trends if t.get("title")]
    local_keywords = extract_keywords_from_articles(articles, top_n=20)
    top_keywords = merge_keywords(clarity_keywords, local_keywords, limit=10)
    return {
        "stage": "keywords",
        "articles": articles[:50],
        "top_keywords": top_keywords,
        "industries": [],
        "analyzed_at": datetime.now().isoformat(),
        "clarity_auth_ok": len(clarity_keywords) > 0,
    }


def run_analysis(raw_data: dict) -> dict:
    """
    階段 3（完整）：執行完整分析流程，包含關鍵字萃取、產業對應與情感判斷。
    """
    articles = raw_data.get("articles", [])
    clarity_trends = raw_data.get("clarity_trends", [])

    clarity_keywords = [t.get("title", "") for t in clarity_trends if t.get("title")]
    local_keywords = extract_keywords_from_articles(articles, top_n=20)
    top_keywords = merge_keywords(clarity_keywords, local_keywords, limit=10)
    industries = build_industry_analysis(top_keywords, articles)

    return {
        "stage": "full",
        "top_keywords": top_keywords,
        "industries": industries,
        "articles": articles[:50],
        "analyzed_at": datetime.now().isoformat(),
        "clarity_auth_ok": len(clarity_keywords) > 0,
    }


def save_cache(analysis_result: dict, cache_dir: str = CACHE_DIR) -> str:
    """將分析結果寫入當日 JSON 快取，回傳檔案路徑。"""
    os.makedirs(cache_dir, exist_ok=True)
    today = date.today().isoformat()
    filepath = os.path.join(cache_dir, f"{today}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(analysis_result, f, ensure_ascii=False, indent=2)
    logger.info(f"快取已寫入：{filepath}")
    return filepath


def load_cache(cache_dir: str = CACHE_DIR) -> dict | None:
    """讀取當日快取，若不存在則回傳 None。"""
    today = date.today().isoformat()
    filepath = os.path.join(cache_dir, f"{today}.json")
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)
