# thesis-investor-segmentation

應用投資人行為分群與個人化推薦模型於數位券商基金投資服務之研究
國立臺北商業大學 資訊與決策科學研究所（在職碩班）碩士論文專案

---

## 目標

整合好好證券 GA4 使用者行為資料與基金交易資料，建立投資人行為分群模型，並設計個人化基金推薦機制，驗證其優於熱門推薦之效果。

## 方法

- **分群**：RFM 指標擴充特徵 + K-means / K-prototypes
- **推薦**：Collaborative Filtering（User-Based / Item-Based）+ 熱門推薦 Baseline 比較
- **評估**：Precision@K、Recall@K、MAP

## 預計畢業

2027 年 6 月

## 資料夾結構

```
thesis-investor-segmentation/
├── README.md                     ← 本檔案
├── thesis-research-plan.md       ← 完整研究規劃（文獻、時程、資料需求）
├── thesis-writing-plan.md        ← 論文撰寫待辦清單（Phase 0–8 完整計畫）
├── literature/
│   ├── literature-matrix.md      ← 文獻矩陣（26 篇含連結）
│   └── notes/                    ← 各篇文獻閱讀筆記
├── data/
│   ├── raw/                      ← 原始匿名化數據（不上 Git）
│   └── processed/                ← 清洗後特徵數據
├── notebooks/
│   ├── 01-eda.ipynb
│   ├── 02-clustering.ipynb
│   └── 03-recommendation.ipynb
├── scripts/
│   ├── feature_engineering.py
│   └── evaluation.py
└── thesis/
    └── chapters/
```

## 結論

> 尚在研究中，預計 2027 年完成。
