from industry_map import (
    get_industries_for_keyword,
    get_fundswap_url,
    map_keywords_to_industries,
)


def test_known_keyword_returns_industry():
    assert "半導體／科技" in get_industries_for_keyword("AI")


def test_case_insensitive():
    assert get_industries_for_keyword("NVIDIA") == get_industries_for_keyword("nvidia")


def test_keyword_with_whitespace_is_stripped():
    assert get_industries_for_keyword(" AI ") == get_industries_for_keyword("AI")


def test_unknown_keyword_returns_empty():
    assert get_industries_for_keyword("不存在的字") == []


def test_fundswap_url_contains_category():
    url = get_fundswap_url("貴金屬")
    assert url is not None
    assert "貴金屬" in url
    assert "fundswap.com.tw" in url


def test_no_fundswap_url_for_trade_policy():
    assert get_fundswap_url("貿易政策") is None


def test_map_keywords_to_industries():
    result = map_keywords_to_industries(["AI", "黃金", "unknown"])
    assert "半導體／科技" in result
    assert "AI" in result["半導體／科技"]
    assert "貴金屬" in result
    assert "黃金" in result["貴金屬"]
    assert "unknown" not in str(result)
