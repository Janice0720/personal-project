"""
Task 7 素材生成：分群結果圖表
產出：
  reports/charts/01_elbow_method.png
  reports/charts/02_silhouette_scores.png
  reports/charts/03_cluster_income_structure.png   ← 給 B、C 的主要圖表
  reports/charts/04_cluster_summary_table.png
"""
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__)))

import joblib
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

from feature_engineering import build_features, INCOME_COLS
from clustering import CLUSTER_NAMES, FEATURE_COLS, find_best_k

OUT_DIR   = os.path.join(os.path.dirname(__file__), '..', 'reports', 'charts')
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed', 'synthetic_data.csv')

# ── 載入資料與特徵 ────────────────────────────────────────
df = build_features(pd.read_csv(DATA_PATH))
X  = df[FEATURE_COLS].values
scaler   = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ── 模型重新訓練（取得 cluster 標籤）────────────────────────
km = KMeans(n_clusters=5, random_state=42, n_init=10)
df['cluster'] = km.fit_predict(X_scaled)
df['persona'] = df['cluster'].map(CLUSTER_NAMES)

# ── Chart 1：Elbow Method ─────────────────────────────────
print("生成圖 1：Elbow Method ...")
eval_df = find_best_k(X_scaled)
fig1 = go.Figure()
fig1.add_trace(go.Scatter(
    x=eval_df['k'], y=eval_df['inertia'],
    mode='lines+markers',
    marker=dict(size=9, color='#2E86AB'),
    line=dict(width=2, color='#2E86AB'),
    name='Inertia'
))
fig1.add_vline(x=5, line_dash='dash', line_color='red',
               annotation_text='選定 K=5', annotation_position='top right')
fig1.update_layout(
    title='Elbow Method — 選定最佳群數 K',
    xaxis_title='K（群數）',
    yaxis_title='Inertia（組內平方和）',
    template='plotly_white',
    width=700, height=420
)
fig1.write_image(os.path.join(OUT_DIR, '01_elbow_method.png'), scale=2)

# ── Chart 2：Silhouette Score ─────────────────────────────
print("生成圖 2：Silhouette Score ...")
colors = ['#A8D8EA' if k != 5 else '#2E86AB' for k in eval_df['k']]
fig2 = go.Figure(go.Bar(
    x=eval_df['k'], y=eval_df['silhouette'].round(4),
    marker_color=colors,
    text=eval_df['silhouette'].round(3),
    textposition='outside',
))
fig2.add_vline(x=5, line_dash='dash', line_color='red',
               annotation_text='選定 K=5', annotation_position='top right')
fig2.update_layout(
    title='Silhouette Score — 各 K 值分群品質評估',
    xaxis_title='K（群數）',
    yaxis_title='Silhouette Score（越接近 1 越好）',
    yaxis=dict(range=[0, 0.6]),
    template='plotly_white',
    width=700, height=420
)
fig2.write_image(os.path.join(OUT_DIR, '02_silhouette_scores.png'), scale=2)

# ── Chart 3：各群體所得結構長條圖（給 B、C 的主要圖表）────────
print("生成圖 3：各群體所得結構長條圖 ...")

INCOME_ZH = {
    'salary':   '薪資所得',
    'dividend': '股利/營利所得',
    'interest': '利息所得',
    'rental':   '租賃所得',
    'business': '執行業務所得',
    'other':    '其他所得',
}
COLORS = ['#3D9970', '#2E86AB', '#E87722', '#C94040', '#8B5CF6', '#6B7280']
ratio_cols = [f'{c}_ratio' for c in INCOME_COLS]
persona_order = ['薪資投資型', '自雇型', '股利集中型', '保守固定型', '多元資產型']

cluster_means = (
    df.groupby('persona')[ratio_cols].mean()
    .reindex(persona_order)
    .rename(columns={f'{c}_ratio': zh for c, zh in INCOME_ZH.items()})
    .multiply(100)  # 轉為 %
)

fig3 = go.Figure()
for col, color in zip(cluster_means.columns, COLORS):
    vals = cluster_means[col].values
    if vals.sum() < 0.5:
        continue
    fig3.add_trace(go.Bar(
        name=col,
        x=cluster_means.index,
        y=vals.round(1),
        marker_color=color,
        text=[f'{v:.1f}%' if v >= 3 else '' for v in vals],
        textposition='inside',
        textfont=dict(color='white', size=11),
    ))

fig3.update_layout(
    barmode='stack',
    title={
        'text': '五種財務人物類型 — 各類所得結構佔比（%）',
        'font': dict(size=18)
    },
    xaxis_title='財務人物類型',
    yaxis_title='所得佔比（%）',
    yaxis=dict(range=[0, 105]),
    legend=dict(
        orientation='h',
        yanchor='bottom', y=1.02,
        xanchor='right', x=1
    ),
    template='plotly_white',
    width=860, height=520
)
fig3.write_image(os.path.join(OUT_DIR, '03_cluster_income_structure.png'), scale=2)

# ── Chart 4：人物摘要表（文字版） ─────────────────────────
print("生成圖 4：分群摘要表 ...")
PERSONA_SUMMARY = {
    '薪資投資型': {
        '特徵': '薪資 ~32% + 股利 ~48%',
        '人數（3000筆）': 870,
        '核心行動（給 B）': '最典型上班族投資人，薪資穩定且持有 ETF/股票',
        '理財建議方向（給 C）': '建立緊急預備金 → 提高投資比例'
    },
    '自雇型': {
        '特徵': '股利 ~49% + 執行業務 ~14.5%',
        '人數（3000筆）': 140,
        '核心行動（給 B）': '兼具業務收入與股利，屬複合所得的自雇或兼業者',
        '理財建議方向（給 C）': '強化退休規劃（勞退自提）+ 保障型保險'
    },
    '股利集中型': {
        '特徵': '股利高達 ~72%',
        '人數（3000筆）': 1083,
        '核心行動（給 B）': '高度依賴股利，可能是退休族或財務自由者',
        '理財建議方向（給 C）': '分散持股至寬基 ETF，降低個股風險'
    },
    '保守固定型': {
        '特徵': '利息 ~29%，低風險偏好',
        '人數（3000筆）': 707,
        '核心行動（給 B）': '偏好定存/債券等固定收益',
        '理財建議方向（給 C）': '升息循環後可部分轉向股息型資產'
    },
    '多元資產型': {
        '特徵': '股利 ~50% + 租賃 ~15% + 利息 ~13%',
        '人數（3000筆）': 200,
        '核心行動（給 B）': '股利/租賃/利息三類並重，最多元',
        '理財建議方向（給 C）': '定期再平衡（Rebalancing），維持目標比例'
    },
}

summary_df = pd.DataFrame(PERSONA_SUMMARY).T.reset_index()
summary_df.columns = ['人物類型', '所得特徵', '樣本人數', '人物描述（B撰寫方向）', '建議方向（C撰寫方向）']

fig4 = go.Figure(go.Table(
    columnwidth=[120, 180, 100, 220, 250],
    header=dict(
        values=[f'<b>{c}</b>' for c in summary_df.columns],
        fill_color='#2E86AB',
        font=dict(color='white', size=12),
        align='left',
        height=36,
    ),
    cells=dict(
        values=[summary_df[c] for c in summary_df.columns],
        fill_color=[['#EAF4FB', '#F7FBFE'] * 4],
        font=dict(size=11),
        align='left',
        height=40,
    )
))
fig4.update_layout(
    title='分群結果摘要表（供 B、C 撰寫素材用）',
    width=950, height=360,
    margin=dict(l=20, r=20, t=60, b=20)
)
fig4.write_image(os.path.join(OUT_DIR, '04_cluster_summary_table.png'), scale=2)

print("\n✅ 全部圖表已儲存至 reports/charts/")
for fn in sorted(os.listdir(OUT_DIR)):
    if fn.endswith('.png'):
        print(f"   {fn}")
