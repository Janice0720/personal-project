# 碩士論文研究規劃文件

應用投資人行為分群與個人化推薦模型於數位券商基金投資服務之研究 — 研究規劃全覽（2026–2027）

> **目前同步狀態（依 `project-status.md`）：** 本文件為早期完整研究規劃草稿，後續以 `project-status.md` 作為專案進度總控。現階段定位調整為「分群為主，推薦模型做概念驗證」；Proposal 暫不定稿，需先完成 Phase 0 題目、範圍、研究對象與不做事項確認。

---

## 目錄

1. [論文概覽](#1-論文概覽)
2. [主題可行性評估](#2-主題可行性評估)
3. [相關文獻整理](#3-相關文獻整理)
4. [資料來源需求分析](#4-資料來源需求分析)
5. [研究時程規劃（在職學生版）](#5-研究時程規劃在職學生版)
6. [技術選型建議](#6-技術選型建議)
7. [研究風險與因應策略](#7-研究風險與因應策略)
8. [待討論事項（需與老師確認）](#8-待討論事項需與老師確認)
9. [下一步行動](#9-下一步行動)

---

## 1. 論文概覽

### 基本資訊

| 項目 | 內容 |
|------|------|
| 學校 | 國立臺北商業大學 |
| 所系 | 資訊與決策科學研究所（在職碩班） |
| 指導教授 | 王亦凡 教授 |
| 研究者職務 | 好好證券 — 數據分析 × 行銷 × PM |

### 論文題目（建議版）

**中文**：應用投資人行為分群與個人化推薦模型於數位券商基金投資服務之研究

**英文**：Investor Segmentation and Personalized Fund Recommendation Using Behavioral and Transaction Data in a Digital Brokerage Platform

### 研究目標摘要

整合使用者行為資料（GA4）與基金交易資料，建立投資人行為分群模型，並以簡化個人化基金推薦模型進行概念驗證，評估其相較熱門推薦 baseline 是否具有增量效果。現階段不以提出全新演算法或完整商用推薦系統為目標。

### 核心研究流程

```
資料蒐集 → 資料清理與特徵工程 → 投資人行為分群
       → 個人化推薦概念驗證 → 模型成效評估 → 結論與建議
```

---

## 2. 主題可行性評估

### 2.1 整體可行性：⭐⭐⭐⭐ 高度可行（附條件，Phase 0 重整中）

此研究主題具備充分的學術依據與實務價值，在台灣碩士論文中屬**創新性高、資料獨特**的研究設計，整體可行。但目前不應直接進入 Proposal 定稿，需先完成 Phase 0 研究邊界重整，特別是研究對象、資料期間、基金範圍與不做事項。

### 2.2 優勢分析

| 優勢面向 | 說明 |
|----------|------|
| **資料獨特性** | 好好證券的真實用戶 GA4 行為數據 + 基金交易數據，是大多數學者無法取得的第一手資料 |
| **學術新穎性** | GA4 事件行為數據整合基金交易的研究在台灣幾乎是空白，研究缺口明確 |
| **實務連結** | 研究者本身就是研究場域的利害關係人，對業務情境的掌握遠超純學術研究者 |
| **角色優勢** | 身兼 DA + 行銷 + PM，具備資料存取、業務詮釋與需求轉化能力 |
| **就業加乘** | 研究過程直接產出可在工作中應用的分群模型與推薦機制 |

### 2.3 前提確認狀態（已確認）

| # | 確認項目 | 狀態 | 說明 |
|---|----------|------|------|
| **1** | **公司資料授權** | ✅ 已確認 | 好好證券同意提供匿名化數據供學術研究使用 |
| **2** | **GA4 user_id 串接** | ✅ 已處理 | GA4 已發送內部 user_id，可與基金交易資料 join，雙軌整合完全可行 |
| **3** | **預計畢業時程** | ✅ 已確認 | 2027 年 6 月畢業，口試目標 2027 年 4–5 月 |
| **4** | **資料倫理/IRB** | 🟡 待確認 | 建議與王亦凡老師確認是否需申請校內 IRB；事先規劃資料脫敏流程 |
| **5** | **研究邊界** | 🟡 重整中 | 已初步確認分群為主、推薦模型為概念驗證；仍需確認研究對象、資料期間、基金範圍與不做事項 |

### 2.4 在職學生可行性評估

| 評估面向 | 說明 |
|----------|------|
| **時間管理** | 在職學生每週可投入研究時間有限（估計 10–15 小時/週）；距 2027 年 6 月畢業約 **14 個月**，時程充裕但需每月嚴格控管里程碑 |
| **研究深度調整** | 不必追求最新深度學習架構（GraphDCF、GNN）；以投資人分群為主，推薦模型採概念驗證與 baseline 比較，兼顧品質與可執行性 |
| **方法論聚焦** | 研究貢獻聚焦在「整合 GA4 行為特徵 × 交易特徵」的**特徵工程設計**，而非演算法本身的創新 |
| **Python 程度** | 可閱讀與理解程式碼、撰寫能力約 5 成 → 採用**高可讀性的 Jupyter Notebook 逐步實作**；AI 輔助撰寫代碼（如 Cursor）可大幅降低門檻 |
| **論文規模** | 在職碩班論文頁數通常 60–100 頁，毋需過度擴大範圍 |

---

## 3. 相關文獻整理

> 以下為初步文獻盤點，供論文第二章文獻探討使用。完整連結與研究缺口分析詳見 [`literature/literature-matrix.md`](literature/literature-matrix.md)。

### 3.1 投資人分群方法

| # | 論文 | 作者 | 年份 | 連結 | 關聯章節 |
|---|-----|------|------|------|----------|
| A1 | RFM-Net: A CNN for Customer Segment Classification | — | 2026 | [MDPI Applied Sciences](https://www.mdpi.com/2076-3417/16/5/2223) | Ch3 研究方法 |
| A2 | AI-Driven CLV Forecasting: Integrating RFM with ML | Akter et al. | 2025 | [ResearchGate](https://www.researchgate.net/publication/389495515_Artificial_Intelligence-Driven_Customer_Lifetime_Value_CLV_Forecasting_Integrating_RFM_Analysis_with_Machine_Learning_for_Strategic_Customer_Retention) | Ch2 文獻、Ch3 |
| A3 | Enhancing Customer Repurchase Prediction with RFM | — | 2025 | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0970389625000266) | Ch2 文獻 |
| A4 | Unlocking High-Value Football Fans: Unsupervised ML | — | 2024 | [Frontiers](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2024.1362489/full) | Ch2 文獻 |
| A5 | 以 RFM 模型結合群集分析建立顧客分群暨商品推薦之研究 | — | 2022 | [臺博碩論文](https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?o=dnclcdr&s=id=%22110THU01026098%22.&searchmode=basic) | Ch2 文獻、Ch3 |

### 3.2 個人化基金推薦系統

| # | 論文 | 作者 | 年份 | 連結 | 關聯章節 |
|---|-----|------|------|------|----------|
| B1 | Modeling Behavior Sequence for Personalized Fund Recommendation with GraphDCF | Chou, Y.-C.; Chen, C.-T.; Huang, S.-H. | 2022 | [ScienceDirect DOI 10.1016/j.eswa.2021.116311](https://www.sciencedirect.com/science/article/abs/pii/S0957417421016122) | Ch2 文獻、Ch3 |
| B2 | Personalized Fund Recommendation with Dynamic Utility Learning | Wei, J.; Liu, J. | 2025 | [Financial Innovation DOI 10.1186/s40854-024-00720-5](https://link.springer.com/article/10.1186/s40854-024-00720-5) | Ch2 文獻 |
| B3 | Mutual Fund Recommendation System with Personalized Explanations | — | 2023 | [ResearchGate](https://www.researchgate.net/publication/367530626_MUTUAL_FUND_RECOMMENDATION_SYSTEM_WITH_PERSONALIZED_EXPLANATIONS) | Ch2 文獻 |
| B4 | A Hybrid Recommendation Engine for Fintech Platforms | — | 2025 | [ResearchGate](https://www.researchgate.net/publication/394559448_A_Hybrid_Recommendation_Engine_for_Fintech_Platforms_Leveraging_Behavioral_Analytics_for_User_Engagement_and_Conversion) | Ch2 文獻 |
| B5 | FAR-Trans: An Investment Dataset for Financial Asset Recommendation | — | 2024 | [arXiv:2407.08692](https://arxiv.org/abs/2407.08692) | Ch4 實驗、附錄 |

### 3.3 FinTech 與數位券商應用

| # | 論文 | 年份 | 連結 | 關聯章節 |
|---|-----|------|------|----------|
| C1 | FinTech, Investor Sophistication, and Financial Portfolio Choices | 2023 | [Oxford RCFS](https://academic.oup.com/rcfs/article/12/4/834/7192186) | Ch1 背景、Ch2 文獻 |
| C2 | The Digital Transformation of Investment Behavior: A Systematic Review | 2024 | [ResearchGate](https://www.researchgate.net/publication/396368845_The_digital_transformation_of_investment_behavior_a_systematic_review_of_gambling_tendencies_in_modern_financial_markets) | Ch2 文獻 |
| C3 | Artificial Intelligence in Capital Markets: Use Cases, Risks (IOSCO) | 2023 | [IOSCO PDF](https://www.iosco.org/library/pubdocs/pdf/IOSCOPD788.pdf) | Ch5 限制、Ch1 背景 |

### 3.4 台灣本土相關研究（含新增）

> 完整連結與說明詳見 [`literature/literature-matrix.md`](literature/literature-matrix.md) E、F、G 類。

**原有 D 類（4 篇）**

| # | 論文 | 年份 | 連結 | 關聯章節 |
|---|-----|------|------|----------|
| D1 | 投資人可否從券商推薦的股票獲利？ | — | [臺博碩](https://ndltd.ncl.edu.tw/handle/46963616466150231805) | Ch2 文獻 |
| D2 | 台灣股票市場散戶投資人電視頻道偏好與投資行為關係之研究 | — | [臺博碩](https://ndltd.ncl.edu.tw/handle/b3agwt) | Ch2 文獻 |
| D3 | 券商推薦個股的資訊內涵之探討（徐楚雯） | 2019 | [臺科大論文庫](https://etheses.lib.ntust.edu.tw/thesis/detail/5fbb589dce8828c2ef89fe78e80010e3/) | Ch2 文獻 |
| D4 | 網路關鍵字搜尋行為反映投資人情緒之研究 | 2023 | [Airiti Library](https://www.airitilibrary.com/Article/Detail/U0002-1107202310513600) | Ch2 文獻 |

**新增 E 類：台灣推薦系統與顧客分群（4 篇）**

| # | 論文 | 年份 | 連結 | 關聯章節 |
|---|-----|------|------|----------|
| E1 | 個人化推薦系統、顧客購買意願與後續退貨行為之影響 | 2022 | [臺博碩](https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?o=dnclcdr&s=id=%22110TKU05121038%22.&searchmode=basic) | Ch2 文獻 |
| E2 | 應用 RFM 模型制定顧客分群行銷策略之研究 | 2020 | [臺博碩](https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?o=dnclcdr&s=id=%22109NTUS5121030%22.&searchmode=basic) | Ch2 文獻、Ch3 ⭐ |
| E3 | 基於用戶序列之協同過濾推薦 | — | [臺博碩](https://ndltd.ncl.edu.tw/handle/3pake6) | Ch2 文獻 |
| E4 | 資料探勘分析於金融機構客戶關係經營之研究 | — | [台科大論文庫](https://etheses.lib.ntust.edu.tw/detail/5f04fdb7c1c54021a137ad835327d677/) | Ch2 文獻 |

**新增 F 類：台灣機器人理財與數位投資行為（3 篇）**

| # | 論文 | 作者 | 年份 | 連結 | 關聯章節 |
|---|-----|------|------|------|----------|
| F1 | 台灣投資人對於機器人理財行為意圖之研究 | 陳奕君 | 2020 | [Airiti Library](https://www.airitilibrary.com/Article/Detail/U0004-G0107351022) | Ch1 背景、Ch2 文獻 |
| F2 | 提升投資人使用機器人理財意願之研究 | — | — | [臺博碩](http://ndltd.ncl.edu.tw/handle/dqk4c3) | Ch1 背景、Ch2 文獻 |
| F3 | 機器人理財服務是否可有效消除投資人行為偏誤 | — | 2019 | [臺博碩](https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?o=dnclcdr&s=id=%22108NTPU0121042%22.&searchmode=basic) | Ch2 文獻 |

**新增 G 類：台灣共同基金投資人行為（4 篇）**

| # | 論文 | 作者 | 年份 | 連結 | 關聯章節 |
|---|-----|------|------|------|----------|
| G1 | 共同基金投資人投資行為及風險偏好之研究 | — | 2009 | [臺博碩](https://ndltd.ncl.edu.tw/handle/7msk6p) | Ch2 文獻 ⭐ |
| G2 | 台灣地區共同基金投資行為實證研究 | 鄭芳盈 | 2007 | [Airiti Library](https://www.airitilibrary.com/Article/Detail?DocID=U0006-0908200717040800) | Ch2 文獻 |
| G3 | 基金投資人是否存在現狀偏誤：來自台灣之證據 | — | — | [臺博碩](https://ndltd.ncl.edu.tw/handle/bx5udf) | Ch2 文獻 |
| G4 | 市場狀態與基金投資人投資行為之探討 | — | — | [臺博碩](https://ndltd.ncl.edu.tw/r/42769455951077663518) | Ch2 文獻 |

### 3.5 研究缺口分析（論文貢獻定位）

```
現有研究多採用：
  ✅ 單一數據來源（僅交易 or 僅行為）
  ✅ 通用商品推薦（非基金專屬）
  ✅ 中國或全球數據集

本研究的創新貢獻：
  🆕 整合 GA4 使用者行為事件 + 基金交易記錄（雙軌數據）
  🆕 聚焦台灣數位券商場景（在地化）
  🆕 行為特徵工程作為推薦模型輸入（非純交易記錄）
  🆕 比較個人化推薦 vs. 熱門基金推薦之效果差異
```

---

## 4. 資料來源需求分析

### 4.1 核心資料集（必須）

| 資料集 | 來源 | 主要欄位 | 時間範圍建議 | 取得難度 |
|--------|------|----------|-------------|---------|
| **GA4 使用者行為資料** | GA4 → BigQuery 匯出 | user_pseudo_id、event_name、page_location、session_id、事件參數 | 最近 12–18 個月 | ⭐ 低（你有 GA4 存取權） |
| **基金交易記錄** | 好好證券後台 / 資料倉儲 | user_id、fund_code、buy/sell、amount、date | 最近 12–18 個月 | ⭐⭐ 中（需公司授權） |
| **用戶屬性資料** | KYC 系統（匿名化） | 風險等級（KYC Risk Score）、開戶年齡區間、是否首次投資 | 同期 | ⭐⭐ 中（需匿名化） |

### 4.2 輔助資料集（加分，非必須）

| 資料集 | 來源 | 用途 | 備注 |
|--------|------|------|------|
| **行銷觸點資料** | Email / Push 系統 | 分析行銷曝光對行為分群的影響 | 可納入為輔助變數 |
| **基金基本資訊** | 基金公司資料 / 公開資料 | 基金類別標籤（股票型/債券型/平衡型）、風險等級 | 通常可公開取得 |
| **市場行情資料** | Yahoo Finance / 公開 API | 對照研究時間段的市場環境 | 公開資料，可直接取得 |

### 4.3 特徵工程規劃（初稿）

#### 行為特徵（來自 GA4）

```python
# 每位用戶聚合的 GA4 行為特徵
behavioral_features = {
    "session_count": "30天內 session 總數",
    "fund_page_views": "基金頁面瀏覽次數",
    "fund_detail_views": "個別基金詳情頁瀏覽次數",
    "search_count": "站內搜尋次數",
    "avg_session_duration": "平均 session 時長（秒）",
    "page_depth": "平均頁面深度",
    "device_type": "裝置類型（mobile/desktop）",
    "visit_frequency": "訪問天數 / 30",
    "last_visit_days": "距上次訪問天數（Recency）",
}
```

#### 交易特徵（來自交易資料）

```python
# 每位用戶聚合的交易行為特徵（投資版 RFM）
transaction_features = {
    "recency": "距上次交易天數",
    "frequency": "交易次數",
    "monetary": "累計交易金額",
    "fund_diversity": "購買不同基金類型數",
    "avg_holding_period": "平均持有天數",
    "buy_sell_ratio": "買入/賣出比率",
    "risk_level_avg": "持有基金加權平均風險等級",
}
```

### 4.4 資料倫理清單

```
□ 取得公司書面授權（學術研究用途）
□ 所有 user_id 替換為研究用匿名編號
□ 不保留、不公開任何可識別個人的欄位
□ 確認符合個人資料保護法相關規定
□ 與指導教授討論是否需申請 IRB 倫理審查
```

---

## 5. 研究時程規劃（在職學生版）

> 今日：2026 年 4 月 14 日 | 目標口試：2027 年 4–5 月 | 目標畢業：2027 年 6 月
> 每週可投入 10–15 小時；**總研究周期約 14 個月**。

```
2026 Apr-Jun  ▌ 文獻整理 + 研究計畫書 + 資料取得準備
2026 Jul-Aug  ▌ 資料清理 + 特徵工程 + EDA
2026 Sep-Oct  ▌ 投資人行為分群模型
2026 Nov-Dec  ▌ 個人化推薦模型
2027 Jan      ▌ 模型評估與比較分析
2027 Feb-Mar  ▌ 論文撰寫（第 1–5 章）
2027 Apr      ▌ 論文修改 + 預口試（Pre-defense）
2027 May-Jun  ▌ 正式口試 + 送審 🎓
```

### 詳細里程碑

| 月份 | 階段 | 主要產出 | 里程碑 |
|------|------|----------|--------|
| 2026 Apr–May | 文獻整理 | 文獻清單 30+ 篇、文獻矩陣 | 與老師確認研究問題與架構 |
| 2026 Jun | 研究設計 | 研究架構圖、變數定義表、Proposal 初稿 | 研究計畫書提交老師審閱 |
| 2026 Jul | 資料準備 | 公司授權文件、IRB（如需）、資料字典、GA4 × 交易 join 驗證 | 取得可用研究資料集 |
| 2026 Aug | 資料前處理 | 清洗後特徵資料、缺值與異常值處理 | EDA 報告完成 |
| 2026 Sep | 分群模型 v1 | K-means / K-prototypes 初版分群結果 | Silhouette Score 確認最佳群數 |
| 2026 Oct | 分群模型 v2 | 各群行為特徵解讀、群體命名與商業詮釋 | 老師確認分群結果合理 |
| 2026 Nov | 推薦模型 v1 | Baseline（熱門推薦）+ User-Based CF 初版 | Precision@K 初步結果 |
| 2026 Dec | 推薦模型 v2 | Item-Based CF 或 Matrix Factorization（SVD） | Recall@K / MAP 評估完成 |
| 2027 Jan | 模型評估 | 個人化推薦 vs. 熱門推薦比較報告 | 模型優於 Baseline 確認 |
| 2027 Feb–Mar | 論文撰寫 | 各章節初稿（Ch1–Ch5） | 指導教授 Review 完成 |
| 2027 Apr | 修改 + 預口試 | 修改後論文 + 口試簡報 | Pre-defense 通過 |
| 2027 May–Jun | 正式口試 | 最終論文繳交 | 🎓 口試通過、畢業 |

---

## 6. 技術選型建議

### 6.1 建議技術棧

| 類別 | 工具 / 套件 | 理由 |
|------|-------------|------|
| 語言 | Python 3.11+ | 數據分析主流，sklearn 生態完整 |
| 資料處理 | pandas, numpy | 基本配備 |
| 分群模型 | scikit-learn (K-means), kmodes (K-prototypes) | 含類別變數時用 K-prototypes |
| 推薦模型 | scikit-surprise (CF), implicit (ALS) | 協同過濾主流套件 |
| 視覺化 | matplotlib, seaborn, plotly | EDA 與結果呈現 |
| 評估 | sklearn.metrics, recmetrics | Precision@K, Recall@K, MAP |
| 環境 | Jupyter Notebook + GitHub | 版本控管與重現性 |
| AI 輔助 | Cursor（本工具） | Python 程式碼撰寫輔助，降低 5 成語法門檻 |
| 報告 | Markdown + LaTeX（如需） | 論文繳交格式 |

### 6.2 針對 Python 5 成程度的學習策略

> 你可以閱讀理解程式碼，撰寫能力約 5 成。建議採用「閱讀範本 → 修改調整 → AI 輔助補全」的學習路徑。

**學習優先順序（建議 2026 Apr–Jun 同步推進）：**

1. **pandas 資料清理**（最高優先）：`groupby`、`merge`、`pivot_table`、缺值處理
2. **scikit-learn K-means**（第二優先）：`KMeans`、`silhouette_score`、`StandardScaler`
3. **matplotlib / seaborn 視覺化**（第三優先）：分群結果圖、特徵分布圖
4. **scikit-surprise 協同過濾**（第四優先，推薦模型階段再學）

**建議資源：**
- Kaggle Learn（免費）：pandas、ML 入門課程（各約 4–6 小時）
- scikit-learn 官方教學：Clustering 章節有完整範例可直接改用

### 6.3 模型選型策略（務實優先）

```
複雜度由低到高 → 建議從左到右逐步嘗試：

分群：
K-means ──→ K-prototypes ──→ Hierarchical Clustering
 (連續特徵)   (混合特徵)        (探索分群數量)

推薦：
熱門推薦(Baseline) ──→ User-Based CF ──→ Item-Based CF ──→ Matrix Factorization (SVD)
   （比較基準）           （協同過濾）        （物品協同）         （矩陣分解）
```

> 學術論文不必用最複雜的模型；關鍵在於**清楚說明比較邏輯**與**結果解讀**。

---

## 7. 研究風險與因應策略

| 風險等級 | 風險項目 | 影響 | 因應策略 |
|---------|---------|------|----------|
| 🔴 高 | **公司不允許使用真實數據** | 整個研究核心受影響 | 事先取得書面授權；若不允許，改用公開數據集（如 FAR-Trans）或模擬數據作為替代 |
| 🔴 高 | **GA4 User ID 無法與交易 ID 串接** | 雙軌整合特徵無法建立 | 確認 GA4 是否有綁定內部 user_id；若未綁定需提前在系統層補充 |
| 🟡 中 | **資料量不足（冷啟動問題）** | 推薦模型效果差 | 使用 Content-Based Filtering 作為冷啟動補救策略 |
| 🟡 中 | **在職學生時間不足** | 研究延遲 | 每月與老師至少面談 1 次；每月設定明確里程碑 |
| 🟡 中 | **研究範圍過廣** | 論文散焦 | 聚焦基金（不含股票/ETF）；投資人限「曾有交易記錄的用戶」 |
| 🟢 低 | **模型無法優於 Baseline** | 無法驗證研究假設 | 先確認 Baseline 設定合理（熱門推薦）；若效果相近，分析原因也是貢獻 |
| 🟢 低 | **法規/倫理問題延誤進度** | 時程推遲 | 在 M1-M2 提前處理，列入研究計畫書中說明 |

---

## 8. 待討論事項（需與老師確認）

> ⚠️ 以下問題建議在與王亦凡老師第一次正式會議前確認，部分可能影響研究設計。

### Q1：資料取得 — ✅ 已確認

公司同意提供匿名化數據用於學術研究，且 GA4 已發送 user_id 可與交易記錄串接。

**剩餘行動項目**：
- [ ] 請公司出具書面授權文件（一頁即可，說明：研究用途、不公開原始數據、研究者姓名）
- [ ] 確認資料脫敏範疇：哪些欄位需去除或 hash（例如：電話、姓名、email）

### Q2：預計畢業時程 — ✅ 已確認：2027 年 6 月

時程已依此更新，詳見第 5 章。

### Q3：Python / 資料分析技術準備度 — ✅ 已確認：可閱讀，撰寫約 5 成

技術策略已調整：採用「閱讀範本 → 修改調整 → AI 輔助補全」路徑，詳見第 6 章。

### Q4：研究範圍邊界 — 🟡 待確認

**問題**：「基金」是否涵蓋所有類型（股票型、債券型、平衡型、ETF）？「投資人」是否只含曾交易用戶還是包含瀏覽未購買用戶？

- 建議：聚焦有交易記錄的用戶（降低冷啟動複雜度）；基金先以主要三類為主

### Q5：學術貢獻定位 — 🟡 建議確認

**建議定位**：**場景應用型研究**（Application Research）
- 貢獻在於「在地化數位券商場景的完整實作流程」與「GA4 × 交易雙軌特徵工程設計」
- 毋需提出全新演算法架構，在職碩班學術標準是符合的

---

## 9. 下一步行動

### 立即行動（2026 年 4 月，本月內）

```
□ 請公司出具書面授權文件（學術研究資料使用同意書）
□ 確認資料脫敏方案：哪些欄位需去除（電話、姓名、email → hash 或移除）
□ 預約與王亦凡老師的第一次正式指導會議，確認：
    - 研究範圍邊界（基金類型、投資人定義）
    - 是否需申請 IRB 倫理審查
    - 研究計畫書格式要求與繳交時間
□ 閱讀文獻 #6（GraphDCF, 2022）與 #9（Hybrid Recommendation Engine, 2025）
□ 確認 GA4 BigQuery 匯出設定，試跑一次資料取出流程
```

### 短期行動（2026 年 5–6 月）

```
□ 完成文獻清單 30 篇（優先搜尋台灣博碩士論文系統：ndltd.ncl.edu.tw）
□ 建立 literature-matrix.md（各篇文獻的研究方法 × 結論 × 缺口整理）
□ 完成研究計畫書（Proposal）初稿送老師審閱
□ Python 學習：完成 Kaggle Learn pandas 課程（約 4 小時）
□ 準備匿名化資料集：GA4 × 交易 join 驗證，確認 user_id 串接正確性
```

### 本專案資料夾結構規劃

```
side-projects/thesis-investor-segmentation/
├── thesis-research-plan.md       ← 本文件（研究規劃）
├── literature/
│   ├── literature-matrix.md      ← 文獻矩陣（尚待建立）
│   └── notes/                    ← 各篇文獻閱讀筆記
├── data/
│   ├── raw/                      ← 原始匿名化數據（不上 Git）
│   └── processed/                ← 清洗後特徵數據
├── notebooks/
│   ├── 01-eda.ipynb              ← 探索性資料分析
│   ├── 02-clustering.ipynb       ← 分群模型
│   └── 03-recommendation.ipynb   ← 推薦模型
├── scripts/
│   ├── feature_engineering.py    ← 特徵工程腳本
│   └── evaluation.py             ← 評估指標計算
└── thesis/
    └── chapters/                 ← 各章節草稿
```

---

*最後更新：2026-04-14（已納入確認事項：公司授權 ✅、GA4 串接 ✅、畢業時程 2027/06 ✅）| 狀態：規劃確認中*
