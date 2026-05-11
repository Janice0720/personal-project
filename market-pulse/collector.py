import feedparser
import requests
import logging
from datetime import datetime
from config import (
    RSS_FEEDS,
    CLARITY_BASE_URL, CLARITY_COOKIES, CLARITY_HEADERS,
    GNEWS_API_KEY, GNEWS_BASE_URL, GNEWS_QUERIES, SOURCE_WEIGHT_GNEWS,
)

logger = logging.getLogger(__name__)


def fetch_rss_articles(url: str, source_name: str, lang: str, weight: int = 1, max_articles: int = 50) -> list[dict]:
    """
    解析單一 RSS Feed，回傳標準化文章列表。
    每篇文章格式：{title, summary, link, source, lang, weight, published_at}
    max_articles 限制每來源最大取得篇數，避免單一來源過度影響關鍵字分析。
    """
    try:
        feed = feedparser.parse(url)
        articles = []
        for entry in feed.entries[:max_articles]:
            articles.append(
                {
                    "title": getattr(entry, "title", ""),
                    "summary": getattr(entry, "summary", ""),
                    "link": getattr(entry, "link", ""),
                    "source": source_name,
                    "lang": lang,
                    "weight": weight,
                    "published_at": getattr(entry, "published", ""),
                }
            )
        logger.info(f"[RSS] {source_name} (weight={weight}): 取得 {len(articles)} 篇")
        return articles
    except Exception as e:
        logger.error(f"[RSS] {source_name} 抓取失敗: {e}")
        return []


def fetch_gnews_articles() -> list[dict]:
    """
    呼叫 GNews API 取得財經新聞（英文 + 中文台灣）。
    需在 .env 中設定 GNEWS_API_KEY。
    每日配額：100 次請求 / 每次最多 10 篇。
    """
    if not GNEWS_API_KEY:
        logger.warning("[GNews] 未設定 GNEWS_API_KEY，跳過 GNews 資料來源")
        return []

    articles = []
    for query in GNEWS_QUERIES:
        url = (
            f"{GNEWS_BASE_URL}/top-headlines"
            f"?topic={query['topic']}&lang={query['lang']}"
            f"&country={query['country']}&max={query['max']}"
            f"&apikey={GNEWS_API_KEY}"
        )
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 403:
                logger.warning("[GNews] API Key 無效或已超過每日配額")
                break
            resp.raise_for_status()
            data = resp.json()
            for item in data.get("articles", []):
                articles.append({
                    "title": item.get("title", ""),
                    "summary": item.get("description", ""),
                    "link": item.get("url", ""),
                    "source": f"GNews/{item.get('source', {}).get('name', 'unknown')}",
                    "lang": query["lang"],
                    "weight": SOURCE_WEIGHT_GNEWS,
                    "published_at": item.get("publishedAt", ""),
                })
            logger.info(f"[GNews] lang={query['lang']} country={query['country']}: 取得 {len(data.get('articles', []))} 篇")
        except Exception as e:
            logger.error(f"[GNews] 請求失敗 (lang={query['lang']}): {e}")

    return articles


def fetch_clarity_trends(limit: int = 10) -> list[dict]:
    """
    呼叫 Clarity API 取得熱門趨勢排行。
    若認證失效（401/403）或回應為空，回傳空列表並記錄警告。
    """
    url = f"{CLARITY_BASE_URL}/api/trends/ranked?limit={limit}"
    try:
        resp = requests.get(url, cookies=CLARITY_COOKIES, headers=CLARITY_HEADERS, timeout=10)
        if resp.status_code in (401, 403):
            logger.warning("[Clarity] 認證失效（Token 可能已過期），請更新 .env 中的 Cookie。")
            return []
        resp.raise_for_status()
        # 空 body 視為未登入，不拋例外
        if not resp.text or not resp.text.strip():
            logger.warning("[Clarity] 回應為空（可能需要先在 .env 設定 Cookie）")
            return []
        data = resp.json()
        logger.info(f"[Clarity] 取得 {len(data)} 個趨勢")
        return data if isinstance(data, list) else []
    except ValueError as e:
        logger.warning(f"[Clarity] 回應非 JSON（可能未登入）: {e}")
        return []
    except Exception as e:
        logger.error(f"[Clarity] API 呼叫失敗: {e}")
        return []


def fetch_clarity_trend_detail(trend_id: str) -> dict:
    """取得特定趨勢的詳細資訊與相關文章。"""
    url = f"{CLARITY_BASE_URL}/api/trends/{trend_id}"
    try:
        resp = requests.get(url, cookies=CLARITY_COOKIES, headers=CLARITY_HEADERS, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        logger.error(f"[Clarity] 趨勢詳情取得失敗 ({trend_id}): {e}")
        return {}


def collect_all() -> dict:
    """
    執行完整資料收集：RSS（Reuters→TWSE→Yahoo 依權重排序）+ GNews + Clarity API。
    回傳 {articles: [...], clarity_trends: [...], collected_at: "ISO時間"}
    各來源文章均帶 weight 欄位，供後續加權關鍵字萃取使用。
    """
    all_articles = []

    # RSS 來源（跳過 enabled=False 的來源；config 已依權重高到低排列）
    for feed_config in RSS_FEEDS:
        if not feed_config.get("enabled", True):
            logger.info(f"[RSS] 已停用：{feed_config['name']}")
            continue
        articles = fetch_rss_articles(
            url=feed_config["url"],
            source_name=feed_config["name"],
            lang=feed_config["lang"],
            weight=feed_config.get("weight", 1),
            max_articles=feed_config.get("max_articles", 50),
        )
        all_articles.extend(articles)

    # GNews API（weight=4，高於所有 RSS）
    gnews_articles = fetch_gnews_articles()
    all_articles.extend(gnews_articles)

    # 去重（依 link）
    seen_links = set()
    unique_articles = []
    for article in all_articles:
        if article["link"] not in seen_links:
            seen_links.add(article["link"])
            unique_articles.append(article)

    # 依權重高到低排序，確保 GNews(×4) > TWSE(×2) > Yahoo(×1) 在前
    unique_articles.sort(key=lambda a: a.get("weight", 1), reverse=True)

    clarity_trends = fetch_clarity_trends(limit=10)

    total = len(unique_articles)
    gnews_count = len(gnews_articles)
    logger.info(f"[collect_all] 共收集 {total} 篇（GNews {gnews_count} 篇），Clarity {len(clarity_trends)} 個趨勢")

    return {
        "articles": unique_articles,
        "clarity_trends": clarity_trends,
        "collected_at": datetime.now().isoformat(),
    }
