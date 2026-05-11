import streamlit as st
import pandas as pd
import logging
from collector import collect_all
from analyzer import run_news_only, run_keywords_only, run_analysis, save_cache, load_cache
from scheduler import create_scheduler
from config import REFERENCE_LINKS

logging.basicConfig(level=logging.INFO)

st.set_page_config(
    page_title="市場輿情分析儀表板",
    page_icon="🌐",
    layout="wide",
)

# 啟動背景排程器（只在第一次執行時初始化）
if "scheduler_started" not in st.session_state:
    scheduler = create_scheduler()
    scheduler.start()
    st.session_state["scheduler_started"] = True
    st.session_state["scheduler"] = scheduler

STAGE_LABELS = {
    "news":     "① 抓取新聞",
    "keywords": "② 關鍵字彙總",
    "full":     "③ 完整分析（含產業）",
}
STAGE_ORDER = ["news", "keywords", "full"]
SENTIMENT_ICON = {"看漲": "📈", "看跌": "📉", "觀望": "➡️"}


def execute_stage(stage: str) -> dict:
    """根據選定階段執行收集與對應層級的分析，寫入快取並回傳結果。"""
    spinner_text = {
        "news":     "正在抓取新聞中，請稍候...",
        "keywords": "抓取新聞 + 萃取關鍵字中，請稍候...",
        "full":     "執行完整分析（新聞 + 關鍵字 + 產業）中，請稍候...",
    }
    with st.spinner(spinner_text[stage]):
        raw_data = collect_all()
        if stage == "news":
            result = run_news_only(raw_data)
        elif stage == "keywords":
            result = run_keywords_only(raw_data)
        else:
            result = run_analysis(raw_data)
        save_cache(result)
    return result


def load_or_prompt() -> dict | None:
    """讀取當日快取，若無則回傳 None（不自動執行）。"""
    return load_cache()


# ── 標頭 ────────────────────────────────────────────────
st.title("🌐 市場輿情分析儀表板")

# ── 左側欄：執行階段控制 ─────────────────────────────────
with st.sidebar:
    st.header("⚙️ 執行控制")

    selected_stage = st.radio(
        "執行階段",
        options=STAGE_ORDER,
        format_func=lambda s: STAGE_LABELS[s],
        index=2,
        help=(
            "① 抓取新聞：只抓取並顯示今日新聞，速度最快。\n\n"
            "② 關鍵字彙總：在新聞基礎上額外萃取 Top 10 熱門關鍵字。\n\n"
            "③ 完整分析：再進一步對應產業與情感，需設定好好證券對照表才有基金連結。"
        ),
    )

    run_clicked = st.button("▶ 立即執行", use_container_width=True, type="primary")
    reset_clicked = st.button("🗑 清除今日快取", use_container_width=True)

    st.divider()
    st.caption("**參考工具**")
    for link in REFERENCE_LINKS:
        st.markdown(f"[{link['name']}]({link['url']})")

# ── 執行邏輯 ─────────────────────────────────────────────
if reset_clicked:
    import os
    from config import CACHE_DIR
    from datetime import date
    cache_file = os.path.join(CACHE_DIR, f"{date.today().isoformat()}.json")
    if os.path.exists(cache_file):
        os.remove(cache_file)
        st.success("今日快取已清除。")
    st.rerun()

if run_clicked:
    data = execute_stage(selected_stage)
    st.rerun()
else:
    data = load_or_prompt()

# ── 狀態列 ───────────────────────────────────────────────
if data:
    analyzed_at = data.get("analyzed_at", "")
    current_stage = data.get("stage", "unknown")
    clarity_ok = data.get("clarity_auth_ok", False)

    col_info, col_stage = st.columns([3, 1])
    with col_info:
        st.caption(f"資料更新時間：{analyzed_at[:19].replace('T', ' ') if analyzed_at else '未知'}")
    with col_stage:
        st.caption(f"目前階段：{STAGE_LABELS.get(current_stage, current_stage)}")

    if not clarity_ok:
        st.warning(
            "⚠️ Clarity API 認證失效，目前僅使用 RSS 來源。"
            "請更新 `.env` 中的 `CLARITY_SESSION_TOKEN`。"
        )

    # 若目前快取階段比選定階段低，提示可升級
    if STAGE_ORDER.index(current_stage) < STAGE_ORDER.index(selected_stage):
        st.info(
            f"目前快取為「{STAGE_LABELS[current_stage]}」，"
            f"點擊「▶ 立即執行」可升級至「{STAGE_LABELS[selected_stage]}」。"
        )
else:
    st.info("尚無今日資料。請在左側選擇執行階段後點擊「▶ 立即執行」。")
    st.stop()

st.divider()

# ── 三個 Tab ─────────────────────────────────────────────
tab_news, tab_kw, tab_industry = st.tabs(["📰 新聞快訊", "🔑 關鍵字彙總", "🏭 產業分析"])

# ── Tab 1：新聞快訊 ──────────────────────────────────────
with tab_news:
    articles = data.get("articles", [])
    if articles:
        all_sources = sorted(set(a.get("source", "") for a in articles))
        selected_source = st.selectbox("篩選來源", options=["全部"] + all_sources, key="src_filter")
        filtered = articles if selected_source == "全部" else [
            a for a in articles if a.get("source") == selected_source
        ]
        st.caption(f"共 {len(filtered)} 篇{'（顯示前 30 篇）' if len(filtered) > 30 else ''}")
        for article in filtered[:30]:
            st.markdown(
                f"**[{article.get('title', '(無標題)')}]({article.get('link', '#')})**  "
                f"　｜　來源：`{article.get('source', '')}` "
                f"　｜　{article.get('published_at', '')[:16]}"
            )
    else:
        st.info("尚無新聞資料，請點擊「▶ 立即執行」（至少選擇① 抓取新聞）。")

# ── Tab 2：關鍵字彙總 ────────────────────────────────────
with tab_kw:
    top_keywords = data.get("top_keywords", [])
    if top_keywords:
        col_chart, col_list = st.columns([2, 1])
        with col_chart:
            kw_scores = {kw: (len(top_keywords) - i) for i, kw in enumerate(top_keywords)}
            chart_df = pd.DataFrame(
                {"關鍵字": list(kw_scores.keys()), "熱度分數": list(kw_scores.values())}
            )
            st.bar_chart(chart_df.set_index("關鍵字"))
        with col_list:
            st.markdown("**排行清單**")
            for i, kw in enumerate(top_keywords, 1):
                st.markdown(f"{i}. `{kw}`")
    else:
        stage_hint = "② 關鍵字彙總" if data.get("stage") == "news" else "② 關鍵字彙總"
        st.info(f"尚無關鍵字資料。請在左側選擇「{stage_hint}」或更高階段後重新執行。")

# ── Tab 3：產業分析 ──────────────────────────────────────
with tab_industry:
    industries = data.get("industries", [])
    if industries:
        for ind in industries:
            icon = SENTIMENT_ICON.get(ind["sentiment"], "➡️")
            with st.expander(f"{ind['industry']}  {icon} {ind['sentiment']}", expanded=True):
                st.markdown(f"**關聯關鍵字：** {', '.join(ind['keywords'])}")
                st.markdown(f"**分析：** {ind['explanation']}")
                if ind.get("fundswap_url"):
                    st.markdown(f"[🔗 前往好好證券篩選相關基金]({ind['fundswap_url']})")
                else:
                    st.caption("好好證券篩選連結待設定（請更新 `industry_map.py` 中的 `INDUSTRY_FUNDSWAP_MAP`）")
    elif data.get("stage") in ("news", "keywords"):
        st.info("尚未執行產業分析。請在左側選擇「③ 完整分析（含產業）」後重新執行。")
    else:
        st.info("目前沒有符合關鍵字的產業資料，可能是今日新聞尚無相關詞彙。")
