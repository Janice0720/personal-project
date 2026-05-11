"""
FinCheck — 個人財務健檢 AI 系統
Streamlit 互動儀表板
執行：cd app && streamlit run streamlit_app.py
"""
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from feature_engineering import INCOME_COLS
from clustering import predict_persona, CLUSTER_NAMES
from scoring import (
    get_fincheck_scores, generate_recommendations,
    PERSONA_DESCRIPTIONS, MAX_ENTROPY
)
from pdf_parser import parse_mydata_pdf

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'kmeans_model.pkl')

# ══════════════════════════════════════════════════════════
# 共用：執行分析並渲染結果
# ══════════════════════════════════════════════════════════
def run_analysis(salary, dividend, interest, rental, business, other, withholding):
    total = salary + dividend + interest + rental + business + other
    if total == 0:
        st.error("請至少輸入一項所得金額。")
        return

    amounts = [salary, dividend, interest, rental, business, other]
    ratios  = {f'{col}_ratio': amt / total for col, amt in zip(INCOME_COLS, amounts)}

    vals      = np.array(list(ratios.values()))
    vals_safe = np.where(vals > 0, vals, 1e-10)
    entropy   = float(-np.sum(vals_safe * np.log2(vals_safe)))
    ratios['shannon_entropy'] = entropy

    persona  = predict_persona(ratios, model_path=MODEL_PATH)
    tax_rate = withholding / total
    scores   = get_fincheck_scores(entropy, tax_rate, total)
    tips     = generate_recommendations(
        persona, scores['diversification_score'], scores['tax_efficiency_score']
    )

    # ── 核心指標 ──────────────────────────────────────────
    st.divider()
    st.header("📊 你的財務健檢報告")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("財務人物類型",   persona)
    col2.metric("所得多元化評分", f"{scores['diversification_score']} 分 / 100")
    col3.metric("稅務效率評分",   f"{scores['tax_efficiency_score']} 分 / 100")
    col4.metric("年度總所得",     f"NT$ {total:,.0f}")
    st.caption(f"📌 {PERSONA_DESCRIPTIONS.get(persona, '')}")
    st.divider()

    # ── 圓餅圖 + 雷達圖 ───────────────────────────────────
    col_left, col_right = st.columns(2)
    with col_left:
        labels_zh = ['薪資', '股利/營利', '利息', '租賃', '執行業務', '其他']
        values    = [salary, dividend, interest, rental, business, other]
        non_zero  = [(l, v) for l, v in zip(labels_zh, values) if v > 0]
        if non_zero:
            fig_pie = px.pie(
                names=[x[0] for x in non_zero],
                values=[x[1] for x in non_zero],
                title="所得來源結構",
                color_discrete_sequence=px.colors.qualitative.Set2,
                hole=0.35
            )
            fig_pie.update_traces(textinfo='percent+label')
            st.plotly_chart(fig_pie, use_container_width=True)

    with col_right:
        div_score = scores['diversification_score']
        tax_score = scores['tax_efficiency_score']
        overall   = int((div_score + tax_score) / 2)
        fig_radar = go.Figure(go.Scatterpolar(
            r=[div_score, tax_score, overall, div_score],
            theta=['所得多元化', '稅務效率', '整體健康度', '所得多元化'],
            fill='toself',
            line_color='#2E86AB'
        ))
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            title='財務健檢雷達圖',
            showlegend=False
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    # ── 稅務效率 ──────────────────────────────────────────
    st.divider()
    with st.expander("🧾 稅務效率詳細說明"):
        b = scores['benchmark_tax_rate']
        u = scores['user_tax_rate']
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("你的扣繳稅率",     f"{u*100:.1f}%")
        col_b.metric("同所得層基準稅率", f"{b*100:.1f}%")
        diff = (u - b) * 100
        col_c.metric("與基準差距",       f"{diff:+.1f}%", delta_color="inverse")
        st.caption(f"所得分位群組：{scores['income_group']}｜年度總所得：NT$ {total:,.0f}")

    # ── 個人化建議 ────────────────────────────────────────
    st.divider()
    st.subheader("💡 個人化理財建議")
    for i, tip in enumerate(tips, 1):
        st.info(f"**建議 {i}**｜{tip}")

    # ── AI 分群說明 ───────────────────────────────────────
    st.divider()
    with st.expander("🤖 AI 分群說明（K-Means 模型）"):
        st.markdown("""
        本系統使用 **K-Means 分群（K=5）** 分析 3,000 筆合成個體資料（基於財政部 111 年度統計），
        依所得結構特徵分為五種財務人物類型：

        | 人物類型 | 特徵描述 |
        |---|---|
        | 薪資投資型 | 薪資 ~32% 搭配股利 ~48%，最典型的上班族投資人 |
        | 自雇型 | 執行業務所得 ~14.5% 搭配股利，屬自雇或兼業複合所得結構 |
        | 股利集中型 | 股利所得佔比 > 70%，高度集中於股票/ETF |
        | 保守固定型 | 利息所得佔比 > 25%，偏好定存/債券等固定收益 |
        | 多元資產型 | 股利、租賃、利息三類並重，資產最為分散 |

        **模型評估（K=2～8 全面比較）**：
        - Silhouette Score（K=5）= **0.310**（所有 K 值最高）
        - Davies-Bouldin（K=5）= **1.048**（所有 K 值最低，越低越好）
        - Calinski-Harabasz（K=5）= **1088**（所有 K 值最高）
        - 分群穩定性：10 個不同初始值均收斂至相同結果（std = 0.0001）
        """)


# ══════════════════════════════════════════════════════════
# 頁面設定
# ══════════════════════════════════════════════════════════
st.set_page_config(
    page_title="FinCheck 個人財務健檢",
    page_icon="💰",
    layout="wide"
)

st.title("💰 FinCheck — 個人財務健檢 AI 系統")
st.caption(
    "基於 **MyData 個人所得資料（財政部財政資訊中心）** × "
    "**財政部 111 年統計** × **K-Means 分群（K=5）**｜"
    "資料來源：[data.gov.tw](https://data.gov.tw)"
)

tab_pdf, tab_manual = st.tabs(["📄 上傳 MyData PDF（推薦）", "✏️ 手動輸入"])


# ══════════════════════════════════════════════════════════
# Tab 1：上傳 PDF
# ══════════════════════════════════════════════════════════
with tab_pdf:
    st.markdown(
        "上傳你從 **MyData 平台 → 財政部財政資訊中心 → 個人所得資料** 申請的"
        "「年度綜合所得稅各類所得資料清單」PDF，系統自動解析所有所得明細。"
    )

    uploaded = st.file_uploader(
        "選擇 PDF 檔案",
        type=['pdf'],
        help="財政部 MyData 個人所得資料 PDF，無需手動輸入任何數字"
    )

    if not uploaded:
        st.info(
            "**如何取得個人所得資料 PDF？**\n\n"
            "1. 前往 [MyData 平台](https://mydata.nat.gov.tw) 登入（自然人憑證或行動身分識別）\n"
            "2. 選擇「**財政部財政資訊中心**」→「**個人所得資料**」\n"
            "3. 選擇申報年度，下載 PDF\n"
            "4. 將 PDF 上傳至此欄位",
            icon="ℹ️"
        )
    else:
        with st.spinner("正在解析 PDF，請稍候..."):
            try:
                result = parse_mydata_pdf(uploaded)
            except Exception as e:
                st.error(f"PDF 解析失敗：{e}")
                st.info("請確認上傳的是財政部「年度綜合所得稅各類所得資料清單」PDF。")
                result = None

        if result:
            t = result['totals']

            # 解析結果標頭
            name = result['taxpayer_name'] or '—'
            year = result['tax_year']      or '—'
            col_info, col_verify = st.columns([3, 1])
            with col_info:
                st.success(
                    f"✅ PDF 解析成功｜納稅義務人：**{name}**｜"
                    f"年度：**{year}**｜共 **{len(result['records'])}** 筆所得記錄"
                )
            with col_verify:
                if result['match_ok']:
                    st.metric("合計驗證", f"NT$ {t['total_income']:,.0f}", "✅ 與 PDF 吻合")
                else:
                    st.metric("合計驗證", f"NT$ {t['total_income']:,.0f}",
                              "⚠️ 有差異", delta_color="inverse")

            # 所得結構摘要
            st.markdown("#### 解析到的所得結構")
            label_map = [
                ('salary',   '薪資所得'),
                ('dividend', '股利/營利所得'),
                ('interest', '利息所得'),
                ('rental',   '租賃所得'),
                ('business', '執行業務所得'),
                ('other',    '其他所得'),
            ]
            shown = [(zh, t[cat]) for cat, zh in label_map if t[cat] > 0]
            s_cols = st.columns(max(len(shown), 1))
            for idx, (zh, amt) in enumerate(shown):
                s_cols[idx].metric(zh, f"NT$ {amt:,.0f}")

            # 所得明細
            with st.expander(f"📋 所得明細（共 {len(result['records'])} 筆）"):
                cat_zh = {
                    'salary': '薪資', 'dividend': '股利/營利',
                    'interest': '利息', 'rental': '租賃',
                    'business': '執行業務', 'other': '其他'
                }
                rows = [
                    {
                        '類別': cat_zh.get(r['category'], r['category']),
                        '扣繳單位': r['source'] or '—',
                        '給付總額（元）': f"{r['amount']:,}",
                        '扣繳稅額（元）': f"{r['withholding']:,}",
                    }
                    for r in result['records']
                ]
                st.dataframe(rows, use_container_width=True, hide_index=True)

            # 執行分析
            run_analysis(
                salary=t['salary'],
                dividend=t['dividend'],
                interest=t['interest'],
                rental=t['rental'],
                business=t['business'],
                other=t['other'],
                withholding=t['withholding_tax'],
            )


# ══════════════════════════════════════════════════════════
# Tab 2：手動輸入
# ══════════════════════════════════════════════════════════
with tab_manual:
    st.markdown("直接輸入各類年度所得金額（元），適合沒有 MyData PDF 的情況。")

    c1, c2 = st.columns(2)
    with c1:
        m_salary   = st.number_input("薪資所得",      min_value=0, value=600_000, step=10_000, format="%d")
        m_dividend = st.number_input("股利/營利所得",  min_value=0, value=200_000, step=10_000, format="%d")
        m_interest = st.number_input("利息所得",      min_value=0, value=50_000,  step=5_000,  format="%d")
    with c2:
        m_rental   = st.number_input("租賃所得",      min_value=0, value=0,       step=10_000, format="%d")
        m_business = st.number_input("執行業務所得",   min_value=0, value=0,       step=10_000, format="%d")
        m_other    = st.number_input("其他所得",      min_value=0, value=0,       step=5_000,  format="%d")
    m_withholding = st.number_input("扣繳稅額合計",   min_value=0, value=60_000,  step=5_000,  format="%d")

    if st.button("🔍 開始健檢", type="primary", use_container_width=True):
        run_analysis(
            salary=m_salary,
            dividend=m_dividend,
            interest=m_interest,
            rental=m_rental,
            business=m_business,
            other=m_other,
            withholding=m_withholding,
        )
