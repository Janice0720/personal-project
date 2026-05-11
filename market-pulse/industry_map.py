from typing import Optional

# 關鍵字 → 產業對照表
# key: 小寫關鍵字（中英文皆可）
# value: 產業名稱（list，一個關鍵字可對應多個產業）
KEYWORD_INDUSTRY_MAP: dict[str, list[str]] = {
    # 半導體 / 科技
    "ai": ["半導體／科技"],
    "人工智慧": ["半導體／科技"],
    "nvidia": ["半導體／科技"],
    "晶片": ["半導體／科技"],
    "semiconductor": ["半導體／科技"],
    "台積電": ["半導體／科技"],
    "tsmc": ["半導體／科技"],
    "chips": ["半導體／科技"],
    "gpu": ["半導體／科技"],
    # 金融 / 利率敏感
    "fed": ["金融／利率敏感"],
    "升息": ["金融／利率敏感"],
    "降息": ["金融／利率敏感"],
    "inflation": ["金融／利率敏感"],
    "利率": ["金融／利率敏感"],
    "interest rate": ["金融／利率敏感"],
    "央行": ["金融／利率敏感"],
    "federal reserve": ["金融／利率敏感"],
    # 能源
    "oil": ["能源"],
    "石油": ["能源"],
    "opec": ["能源"],
    "能源": ["能源"],
    "petroleum": ["能源"],
    "crude": ["能源"],
    # 貴金屬
    "gold": ["貴金屬"],
    "黃金": ["貴金屬"],
    "避險": ["貴金屬"],
    "貴金屬": ["貴金屬"],
    "silver": ["貴金屬"],
    "白銀": ["貴金屬"],
    # 電動車 / 新能源
    "ev": ["電動車／新能源"],
    "tesla": ["電動車／新能源"],
    "電動車": ["電動車／新能源"],
    "新能源": ["電動車／新能源"],
    "electric vehicle": ["電動車／新能源"],
    # 不動產
    "reits": ["不動產"],
    "房地產": ["不動產"],
    "real estate": ["不動產"],
    "房市": ["不動產"],
    # 生技醫療
    "biotech": ["生技醫療"],
    "新藥": ["生技醫療"],
    "fda": ["生技醫療"],
    "醫療": ["生技醫療"],
    "pharmaceutical": ["生技醫療"],
    "藥廠": ["生技醫療"],
    # 貿易政策
    "tariff": ["貿易政策"],
    "關稅": ["貿易政策"],
    "貿易戰": ["貿易政策"],
    "trade war": ["貿易政策"],
    "制裁": ["貿易政策"],
}

# 好好證券篩選 URL 基底
FUNDSWAP_BASE_URL = (
    "https://www.fundswap.com.tw/trade/funds/"
    "?fundsIndex=1&filterType=rateOfReturn&s=-rateOfReturn3Months&page=1"
    "&fundNameCategory={category}"
)

# 產業 → 好好證券篩選關鍵字對照（待用戶提供完整清單）
INDUSTRY_FUNDSWAP_MAP: dict[str, str] = {
    "半導體／科技": "科技",
    "金融／利率敏感": "金融",
    "能源": "能源",
    "貴金屬": "貴金屬",
    "電動車／新能源": "新能源",
    "不動產": "不動產",
    "生技醫療": "醫療",
    "貿易政策": "",  # 無直接對應，留空
}


def get_industries_for_keyword(keyword: str) -> list[str]:
    """給定一個關鍵字，回傳對應的產業清單（不分大小寫、自動去除首尾空白）。"""
    return KEYWORD_INDUSTRY_MAP.get(keyword.strip().lower(), [])


def get_fundswap_url(industry: str) -> Optional[str]:
    """給定產業名稱，回傳好好證券篩選連結，若無對應則回傳 None。"""
    category = INDUSTRY_FUNDSWAP_MAP.get(industry, "")
    if not category:
        return None
    return FUNDSWAP_BASE_URL.format(category=category)


def map_keywords_to_industries(keywords: list[str]) -> dict[str, list[str]]:
    """
    給定關鍵字清單，回傳 {產業: [關鍵字列表]} 的對應關係。
    同一關鍵字可出現在多個產業下。
    """
    result: dict[str, list[str]] = {}
    for kw in keywords:
        industries = get_industries_for_keyword(kw)
        for ind in industries:
            result.setdefault(ind, []).append(kw)
    return result
