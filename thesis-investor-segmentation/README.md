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

## 目前進度（重新盤點版）

> 目前進度以 `project-status.md` 為總控表。先前多位 agent 已產出 Phase 1 / Proposal 素材，但 Phase 0 的研究邊界仍需重新人工確認，因此不再將 Phase 0 標為完成。

| 階段 | 時程 | 工作內容摘要 | 目前狀態 |
|------|------|---|---|
| Phase 0：研究題目與邊界確認 | 2026/04 | 確認題目、研究範圍、研究對象、資料可行性、不做事項與初步研究問題 | 🟡 重整中：已有規劃草稿，但尚待人工確認 |
| Phase 1：文獻整理與研究計畫書素材 | 2026/05–06 | 盤點文獻、分類文獻、建立閱讀順序、整理研究缺口與貢獻素材 | 🟡 已完成第一輪整併，待來源查證與引用格式整理 |
| Proposal：研究計畫書 | 2026/06 | 將 Phase 0 邊界與 Phase 1 文獻整理成正式 Proposal | 🟠 有草稿，不定稿：目前僅作素材庫 |
| Phase 2：資料取得與倫理準備 | 2026/07 | 確認公司授權、IRB / 倫理需求、資料脫敏、資料字典與原始資料匯出 | ⏳ 待開始 |
| Phase 3：資料清理、EDA 與特徵工程 | 2026/08 | 清理 GA4 / 交易 / 用戶資料，完成 EDA 與 user-level 特徵表 | ⏳ 未開始 |
| Phase 4：投資人行為分群模型 | 2026/09–10 | 建立 RFM / 行為特徵分群，選 K 值、命名群體並解釋商業意義 | ⏳ 未開始 |
| Phase 5：個人化推薦概念驗證 | 2026/11–12 | 建立熱門推薦 baseline、協同過濾 / 矩陣分解或分群輔助推薦概念驗證 | ⏳ 未開始 |
| Phase 6：模型評估與比較分析 | 2027/01 | 使用 Precision@K、Recall@K、MAP 等指標比較模型與 baseline | ⏳ 未開始 |
| Phase 7：論文撰寫 | 2027/02–03 | 撰寫第一至五章、統一引用格式、整理圖表與附錄 | ⏳ 未開始 |
| Phase 8：口試準備與畢業 | 2027/04–06 | 準備預口試 / 正式口試簡報、Q&A、修改與畢業送審 | ⏳ 未開始 |

**預計畢業**：2027 年 6 月

## 資料夾結構

```
thesis-investor-segmentation/
├── README.md                               ← 本檔案
├── project-status.md                       ← 論文專案進度總控表 ✅
├── thesis-research-plan.md                 ← 完整研究規劃（文獻、時程、資料需求）🟡 已同步第一輪進度，待 Phase 0 定稿
├── thesis-writing-plan.md                  ← 論文撰寫待辦清單（Phase 0–8 完整計畫）🟡 已同步第一輪待辦狀態
├── literature/
│   ├── literature-matrix.md                ← 整合版文獻矩陣（已合併原始矩陣與 Phase 1 補強）✅
│   ├── phase1/
│   │   └── phase1-literature-matrix-2026-06-22.md ← Phase 1 文獻矩陣補強原始紀錄（已併入主矩陣）✅
│   ├── chiou-wei-2024-kl-km-reading-summary.md   ← Chiou-Wei 2024 精讀摘要 ✅
│   └── chiou-wei-2024-kl-km-fund-recommendation-report.md ← 課堂報告素材 ✅
├── proposal/
│   └── phase1/
│       ├── README.md                        ← Phase 1 agent 產出索引 ✅
│       ├── proposal-draft-master.md         ← Proposal 初稿主檔 ✅
│       ├── consistency-check-literature-vs-proposal.md ← 文獻矩陣與 Proposal 一致性檢查 ✅
│       ├── reading-order-and-goals.md       ← 文件閱讀順序與閱讀目標 ✅
│       ├── 01-literature-structure-gap-contribution-integrated.md ← 文獻架構、研究缺口與貢獻整合稿 ✅
│       ├── 02-research-gap-analysis.md      ← 研究缺口分析 ✅
│       ├── 03-research-contribution-claims.md ← 研究貢獻主張 ✅
│       └── 04-phase1-literature-context-gap-final.md ← Phase 1 最終整合稿 ✅
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
            ├── 01-investor-behavior-segmentation-rfm.md ← 第二章前三類文獻脈絡草稿 ✅
            └── 02-recommendation-fintech-digital-brokerage.md ← 第二章後三類文獻脈絡草稿 ✅
```

## 結論

> 研究進行中，預計 2027 年 6 月完成口試與畢業。
