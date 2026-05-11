"""K-Means 分群模組：訓練、評估、預測財務人物類型"""
import joblib
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

FEATURE_COLS = [
    'salary_ratio', 'dividend_ratio', 'interest_ratio',
    'rental_ratio', 'business_ratio', 'shannon_entropy'
]

# 依 K-Means K=5 實際群心特徵命名（三項指標 Silhouette/Davies-Bouldin/Calinski-H 均最優）
# cluster 0: 薪資31.8%+股利48.0% → 薪資投資型
# cluster 1: 股利49.0%+執行業務14.5% → 自雇型
# cluster 2: 股利49.8%+租賃14.7%+利息13.4% → 多元資產型
# cluster 3: 股利72.4%（高度集中）→ 股利集中型
# cluster 4: 利息29.2%（偏高）→ 保守固定型
CLUSTER_NAMES = {
    0: '薪資投資型',
    1: '自雇型',
    2: '多元資產型',
    3: '股利集中型',
    4: '保守固定型',
}


def find_best_k(X_scaled: np.ndarray, k_range=range(2, 9)) -> dict:
    """執行 Elbow Method 與 Silhouette Score，回傳評估結果字典"""
    results = []
    for k in k_range:
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = km.fit_predict(X_scaled)
        sil = silhouette_score(X_scaled, labels)
        results.append({'k': k, 'inertia': km.inertia_, 'silhouette': sil})
    return pd.DataFrame(results)


def train_and_save(df: pd.DataFrame, k: int = 4,
                   model_path: str = 'models/kmeans_model.pkl') -> tuple:
    """訓練 K-Means 模型並存檔，回傳 (model, scaler, cluster_names)"""
    X = df[FEATURE_COLS].values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)

    bundle = {
        'model': km,
        'scaler': scaler,
        'feature_cols': FEATURE_COLS,
        'cluster_names': CLUSTER_NAMES,
    }
    joblib.dump(bundle, model_path)
    return km, scaler


def predict_persona(user_features: dict,
                    model_path: str = 'models/kmeans_model.pkl') -> str:
    """
    輸入使用者所得特徵字典，回傳財務人物類型名稱。
    user_features 範例：
    {
      'salary_ratio': 0.8, 'dividend_ratio': 0.05, 'interest_ratio': 0.1,
      'rental_ratio': 0.0, 'business_ratio': 0.05, 'shannon_entropy': 0.9
    }
    """
    bundle = joblib.load(model_path)
    km = bundle['model']
    scaler = bundle['scaler']
    cols = bundle['feature_cols']
    names = bundle['cluster_names']

    X = np.array([[user_features.get(c, 0.0) for c in cols]])
    X_scaled = scaler.transform(X)
    cluster = int(km.predict(X_scaled)[0])
    return names.get(cluster, f'類型{cluster}')
