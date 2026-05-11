from unittest.mock import patch, MagicMock
from collector import fetch_rss_articles, fetch_clarity_trends, collect_all


# 模擬 feedparser 回傳結果
MOCK_RSS_FEED = MagicMock()
MOCK_RSS_FEED.entries = [
    MagicMock(
        title="台積電法說會樂觀展望，半導體需求回升",
        summary="台積電在法說會中表示...",
        link="https://example.com/news1",
        published="Tue, 07 Apr 2026 08:00:00 +0000",
    ),
    MagicMock(
        title="Fed 維持利率不變，市場觀望",
        summary="聯準會宣布維持...",
        link="https://example.com/news2",
        published="Tue, 07 Apr 2026 09:00:00 +0000",
    ),
]


def test_fetch_rss_returns_list_of_articles():
    with patch("feedparser.parse", return_value=MOCK_RSS_FEED):
        articles = fetch_rss_articles(
            "https://fake-rss.com/feed", source_name="Test RSS", lang="zh"
        )
    assert isinstance(articles, list)
    assert len(articles) == 2


def test_fetch_rss_article_has_required_fields():
    with patch("feedparser.parse", return_value=MOCK_RSS_FEED):
        articles = fetch_rss_articles(
            "https://fake-rss.com/feed", source_name="Test RSS", lang="zh"
        )
    article = articles[0]
    assert "title" in article
    assert "summary" in article
    assert "link" in article
    assert "source" in article
    assert "lang" in article
    assert "published_at" in article


def test_fetch_rss_handles_parse_error_gracefully():
    with patch("feedparser.parse", side_effect=Exception("Network error")):
        articles = fetch_rss_articles(
            "https://fake-rss.com/feed", source_name="Test RSS", lang="zh"
        )
    assert articles == []


def test_fetch_clarity_trends_returns_list():
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {"id": "abc123", "title": "AI", "score": 95},
        {"id": "def456", "title": "tariff", "score": 80},
    ]
    with patch("requests.get", return_value=mock_response):
        trends = fetch_clarity_trends(limit=10)
    assert isinstance(trends, list)
    assert len(trends) == 2


def test_fetch_clarity_trends_returns_empty_on_auth_error():
    mock_response = MagicMock()
    mock_response.status_code = 401
    with patch("requests.get", return_value=mock_response):
        trends = fetch_clarity_trends(limit=10)
    assert trends == []


def test_collect_all_returns_dict_with_expected_keys():
    with (
        patch("collector.fetch_rss_articles", return_value=[]),
        patch("collector.fetch_clarity_trends", return_value=[]),
    ):
        result = collect_all()
    assert "articles" in result
    assert "clarity_trends" in result
    assert "collected_at" in result
    assert isinstance(result["articles"], list)
    assert isinstance(result["clarity_trends"], list)
    assert isinstance(result["collected_at"], str)
