"""
Task 4：K-Means 分群建模
執行：python3 scripts/train_model.py
產出：models/kmeans_model.pkl + 評估報告
"""
import sys, os
sys.path.append(os.path.dirname(__file__))

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from clustering import FEATURE_COLS, CLUSTER_NAMES, find_best_k, train_and_save

df = pd.read_csv('data/processed/synthetic_data.csv')
X = df[FEATURE_COLS].values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 1：Elbow Method + Silhouette Score
print("=== Elbow Method & Silhouette Score ===")
eval_df = find_best_k(X_scaled)
print(eval_df.to_string(index=False))

best_k = int(eval_df.loc[eval_df['silhouette'].idxmax(), 'k'])
best_sil = eval_df['silhouette'].max()
print(f"\n建議最佳 K 值：{best_k}（Silhouette Score = {best_sil:.4f}）")

# Step 2：以 K=5 訓練（三項指標均指向 K=5 為最佳分群數）
FINAL_K = 5
km, _ = train_and_save(df, k=FINAL_K, model_path='models/kmeans_model.pkl')

df['cluster'] = km.predict(X_scaled)
df['persona'] = df['cluster'].map(CLUSTER_NAMES)

# Step 3：顯示各群特徵均值（用於命名確認）
print(f"\n=== 各群特徵均值（K={FINAL_K}）===")
profile = df.groupby('cluster')[FEATURE_COLS + ['persona']].agg(
    {col: 'mean' for col in FEATURE_COLS} | {'persona': 'first'}
).round(3)
print(profile.to_string())

# Step 4：分群人數分佈
print("\n=== 分群結果人數 ===")
print(df['persona'].value_counts().to_string())

# Step 5：各群平均總所得
print("\n=== 各群平均總所得（元）===")
print(df.groupby('persona')['total_income'].mean().apply(lambda x: f'{x:,.0f}').to_string())

print("\n✅ 模型已儲存至 models/kmeans_model.pkl")
