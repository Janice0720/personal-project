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

## 目前進度（2026-06-21）

| 階段 | 時程 | 狀態 |
|------|------|------|
| Phase 0：前置準備 | 2026/04 | ✅ 完成 |
| Phase 1：文獻整理與研究計畫書 | 2026/05–06 | 🔄 進行中（文獻矩陣已建立，待完成 Proposal 初稿） |
| Phase 2：資料取得與倫理準備 | 2026/07 | ⏳ 待開始 |
| Phase 3：資料清理、EDA 與特徵工程 | 2026/08 | ⏳ 待開始 |
| Phase 4：投資人行為分群模型 | 2026/09–10 | ⏳ 待開始 |
| Phase 5：個人化推薦模型 | 2026/11–12 | ⏳ 待開始 |
| Phase 6：模型評估與比較分析 | 2027/01 | ⏳ 待開始 |
| Phase 7：論文撰寫 | 2027/02–03 | ⏳ 待開始 |
| Phase 8：口試準備與畢業 | 2027/04–06 | ⏳ 待開始 |

**預計畢業**：2027 年 6 月

## 資料夾結構

```
thesis-investor-segmentation/
├── README.md                               ← 本檔案
├── thesis-research-plan.md                 ← 完整研究規劃（文獻、時程、資料需求）✅
├── thesis-writing-plan.md                  ← 論文撰寫待辦清單（Phase 0–8 完整計畫）✅
├── literature/
│   ├── literature-matrix.md                ← 文獻矩陣（26 篇含連結）✅
│   ├── phase1/
│   │   └── phase1-literature-matrix-2026-06-22.md ← Phase 1 文獻矩陣補強 ✅
│   ├── chiou-wei-2024-kl-km-reading-summary.md   ← Chiou-Wei 2024 精讀摘要 ✅
│   └── chiou-wei-2024-kl-km-fund-recommendation-report.md ← 課堂報告素材 ✅
├── proposal/
│   └── phase1/
│       ├── README.md                        ← Phase 1 agent 產出索引 ✅
│       ├── 01-literature-structure-gap-contribution-integrated.md ← 文獻架構、研究缺口與貢獻整合稿 ✅
│       ├── 02-research-gap-analysis.md      ← 研究缺口分析 ✅
│       └── 03-research-contribution-claims.md ← 研究貢獻主張 ✅
├── data/
│   ├── raw/                                ← 原始匿名化數據（不上 Git）⏳
│   └── processed/                          ← 清洗後特徵數據 ⏳
├── notebooks/
│   ├── 01-eda.ipynb                        ← 探索性資料分析 ⏳
│   ├── 02-clustering.ipynb                 ← 分群模型 ⏳
│   └── 03-recommendation.ipynb             ← 推薦模型 ⏳
├── scripts/
│   ├── feature_engineering.py              ← 特徵工程腳本 ⏳
│   └── evaluation.py                       ← 評估指標計算 ⏳
└── thesis/
    └── chapters/
        └── chapter-02-literature-review/
            └── 01-investor-behavior-segmentation-rfm.md ← 第二章前三類文獻脈絡草稿 ✅
```

## 結論

> 研究進行中，預計 2027 年 6 月完成口試與畢業。
