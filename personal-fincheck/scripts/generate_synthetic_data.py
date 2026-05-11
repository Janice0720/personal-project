"""
Task 2：合成個體資料生成
依財政部 111 年度 20 分位統計，生成 3,000 筆模擬台灣個人所得資料。
執行：python3 scripts/generate_synthetic_data.py
產出：data/processed/synthetic_data.csv
"""
import numpy as np
import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(__file__))
from feature_engineering import build_features

np.random.seed(42)

# 依 111 年度 20 分位統計設定各所得群組的特徵分佈
# 資料來源：111_綜所稅各類所得20分位統計.csv（佔比 %）
# 分為五群：low / mid_low / mid / mid_high / high（對應 5 分位）
INCOME_PROFILES = {
    'low': {
        'salary': 24.1, 'dividend': 52.7, 'interest': 13.9,
        'rental': 0.9,  'business': 1.9,  'other': 6.5
    },
    'mid_low': {
        'salary': 18.0, 'dividend': 56.0, 'interest': 14.2,
        'rental': 1.7,  'business': 1.8,  'other': 8.3
    },
    'mid': {
        'salary': 19.0, 'dividend': 55.5, 'interest': 14.1,
        'rental': 1.8,  'business': 1.7,  'other': 7.9
    },
    'mid_high': {
        'salary': 15.0, 'dividend': 59.7, 'interest': 15.0,
        'rental': 1.9,  'business': 1.3,  'other': 7.1
    },
    'high': {
        'salary': 11.0, 'dividend': 61.1, 'interest': 16.8,
        'rental': 2.6,  'business': 0.9,  'other': 7.6
    },
}

# 5 分位薪資收入均值（千元）→ 換算為元作為總收入基準
# 資料來源：111_綜所稅各類所得5分位統計.csv
INCOME_BASE_TWD = {
    'low':      197_740,
    'mid_low':  140_220,
    'mid':      119_330,
    'mid_high': 103_170,
    'high':      74_410,
}

# 各群組的基準扣繳稅率（依所得高低遞增）
BASE_TAX_RATES = {
    'low': 0.05, 'mid_low': 0.08, 'mid': 0.11, 'mid_high': 0.14, 'high': 0.17,
}

GROUPS = list(INCOME_PROFILES.keys())
N_PER_GROUP = 600  # 每群 600 筆，共 3,000 筆

records = []
for group in GROUPS:
    profile = INCOME_PROFILES[group]
    base = INCOME_BASE_TWD[group]
    tax_rate = BASE_TAX_RATES[group]

    for _ in range(N_PER_GROUP):
        # log-normal 分佈模擬真實所得分散程度
        total_income = int(np.random.lognormal(
            mean=np.log(base), sigma=0.4
        ))
        # Dirichlet 擾動模擬個體所得結構差異
        proportions = np.array(list(profile.values())) / 100
        noisy_prop = np.random.dirichlet(proportions * 10)

        row = {'group': group, 'total_income': total_income}
        for col, prop in zip(profile.keys(), noisy_prop):
            row[col] = int(total_income * prop)

        # 扣繳稅額加入隨機擾動（±20%）
        row['withholding_tax'] = int(
            total_income * tax_rate * np.random.uniform(0.8, 1.2)
        )
        records.append(row)

df = pd.DataFrame(records)

# 驗證：各群薪資佔比均值應接近 INCOME_PROFILES 設定值
print("=== 合成資料驗證：各群薪資佔比均值 vs. 目標值 ===")
for grp in GROUPS:
    sub = df[df['group'] == grp]
    actual = (sub['salary'] / sub['total_income']).mean() * 100
    target = INCOME_PROFILES[grp]['salary']
    diff = abs(actual - target)
    status = "✅" if diff < 5 else "⚠️"
    print(f"  {grp:10s}: 實際 {actual:5.1f}%  目標 {target:5.1f}%  差異 {diff:.1f}%  {status}")

# 套用特徵工程
df = build_features(df)

# 儲存
out_path = 'data/processed/synthetic_data.csv'
df.to_csv(out_path, index=False)
print(f"\n✅ 已儲存：{out_path}")
print(f"   筆數：{len(df)}  欄位：{len(df.columns)}")
print(f"\n特徵欄位統計：")
feat_cols = ['shannon_entropy', 'tax_burden_rate', 'salary_ratio', 'dividend_ratio']
print(df[feat_cols].describe().round(3).to_string())
