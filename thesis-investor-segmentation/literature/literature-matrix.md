# 整合版文獻矩陣

論文：應用投資人行為分群與個人化推薦模型於數位券商基金投資服務之研究

最後更新：2026-07-22  
整合來源：

1. `literature/literature-matrix.md` 原始 A–G 文獻矩陣
2. `literature/phase1/phase1-literature-matrix-2026-06-22.md` Phase 1 補強文獻矩陣

> **使用定位：** 本檔為目前 Phase 1 的主要文獻總表。已將原始 A–G 文獻與 Phase 1 補強文獻整併、初步去重並重新分類。仍需後續人工查證部分作者、年份、來源品質與正式 APA / 作者年份格式。

---

## 整併摘要

| 項目 | 說明 |
|---|---|
| 主要用途 | Phase 1 文獻盤點、核心文獻閱讀順序、第二章文獻探討素材 |
| 整併方式 | 保留原 A–G 分類邏輯，將補強文獻併入相近分類 |
| 已初步去重 | GraphDCF、Dynamic Utility Learning、RFM + K-means、Robo-advisor、IOSCO 等重複或相近文獻已合併或標記 |
| 尚待處理 | 待查證來源、正式引用格式、作者年份缺漏、ResearchGate / NDLTD / Airiti 來源品質確認 |
| 閱讀優先 | 先讀「高」優先級文獻；中、低優先級作為背景或補充 |

---

## 目錄

1. [A 類：投資人分群、RFM 與機器學習分群方法](#a-類投資人分群rfm-與機器學習分群方法)
2. [B 類：基金與金融商品推薦系統](#b-類基金與金融商品推薦系統)
3. [C 類：FinTech、數位券商、GA4 與 AI 治理](#c-類fintech數位券商ga4-與-ai-治理)
4. [D 類：台灣本土券商與投資人行為研究](#d-類台灣本土券商與投資人行為研究)
5. [E 類：台灣推薦系統、RFM 與金融 CRM 研究](#e-類台灣推薦系統rfm-與金融-crm-研究)
6. [F 類：Robo-advisor、投資人輪廓、信任與透明度](#f-類robo-advisor投資人輪廓信任與透明度)
7. [G 類：台灣共同基金投資人行為與風險偏好](#g-類台灣共同基金投資人行為與風險偏好)
8. [重複與整併對照](#重複與整併對照)
9. [建議核心閱讀順序](#建議核心閱讀順序)
10. [研究缺口對應](#研究缺口對應)
11. [待查證與待補文獻](#待查證與待補文獻)

---

## A 類：投資人分群、RFM 與機器學習分群方法

| # | 論文標題 | 作者 | 年份 | 來源 | 核心方法 / 內容 | 本研究關聯 | 優先級 | 連結 |
|---|---|---|---:|---|---|---|---|---|
| A1 | RFM-Net: A Convolutional Neural Network for Customer Segment Classification | — | 2026 | Applied Sciences / MDPI | CNN + RFM 特徵分類；準確率 94.33% | 分群方法比較基準；RFM 特徵設計參考 | 中 | https://www.mdpi.com/2076-3417/16/5/2223 |
| A2 | Artificial Intelligence-Driven CLV Forecasting: Integrating RFM Analysis with ML for Strategic Customer Retention | Akter et al. | 2025 | JCSTS / ResearchGate | K-means++、XGBoost、AHP 加權 RFM、動態 CLV | 特徵加權與 K-means++ 應用參考 | 中 | https://www.researchgate.net/publication/389495515_Artificial_Intelligence-Driven_Customer_Lifetime_Value_CLV_Forecasting_Integrating_RFM_Analysis_with_Machine_Learning_for_Strategic_Customer_Retention |
| A3 | Enhancing Customer Repurchase Prediction: Integrating Classification Algorithms with RFM Analysis for Precision and Actionable Insights | — | 2025 | ScienceDirect | RFM + 分類演算法、10-fold 交叉驗證 | 模型評估與驗證方法參考 | 低 | https://www.sciencedirect.com/science/article/pii/S0970389625000266 |
| A4 | Unlocking High-Value Football Fans: Unsupervised ML for Customer Segmentation and Lifetime Value | — | 2024 | Frontiers in Sports and Active Living | AHP 加權 RFM + K-means，識別 8 個群體 | 無監督分群流程與群體命名參考 | 中 | https://doi.org/10.3389/fspor.2024.1362489 |
| A5 | 以 RFM 模型結合群集分析建立顧客分群暨商品推薦之研究 | — | 2022 | 東海大學碩士論文 | RFM + 群集分析 + 商品推薦流程 | 台灣碩士論文範本；研究設計與章節結構可對照 | 高 | https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?o=dnclcdr&s=id=%22110THU01026098%22.&searchmode=basic |
| A6 | Profiling investor behavior in the Malaysian derivatives market using K-means clustering | Tan et al. | 2025 | Frontiers in Artificial Intelligence | K-means、IHS transformation、decision tree validation；1,100 萬筆交易資料 | 金融交易行為分群方法參考；雖非基金但場景接近 | 高 | https://doi.org/10.3389/frai.2025.1640776 |
| A7 | RFM ranking – An effective approach to customer segmentation | Christy et al. | 2021 | Journal of King Saud University - Computer and Information Sciences | RFM、K-means、Fuzzy C-Means | 支撐本研究交易 RFM / 行為 RFM 特徵工程 | 高 | https://doi.org/10.1016/j.jksuci.2018.09.004 |
| A8 | RFM model for customer purchase behavior using K-Means algorithm | Anitha; Patil R. P.（待查證） | 2021 | Journal of King Saud University - Computer and Information Sciences | RFM、K-means、Silhouette Coefficient | 補強分群品質評估指標設計 | 中 | https://www.sciencedirect.com/science/article/pii/S1319157819309802 |
| A9 | Tracking Customer Segments in Alternative Finance using time-evolving Cluster Analysis | Lennert Aerts | 2020 | Erasmus University Rotterdam Master Thesis | K-means、K-prototypes、GMM、DBSCAN、cluster tracking | 若後續做分群穩定性或混合型資料，可作方法參考 | 中 | https://thesis.eur.nl/pub/52256/Aerts.pdf |
| A10 | Intuitive-K-prototypes: A mixed data clustering algorithm with improved prototype representation and attribute weights | 作者待補 | 2024 | Pattern Recognition / Elsevier | K-prototypes、混合型資料分群、attribute weighting | 若同時使用數值與類別特徵，支撐 K-prototypes 合理性 | 中 | https://www.sciencedirect.com/science/article/pii/S0031320324008136 |
| A11 | Using RFM, AUM, and K-means clustering for customer segmentation | Uchechukwu Emmanuel / Cowrywise | 2025 | Metabase Community / Cowrywise 產業案例 | RFM + AUM + K-means | FinTech / 財富管理平台分群實務案例；適合作背景，不宜作核心學術引用 | 低 | https://www.metabase.com/community-posts/using-rfm-aum-and-k-means-clustering-customers-segmentation |

---

## B 類：基金與金融商品推薦系統

| # | 論文標題 | 作者 | 年份 | 來源 | 核心方法 / 內容 | 本研究關聯 | 優先級 | 連結 |
|---|---|---|---:|---|---|---|---|---|
| B1 | Modeling Behavior Sequence for Personalized Fund Recommendation with Graphical Deep Collaborative Filtering | Chou, Chen & Huang | 2021/2022 | Expert Systems with Applications | GraphDCF；基金交易序列與圖式協同過濾 | 最核心基金推薦文獻；支撐推薦模型與交易序列設計 | 高 | https://doi.org/10.1016/j.eswa.2021.116311 |
| B2 | Personalized Fund Recommendation with Dynamic Utility Learning | Wei & Liu | 2025 | Financial Innovation | Incremental utility learning、點擊序列、探索 / 利用 | 連接數位行為資料與基金推薦；與 GA4 行為資料高度相關 | 高 | https://doi.org/10.1186/s40854-024-00720-5 |
| B3 | Mutual Fund Recommendation System with Personalized Explanations | — | 2023 | ResearchGate | 知識圖譜、ML、可解釋推薦 | 支撐金融推薦可解釋性；需查證來源品質 | 中 | https://www.researchgate.net/publication/367530626_MUTUAL_FUND_RECOMMENDATION_SYSTEM_WITH_PERSONALIZED_EXPLANATIONS |
| B4 | A Hybrid Recommendation Engine for Fintech Platforms: Leveraging Behavioral Analytics for User Engagement and Conversion | — | 2025 | ResearchGate | 混合推薦、CF、Content-based、Deep Learning、行為分析 | 可作 FinTech 混合推薦架構參考；需查證來源品質 | 中 | https://www.researchgate.net/publication/394559448_A_Hybrid_Recommendation_Engine_for_Fintech_Platforms_Leveraging_Behavioral_Analytics_for_User_Engagement_and_Conversion |
| B5 | FAR-Trans: An Investment Dataset for Financial Asset Recommendation | — | 2024 | arXiv | 金融資產推薦資料集、資產定價與散戶交易紀錄 | 可作外部資料集與推薦評估基準背景 | 中 | https://arxiv.org/abs/2407.08692 |
| B6 | Explainable mutual fund recommendation system developed based on knowledge graph embeddings | Hsu, Chen, Chou & Huang | 2022 | Applied Intelligence / Springer | Knowledge Graph Embedding、可解釋共同基金推薦 | 補強信任與可解釋性；可與 B1 形成台灣基金推薦文獻群 | 高 | https://doi.org/10.1007/s10489-021-03136-1 |
| B7 | A Systematic Literature Review of Financial Product Recommendation Systems | Wu & Li | 2025 | Information / MDPI | 系統性文獻回顧；金融商品推薦特殊性 | 第二章推薦系統總覽與研究缺口核心來源 | 高 | https://doi.org/10.3390/info16030196 |
| B8 | Research on Personalized Financial Product Recommendation by Integrating Large Language Models and Graph Neural Networks | Zhao et al. | 2025 | arXiv / ACM ICSECA | LLM embeddings + heterogeneous graph + GNN | 最新技術趨勢；可用來說明本研究不採 LLM/GNN 的邊界 | 中 | https://arxiv.org/abs/2506.05873 |
| B9 | A survey on recommendation systems for financial services | Sharaf et al. | 2022 | Multimedia Tools and Applications（待查證） | 金融服務推薦綜述 | 推薦系統背景文獻；需補 DOI / 全文後再正式引用 | 中 | 待查證 |

---

## C 類：FinTech、數位券商、GA4 與 AI 治理

| # | 論文 / 報告標題 | 作者 / 機構 | 年份 | 來源 | 核心內容 | 本研究關聯 | 優先級 | 連結 |
|---|---|---|---:|---|---|---|---|---|
| C1 | FinTech, Investor Sophistication, and Financial Portfolio Choices | — | 2023 | Review of Corporate Finance Studies / Oxford | FinTech 平台影響投資人成熟度與投資組合選擇 | Ch1 背景；數位券商對投資行為影響 | 高 | https://academic.oup.com/rcfs/article/12/4/834/7192186 |
| C2 | The Digital Transformation of Investment Behavior: A Systematic Review of Gambling Tendencies in Modern Financial Markets | — | 2024 | ResearchGate | 數位化投資行為、行為偏誤系統性回顧 | 支撐數位平台與投資人行為改變；需查證來源品質 | 中 | https://www.researchgate.net/publication/396368845_The_digital_transformation_of_investment_behavior_a_systematic_review_of_gambling_tendencies_in_modern_financial_markets |
| C3 | Artificial Intelligence in Capital Markets: Use Cases, Risks, and Challenges | IOSCO | 2023 | IOSCO 官方報告 | AI 在資本市場應用、風險與監理挑戰 | Ch1 背景、Ch5 限制與監理討論 | 高 | https://www.iosco.org/library/pubdocs/pdf/IOSCOPD788.pdf |
| C4 | The use of artificial intelligence and machine learning by market intermediaries and asset managers | IOSCO Board | 2021 | IOSCO Final Report | AI/ML 治理、測試、監控、揭露、資料品質與偏誤 | 金融推薦模型治理、資料品質與可解釋性權威來源 | 高 | https://www.iosco.org/library/pubdocs/pdf/IOSCOPD684.pdf |
| C5 | Enhancing Investors’ Trust: 2022 CFA Institute Investor Trust Study | CFA Institute | 2022 | CFA Institute | 投資人信任、科技、個人化、people plus technology | 支撐數位券商為何需要個人化服務與信任設計 | 高 | https://www.cfainstitute.org/sites/default/files/-/media/documents/article/Enhancing-Investors-Trust-Report_2022_Online.pdf |
| C6 | [GA4] Cohort exploration | Google Analytics Help | 2024–2026 | Google 官方文件 | GA4 cohort、event、transaction、conversion、User-ID 限制 | 第三章 GA4 行為資料處理與限制 | 高 | https://support.google.com/analytics/answer/9670133?hl=en |
| C7 | Segments in Google Analytics 4 / GA4 segment types | Google Analytics Help / GA4 教學來源 | 2024–2026 | Google / GA4 文件 | User / session / event segment scope | 支撐 GA4 使用者層、session 層、事件層特徵工程設計 | 中 | https://support.google.com/analytics/answer/9304353 |
| C8 | A Preliminary Study of Fintech Industry: A Two-Stage Clustering Analysis for Customer Segmentation in the B2B Setting | Sheikh, Ghanbarpour & Gholamiangonabadi | 2019 | Journal of Business-to-Business Marketing | FinTech 客戶分群、two-stage clustering | FinTech 分群方法背景；B2B 與本研究差異較大 | 低 | https://doi.org/10.1080/1051712X.2019.1603420 |

---

## D 類：台灣本土券商與投資人行為研究

| # | 論文標題 | 作者 | 年份 | 來源 | 核心內容 | 本研究關聯 | 優先級 | 連結 |
|---|---|---|---:|---|---|---|---|---|
| D1 | 投資人可否從券商推薦的股票獲利？ | — | — | 臺博碩 | 台灣股市散戶是否能從券商推薦中獲利 | 台灣券商推薦效果研究脈絡 | 中 | https://ndltd.ncl.edu.tw/handle/46963616466150231805 |
| D2 | 台灣股票市場散戶投資人電視頻道偏好與投資行為關係之研究 | — | — | 臺博碩 | 媒體偏好、投資性格與行為偏誤 | 投資人行為分群變數設計參考 | 中 | https://ndltd.ncl.edu.tw/handle/b3agwt |
| D3 | 券商推薦個股的資訊內涵之探討 | 徐楚雯 | 2019 | 國立臺灣科技大學碩士論文 | 券商推薦對股價影響與資訊內涵 | 推薦資訊內涵與台灣券商脈絡 | 中 | https://etheses.lib.ntust.edu.tw/thesis/detail/5fbb589dce8828c2ef89fe78e80010e3/ |
| D4 | 網路關鍵字搜尋行為反映投資人情緒之研究 | — | 2023 | Airiti Library | Google 搜尋趨勢與投資人情緒 | 支撐數位搜尋 / 行為資料可作投資人意圖代理變數 | 中 | https://www.airitilibrary.com/Article/Detail/U0002-1107202310513600 |

---

## E 類：台灣推薦系統、RFM 與金融 CRM 研究

| # | 論文標題 | 作者 | 年份 | 來源 | 核心方法 / 內容 | 本研究關聯 | 優先級 | 連結 |
|---|---|---|---:|---|---|---|---|---|
| E1 | 個人化推薦系統、顧客購買意願與後續退貨行為之影響 | — | 2022 | 淡江大學碩士論文 / 臺博碩 | 電商個人化推薦與購買意願 | 台灣推薦系統對使用者行為影響背景 | 中 | https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?o=dnclcdr&s=id=%22110TKU05121038%22.&searchmode=basic |
| E2 | 應用 RFM 模型制定顧客分群行銷策略之研究——以 A 保健食品公司為例 | — | 2020 | 臺灣科技大學碩士論文 / 臺博碩 | RFM 模型、顧客分群、行銷策略 | 台灣 RFM 分群行銷論文範本；方法論可對照 | 高 | https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?o=dnclcdr&s=id=%22109NTUS5121030%22.&searchmode=basic |
| E3 | 基於用戶序列之協同過濾推薦 | — | — | 臺博碩 | 使用者序列行為、協同過濾 | 台灣協同過濾推薦系統研究脈絡 | 中 | https://ndltd.ncl.edu.tw/handle/3pake6 |
| E4 | 資料探勘分析於金融機構客戶關係經營之研究 | — | — | 臺灣科技大學碩士論文 | Data Mining、金融機構 CRM、分群 | 金融業資料探勘與 CRM 應用支撐 | 中 | https://etheses.lib.ntust.edu.tw/detail/5f04fdb7c1c54021a137ad835327d677/ |

---

## F 類：Robo-advisor、投資人輪廓、信任與透明度

| # | 論文標題 | 作者 | 年份 | 來源 | 核心內容 | 本研究關聯 | 優先級 | 連結 |
|---|---|---|---:|---|---|---|---|---|
| F1 | 台灣投資人對於機器人理財行為意圖之研究 | 陳奕君 | 2020 | 政治大學碩士論文 / Airiti | 台灣投資人對 robo-advisor 的採用意圖 | 台灣數位理財接受度背景 | 中 | https://www.airitilibrary.com/Article/Detail/U0004-G0107351022 |
| F2 | 提升投資人使用機器人理財意願之研究 | — | — | 臺博碩 | 機器人理財、科技接受模型、投資新手 | 台灣數位理財服務採用障礙 | 中 | http://ndltd.ncl.edu.tw/handle/dqk4c3 |
| F3 | 機器人理財服務是否可有效消除投資人行為偏誤 | — | 2019 | 臺北大學碩士論文 / 臺博碩 | Robo-advisor 與行為偏誤 | 數位化服務對投資行為偏誤的影響 | 中 | https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?o=dnclcdr&s=id=%22108NTPU0121042%22.&searchmode=basic |
| F4 | Robo Advising and Investor Profiling | Gaspar & Oliveira | 2024 | FinTech / MDPI | 投資人風險輪廓、RRA、Mean-Variance | 支撐投資人 profiling 與風險屬性適配 | 高 | https://doi.org/10.3390/fintech3010007 |
| F5 | Robo-advisors: A systematic literature review | Cardillo & Chiappini | 2024 | Finance Research Letters | Robo-advisor 系統性文獻回顧 | 數位投資服務與 robo-advisor 背景總覽 | 高 | https://doi.org/10.1016/j.frl.2024.105119 |
| F6 | Business Model of Sustainable Robo-Advisors: Empirical Insights for Practical Implementation | Au et al. | 2021 | Sustainability / MDPI | 永續 robo-advisor 採用意願 | 可作 ESG / 價值觀偏好與個人化背景 | 低 | https://doi.org/10.3390/su132313009 |
| F7 | Robo-advisors and the financialization of lay investors | Tan | 2020 | Geoforum | 演算法透明度、一般投資人、金融教育 | 支撐金融推薦需考量透明度、理解與信任 | 中 | https://doi.org/10.1016/j.geoforum.2020.09.017 |

---

## G 類：台灣共同基金投資人行為與風險偏好

| # | 論文標題 | 作者 | 年份 | 來源 | 核心內容 | 本研究關聯 | 優先級 | 連結 |
|---|---|---|---:|---|---|---|---|---|
| G1 | 共同基金投資人投資行為及風險偏好之研究 | — | 2009 | 臺博碩 / Airiti | 依風險程度將投資人分為保守、穩健、積極 | 台灣基金投資人風險分群參考；KYC 風險等級支撐 | 高 | https://ndltd.ncl.edu.tw/handle/7msk6p |
| G2 | 台灣地區共同基金投資行為實證研究 | 鄭芳盈 | 2007 | Airiti Library | BPN + CART；依性別、教育、風險偏好分類 | 台灣基金投資人行為分類早期實證 | 中 | https://www.airitilibrary.com/Article/Detail?DocID=U0006-0908200717040800 |
| G3 | 基金投資人是否存在現狀偏誤：來自台灣之證據 | — | — | 臺博碩 | 台灣基金投資人現狀偏誤 | 解釋分群結果中可能的非理性行為 | 中 | https://ndltd.ncl.edu.tw/handle/bx5udf |
| G4 | 市場狀態與基金投資人投資行為之探討 | — | — | 臺博碩 | 不同市場狀態下基金申購 / 贖回行為 | 外部市場環境對投資行為影響；可放研究限制 | 中 | https://ndltd.ncl.edu.tw/r/42769455951077663518 |

---

## 重複與整併對照

| 補強矩陣編號 | 處理方式 | 對應整合後編號 | 說明 |
|---:|---|---|---|
| 1 | 合併 | B1 | 與原 B1 GraphDCF 重複，保留更完整資訊 |
| 2 | 新增 | B6 | 可解釋共同基金推薦，原矩陣未完整收錄 |
| 3 | 合併 | B2 | 與原 B2 Dynamic Utility Learning 重複，保留更完整資訊 |
| 4 | 新增 | B7 | 金融商品推薦 SLR，建議列為核心文獻 |
| 5 | 新增 | B8 | 最新 LLM/GNN 趨勢，作研究邊界與未來研究 |
| 6 | 新增但待查證 | B9 | 金融服務推薦綜述，需補 DOI / 全文 |
| 7 | 新增 | A6 | 金融交易投資人 K-means 分群 |
| 8 | 暫未列核心 | — | Digital investors / crowdfunding，可後續視需要補入背景文獻 |
| 9 | 新增 | C8 | FinTech B2B 分群，僅作低優先背景 |
| 10 | 新增 | A7 | RFM + K-means 基礎文獻 |
| 11 | 新增但待查證 | A8 | RFM + K-means + Silhouette，需查證作者書目 |
| 12 | 新增 | A9 | K-prototypes / 動態分群方法參考 |
| 13 | 新增但待查證 | A10 | K-prototypes 改良方法，需補作者 |
| 14 | 新增 | F4 | Investor profiling / robo-advisor |
| 15 | 新增 | F5 | Robo-advisor SLR |
| 16 | 新增 | F6 | 永續 robo-advisor 採用意願 |
| 17 | 新增 | F7 | Robo-advisor 透明度與一般投資人 |
| 18 | 新增 | C4 | IOSCO 2021 AI/ML 治理報告，與 C3 互補 |
| 19 | 新增 | C5 | CFA 投資人信任報告 |
| 20 | 新增 | C6 | GA4 Cohort 官方文件 |
| 21 | 新增 | C7 | GA4 segment scope 文件 |
| 22 | 新增 | A11 | FinTech RFM / AUM 實務案例，低優先 |

---

## 建議核心閱讀順序

### 第一優先：先讀 5 篇，建立論文骨架

| 順序 | 編號 | 文獻 | 閱讀目的 |
|---:|---|---|---|
| 1 | A5 | 以 RFM 模型結合群集分析建立顧客分群暨商品推薦之研究 | 看台灣碩論如何設計 RFM、分群與推薦流程 |
| 2 | E2 | 應用 RFM 模型制定顧客分群行銷策略之研究 | 看台灣 RFM 分群與策略轉換寫法 |
| 3 | B1 | GraphDCF 基金推薦 | 看基金推薦如何使用交易序列與評估模型 |
| 4 | G1 | 共同基金投資人投資行為及風險偏好之研究 | 補台灣基金投資人風險分群脈絡 |
| 5 | B7 | Financial Product Recommendation Systems SLR | 建立金融商品推薦文獻總覽與研究缺口 |

### 第二優先：補方法與研究設計

| 編號 | 文獻 | 閱讀目的 |
|---|---|---|
| A7 | RFM ranking | 支撐 RFM + K-means 方法 |
| A6 | Malaysian derivatives K-means clustering | 支撐金融交易行為分群與分群解釋 |
| B2 | Dynamic Utility Learning | 支撐點擊 / 行為序列與推薦模型關聯 |
| B6 | Explainable mutual fund recommendation | 支撐金融推薦可解釋性 |
| C6 / C7 | GA4 官方文件 | 支撐第三章 GA4 特徵工程與資料限制 |

### 第三優先：補背景、治理與限制

| 編號 | 文獻 | 閱讀目的 |
|---|---|---|
| C1 | FinTech, Investor Sophistication | 數位券商 / FinTech 背景 |
| C4 | IOSCO 2021 AI/ML report | AI/ML 治理、資料品質、模型偏誤 |
| C5 | CFA Investor Trust Study | 個人化與投資人信任 |
| F4 / F5 / F7 | Robo-advisor / investor profiling | 風險輪廓、透明度、投資人理解 |

---

## 研究缺口對應

| 研究缺口 | 可支撐文獻 |
|---|---|
| 既有研究偏重交易資料、靜態屬性或問卷，較少掌握交易前數位互動 | B1、B2、C6、C7、D4 |
| 網站行為資料與基金交易資料整合不足 | B2、B7、C6、C7 |
| 台灣數位券商基金投資服務場域實證不足 | B1、B6、D1–D4、G1–G4 |
| 基金 / 金融商品推薦不同於一般電商推薦，需考慮風險、信任、適合度與治理 | B6、B7、C4、C5、F4、F7 |
| 個人化推薦需與熱門推薦 baseline 比較，才能證明增量效果 | B1、B2、B5、B7 |
| 分群若未連結推薦或服務策略，容易停留在描述層次 | A5、E2、A7、A6 |

---

## 待查證與待補文獻

### 1. 待查證來源

| 編號 | 待查證內容 |
|---|---|
| A1 | 作者資訊與正式引用格式 |
| A3 | 作者、期刊卷期與 DOI |
| B3 | ResearchGate 來源品質與是否有正式出版版本 |
| B4 | ResearchGate 來源品質與是否有正式出版版本 |
| B9 | Sharaf et al. 2022 的 DOI、完整題名與全文 |
| A8 | 作者全名、期刊資訊與正式引用格式 |
| A10 | 作者與正式書目 |
| D1、D2、G3、G4 | NDLTD 詳細作者、學校、年份 |

### 2. 建議後續補文獻

```text
□ 冷啟動問題（Cold-start problem）
□ Top-K 推薦評估指標：Precision@K、Recall@K、MAP、NDCG
□ Elbow Method / Silhouette Score 原始或經典方法文獻
□ K-prototypes 原始文獻：Huang (1998)
□ 台灣金融科技 / 數位券商官方報告
□ 個人資料保護法、資料匿名化與研究倫理相關文獻
```
