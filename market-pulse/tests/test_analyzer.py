import pytest
from analyzer import (
    extract_keywords_from_articles,
    merge_keywords,
    analyze_sentiment,
    build_industry_analysis,
    run_analysis,
)

SAMPLE_ARTICLES = [
    {"title": "AI 晶片需求大增，台積電訂單滿載", "summary": "人工智慧帶動半導體...", "lang": "zh"},
    {"title": "黃金突破歷史高點，避險情緒升溫", "summary": "國際金價持續上漲...", "lang": "zh"},
    {"title": "Fed 宣布暫停升息，市場反彈", "summary": "聯準會會議決定...", "lang": "zh"},
    {"title": "NVIDIA 發布新 GPU，科技股大漲", "summary": "NVIDIA 股價創新高...", "lang": "zh"},
    {"title": "關稅戰再升溫，貿易前景不明", "summary": "美中貿易摩擦加劇...", "lang": "zh"},
]

SAMPLE_CLARITY_TRENDS = [
    {"id": "t1", "title": "AI"},
    {"id": "t2", "title": "tariff"},
    {"id": "t3", "title": "gold"},
]


def test_extract_keywords_returns_list():
    keywords = extract_keywords_from_articles(SAMPLE_ARTICLES)
    assert isinstance(keywords, list)
    assert len(keywords) > 0


def test_extract_keywords_contain_expected_terms():
    keywords = extract_keywords_from_articles(SAMPLE_ARTICLES)
    keyword_lower = [kw.lower() for kw in keywords]
    # 至少應該包含其中幾個高頻詞
    assert any(k in keyword_lower for k in ["ai", "nvidia", "fed", "黃金", "台積電"])


def test_merge_keywords_deduplicates():
    clarity = ["AI", "gold", "tariff"]
    local = ["AI", "黃金", "Fed"]
    merged = merge_keywords(clarity_keywords=clarity, local_keywords=local, limit=10)
    # AI 不應重複出現
    assert merged.count("AI") + merged.count("ai") <= 1


def test_merge_keywords_respects_limit():
    clarity = ["A", "B", "C", "D", "E"]
    local = ["F", "G", "H", "I", "J", "K"]
    merged = merge_keywords(clarity_keywords=clarity, local_keywords=local, limit=7)
    assert len(merged) <= 7


def test_analyze_sentiment_positive():
    titles = ["股市大漲", "突破高點", "需求旺盛", "樂觀展望"]
    sentiment = analyze_sentiment(titles)
    assert sentiment == "看漲"


def test_analyze_sentiment_negative():
    titles = ["股市大跌", "市場崩盤", "衰退警告", "下修展望"]
    sentiment = analyze_sentiment(titles)
    assert sentiment == "看跌"


def test_analyze_sentiment_neutral():
    titles = ["市場觀望", "資訊公告"]
    sentiment = analyze_sentiment(titles)
    assert sentiment == "觀望"


def test_build_industry_analysis_structure():
    keywords = ["AI", "黃金", "tariff"]
    result = build_industry_analysis(keywords=keywords, articles=SAMPLE_ARTICLES)
    assert isinstance(result, list)
    for item in result:
        assert "industry" in item
        assert "keywords" in item
        assert "sentiment" in item
        assert "explanation" in item
        assert "fundswap_url" in item
        assert "related_articles" in item


def test_run_analysis_returns_full_structure():
    raw_data = {
        "articles": SAMPLE_ARTICLES,
        "clarity_trends": SAMPLE_CLARITY_TRENDS,
        "collected_at": "2026-04-07T08:00:00",
    }
    result = run_analysis(raw_data)
    assert "top_keywords" in result
    assert "industries" in result
    assert "articles" in result
    assert "analyzed_at" in result
    assert len(result["top_keywords"]) <= 10
