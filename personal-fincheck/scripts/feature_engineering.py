"""特徵工程模組：計算所得佔比、Shannon Entropy、稅務負擔率"""
import numpy as np
import pandas as pd

INCOME_COLS = ['salary', 'dividend', 'interest', 'rental', 'business', 'other']


def compute_income_ratios(df: pd.DataFrame) -> pd.DataFrame:
    """計算各類所得佔總所得的比例（0~1），作為 K-Means 特徵"""
    df = df.copy()
    for col in INCOME_COLS:
        df[f'{col}_ratio'] = df[col] / df['total_income'].replace(0, np.nan)
    return df.fillna(0)


def compute_shannon_entropy(df: pd.DataFrame) -> pd.Series:
    """
    計算所得多元化程度（Shannon Entropy）。
    H = -sum(p * log2(p))，值越高代表來源越分散。
    最大值 = log2(6) ≈ 2.585（六類所得完全均等時）
    """
    ratio_cols = [f'{col}_ratio' for col in INCOME_COLS]
    ratios = df[ratio_cols].values
    ratios_safe = np.where(ratios > 0, ratios, 1e-10)
    entropy = -np.sum(ratios_safe * np.log2(ratios_safe), axis=1)
    return pd.Series(entropy, index=df.index, name='shannon_entropy')


def compute_tax_burden_rate(df: pd.DataFrame) -> pd.Series:
    """稅務負擔率 = 扣繳稅額 / 總所得（用於稅務效率評分）"""
    rate = df['withholding_tax'] / df['total_income'].replace(0, np.nan)
    return rate.fillna(0).rename('tax_burden_rate')


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """整合所有特徵，回傳可供 K-Means 使用的 DataFrame"""
    df = compute_income_ratios(df)
    df['shannon_entropy'] = compute_shannon_entropy(df)
    df['tax_burden_rate'] = compute_tax_burden_rate(df)
    return df
