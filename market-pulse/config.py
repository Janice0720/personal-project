import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# ── 來源權重常數 ──────────────────────────────────────────
# 數字越大，關鍵字貢獻度越高（keyword 計數 × weight）
SOURCE_WEIGHT_CLARITY = 5   # Clarity 趨勢 API（最高優先）
SOURCE_WEIGHT_GNEWS   = 4   # GNews API
SOURCE_WEIGHT_REUTERS = 3   # Reuters RSS
SOURCE_WEIGHT_TWSE    = 2   # 臺灣證交所 RSS
SOURCE_WEIGHT_YAHOO   = 1   # Yahoo 股市 RSS（最低優先）

# Clarity API
CLARITY_BASE_URL = "https://clarity.vibegens.com"
CLARITY_COOKIES = {
    "__Secure-authjs.session-token": os.getenv("CLARITY_SESSION_TOKEN", ""),
    "__Host-authjs.csrf-token": os.getenv("CLARITY_CSRF_TOKEN", ""),
}
CLARITY_HEADERS = {
    "accept": "*/*",
    "referer": "https://clarity.vibegens.com/",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
}

# GNews API（免費方案：每日 100 次請求，每次最多 10 篇）
GNEWS_API_KEY = os.getenv("GNEWS_API_KEY", "")
GNEWS_BASE_URL = "https://gnews.io/api/v4"
# 每次執行抓取的主題組合（lang + topic + country）
# 節省配額：英文財經 × 1 + 中文台灣財經 × 1 = 每日 2 次請求
GNEWS_QUERIES = [
    {"topic": "business", "lang": "en", "country": "us", "max": 10},
    {"topic": "business", "lang": "zh", "country": "tw", "max": 10},
]

# 選配：MarketAux API
MARKETAUX_API_KEY = os.getenv("MARKETAUX_API_KEY", "")

# RSS 來源清單（含權重）
# enabled=False 的來源會被 collector.py 跳過
RSS_FEEDS = [
    {
        "name": "CNBC Business News",
        "url": "https://www.cnbc.com/id/100003114/device/rss/rss.html",
        "lang": "en",
        "weight": SOURCE_WEIGHT_REUTERS,
        "enabled": True,
        "max_articles": 20,
    },
    {
        "name": "MarketWatch Top Stories",
        "url": "https://feeds.content.dowjones.io/public/rss/mw_topstories",
        "lang": "en",
        "weight": SOURCE_WEIGHT_REUTERS,
        "enabled": True,
        "max_articles": 10,
    },
    {
        "name": "TWSE 臺灣證交所",
        "url": "https://www.twse.com.tw/rwd/zh/news/feed?type=rss",
        "lang": "zh",
        "weight": SOURCE_WEIGHT_TWSE,
        "enabled": False,        # 停用：官方公告用語（上市/掛牌/億元）不適合輿情分析
        "max_articles": 10,
    },
    {
        "name": "Yahoo 股市 - 台灣市場",
        "url": "https://tw.stock.yahoo.com/rss?category=tw-market",
        "lang": "zh",
        "weight": SOURCE_WEIGHT_YAHOO,
        "enabled": True,
        "max_articles": 15,
    },
    {
        "name": "Yahoo 股市 - 國際財經",
        "url": "https://tw.stock.yahoo.com/rss?category=intl-markets",
        "lang": "zh",
        "weight": SOURCE_WEIGHT_YAHOO,
        "enabled": True,
        "max_articles": 15,
    },
    {
        "name": "Yahoo 股市 - 基金新聞",
        "url": "https://tw.stock.yahoo.com/rss?category=funds-news",
        "lang": "zh",
        "weight": SOURCE_WEIGHT_YAHOO,
        "enabled": False,        # 停用：基金 NAV 公告，與市場輿情無關
        "max_articles": 10,
    },
]

# 人工參考連結（Dashboard 側欄）
REFERENCE_LINKS = [
    {"name": "Clarity 趨勢分析", "url": "https://clarity.vibegens.com/"},
    {"name": "Glint Trade Terminal", "url": "https://glint.trade/terminal"},
    {"name": "TradingView", "url": "https://www.tradingview.com/"},
]

# 排程設定
SCHEDULE_HOUR = 8
SCHEDULE_MINUTE = 0

# 快取設定
_PROJECT_ROOT = Path(__file__).parent
CACHE_DIR = str(_PROJECT_ROOT / "data" / "cache")
CACHE_KEEP_DAYS = 30
