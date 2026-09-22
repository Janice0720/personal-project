# 整合版文獻矩陣

論文：應用投資人行為分群與個人化推薦模型於數位券商基金投資服務之研究

最後更新：2026-07-28  
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

1. [📋 全文取得狀態總表（人工查找對照用）](#-全文取得狀態總表人工查找對照用)
2. [A 類：投資人分群、RFM 與機器學習分群方法](#a-類投資人分群rfm-與機器學習分群方法)
3. [B 類：基金與金融商品推薦系統](#b-類基金與金融商品推薦系統)
4. [C 類：FinTech、數位券商、GA4 與 AI 治理](#c-類fintech數位券商ga4-與-ai-治理)
5. [D 類：台灣本土券商與投資人行為研究](#d-類台灣本土券商與投資人行為研究)
6. [E 類：台灣推薦系統、RFM 與金融 CRM 研究](#e-類台灣推薦系統rfm-與金融-crm-研究)
7. [F 類：Robo-advisor、投資人輪廓、信任與透明度](#f-類robo-advisor投資人輪廓信任與透明度)
8. [G 類：台灣共同基金投資人行為與風險偏好](#g-類台灣共同基金投資人行為與風險偏好)
9. [重複與整併對照](#重複與整併對照)
10. [建議核心閱讀順序](#建議核心閱讀順序)
11. [研究缺口對應](#研究缺口對應)
12. [待查證與待補文獻](#待查證與待補文獻)

---

## 📋 全文取得狀態總表（人工查找對照用）

整理日期：2026-09-22。本表彙整 A–G 矩陣正式編號＋`ntub-library-search-plan-2020plus.md` 候選文獻（-cand 編號），對照實際檔案位置，供**人工查找時**快速判斷「這篇還要不要找、去哪裡找」。

**檔案存放位置說明**：
- `literature/downloads/`：已取得的原始全文 PDF（僅存本機，未進版控）
- `literature/reading-summaries/`（含 `pdf-export/`）：已精讀完成、寫成中文摘要筆記的正式矩陣文獻
- `literature/class-readings/`：課堂補充參考文獻，已精讀但不算入正式 A–G 矩陣編號

**狀態圖例**：✅ 全文已取得（含已精讀）｜⚠️ 全文確認無法取得，僅摘要佐證｜⏳ 尚未查找，需人工查找｜🔵 開放取用但尚未下載（可直接查即下載，無需圖書館帳號）

### A 類（投資人分群、RFM、機器學習分群）

| 編號 | 標題（簡） | 狀態 | 檔案 / 摘要來源 | 建議查詢網站 |
|---|---|---|---|---|
| A1 | RFM-Net CNN 分類 | ✅ 已取得（未精讀） | `downloads/A1-RFM-Net_A Convolutional Neural Network for Customer Segment Classification.pdf` | 尚待撰寫 reading-summary |
| A2 | AI-Driven CLV Forecasting | ✅ 已取得（未精讀） | `downloads/A2-AI-Driven CLV Forecasting.pdf` | 尚待撰寫 reading-summary |
| A3 | Enhancing Customer Repurchase Prediction | ⏳ 未查 | — | 北商 ScienceDirect (SDOL) proxy，查標題或 DOI |
| A4 | Football Fans AHP+K-means | ✅ 已取得（未精讀） | `downloads/A4-Football Fans AHP+K-means.pdf` | 尚待撰寫 reading-summary |
| A5 | RFM+群集分析 商品推薦（東海大學） | ❌ 確認受限 | — | NDLTD 授權限制未開放；已用 A12 替代，如需原文須走館際合作（論文編號 110THU01026098） |
| A6 | Malaysian derivatives K-means | ✅ 已取得＋已精讀 | `reading-summaries/A6-tan-2025-...md`（+`pdf-export/`） | 已完成 |
| A7 | RFM ranking | ✅ 已取得＋已精讀 | `reading-summaries/A7-christy-2021-...md`（+`pdf-export/`） | 已完成 |
| A8 | RFM+K-means+Silhouette | ✅ 已取得（未精讀） | `downloads/A8-RFM+K-means+Silhouette.pdf` | 尚待撰寫 reading-summary |
| A9 | K-means/K-prototypes/GMM/DBSCAN cluster tracking（Erasmus 碩論） | ✅ 已取得（未精讀） | `downloads/A9-K-means:K-prototypes:GMM:DBSCAN cluster tracking.pdf` | 尚待撰寫 reading-summary |
| A10 | Intuitive-K-prototypes | ⏳ 未查 | — | ScienceDirect：https://www.sciencedirect.com/science/article/pii/S0031320324008136（北商 SDOL） |
| A11 | RFM+AUM+K-means（Cowrywise 產業案例） | ⏳ 未查（低優先） | — | 官網部落格文章，直接開放瀏覽 |
| A12 | RFM+SOM 適性化推薦（崇越論文大賞） | ✅ 已取得＋已精讀 | `reading-summaries/A12-cheng-2010-...md`（+`pdf-export/`） | 已完成 |
| A13 | Aliyev et al. 銀行 RFM 分群比較 | ✅ 已取得（未精讀） | `downloads/A13-aliyev-2020-rfm-bank-segmentation.pdf` | 尚待撰寫 reading-summary |
| A-cand-1 | Salo（Aalto 碩論）RFM+B 財富管理分群 | ⏳ 未查（摘要也查不到） | — | ProQuest／Aalto 學位論文系統：https://aaltodoc.aalto.fi/items/ebf942d7-2a95-4b5a-bd74-645bc9746c15 |
| A-cand-2 | Arayasaeng et al. RFM-R 泰國商銀 | ⚠️ 僅摘要 | Semantic Scholar 摘要（未存檔案，見 matrix 待查證表） | IEEE Xplore proxy（`eresources.ntub.edu.tw:3609`，先前載入卡住），DOI: 10.1109/ictke58576.2023.10401701 |
| A-cand-3 | Ganar & Hosein 銀行客戶分群+CLV | ⚠️ 僅摘要 | Semantic Scholar 摘要 | IEEE Xplore proxy，DOI: 10.1109/acmlc58173.2022.00017 |
| A-cand-4 | ＝ A13（Aliyev et al.） | ✅ 已取得 | 同 A13 | 已完成 |

### B 類（基金與金融商品推薦系統）

| 編號 | 標題（簡） | 狀態 | 檔案 / 摘要來源 | 建議查詢網站 |
|---|---|---|---|---|
| B1 | GraphDCF 基金推薦 | ✅ 已取得（未精讀） | `downloads/B1-chou-chen-huang-2022-graphdcf.pdf` | 尚待撰寫 reading-summary（**建議優先精讀**） |
| B2 | Dynamic Utility Learning 基金推薦 | ✅ 已取得＋已精讀 | `reading-summaries/B2-wei-liu-2025-...md`（+`pdf-export/`） | 已完成 |
| B3 | 可解釋基金推薦（ResearchGate） | ✅ 已取得（未精讀） | `downloads/B3-MUTUAL FUND RECOMMENDATION SYSTEM WITH PERSONALIZED EXPLANATIONS.pdf` | 尚待撰寫 reading-summary |
| B4 | FinTech 混合推薦引擎（ResearchGate） | ✅ 已取得（未精讀） | `downloads/B4-A Hybrid Recommendation Engine for Fintech Platforms.pdf` | 尚待撰寫 reading-summary |
| B5 | FAR-Trans 資料集 | ✅ 已取得（未精讀） | `downloads/B5-far-trans-2024-arxiv.pdf` | 尚待撰寫 reading-summary |
| B6 | 可解釋基金推薦知識圖譜 | ❌ 確認無法取得 | 摘要見 matrix 內文 | SpringerLink proxy 需機構聯合登入或付費 €39.95，已放棄，改用摘要 |
| B7 | 金融商品推薦 SLR | ✅ 已取得＋已精讀 | `reading-summaries/B7-wu-li-2025-...md`（+`pdf-export/`） | 已完成 |
| B8 | LLM+GNN 金融商品推薦 | ✅ 已取得（未精讀） | `downloads/B8-Research on Personalized Financial Product Recommendation.pdf` | 尚待撰寫 reading-summary |
| B9 | 金融服務推薦綜述 | ⚠️ 僅摘要 | Semantic Scholar 摘要 | SpringerLink proxy（`eresources.ntub.edu.tw:3939`）**2026-09-22 連續當機**，下次可先確認 proxy 是否恢復，或走 Shibboleth 機構登入 |
| B10 | KL距離+K-medoids 基金推薦（Chiou-Wei 2024） | ✅ 已取得＋已精讀 | `class-readings/chiou-wei-2024-kl-km-reading-summary.md` | 已完成（PMC 開放取用） |
| B11 | Fund2Vec 圖學習基金相似度 | ✅ 已取得（未精讀） | `downloads/B11-Fund2Vec- Mutual Funds Similarity using Graph Learning.pdf` | 尚待撰寫 reading-summary |
| B-cand-1 | ＝ B10（Chiou-Wei 2024） | ✅ 已取得 | 同 B10 | 已完成 |
| B-cand-2 | ＝ B9（Sharaf et al. 2022） | ⚠️ 僅摘要 | 同 B9 | 同 B9 |
| B-cand-3 | Pérez-Pons OCI-CBR 混合推薦 | ❌ 下載卡住 | — | ScienceDirect Open Access 文章但 proxy 下載卡住（View PDF 停在跳轉頁不解析），DOI: 10.1016/j.eswa.2022.118568，可再試一次或改用 Cmd+S 手動存檔 |
| B-cand-4 | ＝ B11（Fund2Vec） | ✅ 已取得 | 同 B11 | 已完成 |
| B-cand-5 | Shen/Shi/Shao DIEN 興趣演化 | ⚠️ 僅摘要 | Semantic Scholar 摘要 | IEEE proxy 卡住，DOI: 10.1109/EEBDA53927.2022.9744929 |
| B-cand-6 | Yang（2024）Fuzzy K-means FNFinRec | ⚠️ 僅摘要 | Semantic Scholar／Crossref 摘要 | SpringerLink proxy 需機構登入，DOI: 10.1007/s44196-024-00719-x |

### C 類（FinTech、數位券商、GA4、AI 治理）

| 編號 | 標題（簡） | 狀態 | 檔案 / 摘要來源 | 建議查詢網站 |
|---|---|---|---|---|
| C1 | FinTech 投資人成熟度（Oxford RCFS） | ❌ 確認未訂閱 | — | 北商未訂閱 Oxford Academic；可試 ResearchGate 作者版或直接向作者索取 |
| C2 | 數位投資行為系統性回顧（ResearchGate） | ⏳ 未查 | — | ResearchGate：https://www.researchgate.net/publication/396368845_...（來源品質待查證） |
| C3 | IOSCO AI 資本市場報告 | 🔵 開放取用未下載 | — | 官網直接下載（不需圖書館）：https://www.iosco.org/library/pubdocs/pdf/IOSCOPD788.pdf |
| C4 | IOSCO AI/ML 治理報告 | ✅ 已取得 | `downloads/C4-iosco-2021-ai-ml-governance.pdf` | 已完成 |
| C5 | CFA Institute 投資人信任報告 | ✅ 已取得 | `downloads/C5-cfa-institute-2022-investor-trust.pdf` | 已完成 |
| C6 | GA4 Cohort 官方文件 | 🔵 開放取用未下載 | — | Google 官方線上文件，隨時可查：https://support.google.com/analytics/answer/9670133 |
| C7 | GA4 Segment 類型文件 | 🔵 開放取用未下載 | — | https://support.google.com/analytics/answer/9304353 |
| C8 | FinTech B2B 兩階段分群 | ⏳ 未查（低優先） | — | https://doi.org/10.1080/1051712X.2019.1603420（北商 SDOL 或 Taylor & Francis） |

### D 類（台灣本土券商與投資人行為）

| 編號 | 標題（簡） | 狀態 | 檔案 / 摘要來源 | 建議查詢網站 |
|---|---|---|---|---|
| D1 | 投資人可否從券商推薦股票獲利 | ⏳ 未查 | — | NDLTD：https://ndltd.ncl.edu.tw/handle/46963616466150231805（需驗證碼，人工輸入） |
| D2 | 電視頻道偏好與投資行為 | ⏳ 未查 | — | NDLTD：https://ndltd.ncl.edu.tw/handle/b3agwt |
| D3 | 券商推薦個股資訊內涵（徐楚雯 2019） | ⏳ 未查 | — | NTUST etheses：https://etheses.lib.ntust.edu.tw/thesis/detail/5fbb589dce8828c2ef89fe78e80010e3/ |
| D4 | 網路關鍵字搜尋行為反映投資人情緒 | ✅ 已取得 | `downloads/D4-internet-keyword-search-investor-sentiment-2023.pdf` | 已完成 |
| D5 | 共同基金電子交易平台推薦系統（王怡 2023） | ⚠️ 僅摘要 | matrix 內文摘要 | 需**使用者本人**至臺博碩免費會員系統註冊帳號才能下載，AI 無法代辦：https://hdl.handle.net/11296/xaz6j9 |
| D-cand-1 | NDLTD 檢索式10–12 現場篩選 | ⏳ 未執行 | — | NDLTD 簡易查詢，關鍵字「投資人分群 OR 客戶分群」「RFM AND 金融」（見 `ntub-library-search-plan-2020plus.md` 檢索式11、12） |

### E 類（台灣推薦系統、RFM、金融 CRM）

| 編號 | 標題（簡） | 狀態 | 檔案 / 摘要來源 | 建議查詢網站 |
|---|---|---|---|---|
| E1 | 個人化推薦與退貨行為（淡江大學） | ⏳ 未查 | — | NDLTD：https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?o=dnclcdr&s=id=%22110TKU05121038%22.&searchmode=basic |
| E2 | RFM 顧客分群行銷策略（保健食品公司） | ❌ 確認受限 | — | NDLTD 授權限制未開放；已用 E5 替代，如需原文須走館際合作或 NTUST 電子論文系統（論文編號 109NTUS5121030） |
| E3 | 用戶序列協同過濾推薦 | ⏳ 未查 | — | NDLTD：https://ndltd.ncl.edu.tw/handle/3pake6 |
| E4 | 資料探勘金融機構 CRM | ⏳ 未查 | — | NTUST etheses：https://etheses.lib.ntust.edu.tw/detail/5f04fdb7c1c54021a137ad835327d677/ |
| E5 | RFM+購物籃分析電商分群（政大） | ✅ 已取得＋已精讀 | `reading-summaries/E5-chen-2021-...md`（+`pdf-export/`） | 已完成 |
| E6 | 台灣券商大財管業務 K-means 分群 | ✅ 已取得（未精讀） | `downloads/E-cand-1-xu-2022-ml-securities-wealth-management.pdf` | 尚待撰寫 reading-summary（**建議優先精讀**） |
| E7 | 零售業 RFM 衍伸+推薦（中原大學） | ❌ 確認 embargo | — | 全文 embargo 至 2029/04/10，目前無法提前取得，已有完整摘要佐證 |
| E-cand-1 | ＝ E6 | ✅ 已取得 | 同 E6 | 已完成 |
| E-cand-2 | ＝ E7 | ❌ embargo | 同 E7 | 同 E7 |

### F 類（Robo-advisor、投資人輪廓、信任與透明度）

| 編號 | 標題（簡） | 狀態 | 檔案 / 摘要來源 | 建議查詢網站 |
|---|---|---|---|---|
| F1 | 台灣投資人機器人理財意圖（政大） | ⏳ 未查 | — | Airiti：https://www.airitilibrary.com/Article/Detail/U0004-G0107351022（可試北商 Airiti proxy） |
| F2 | 提升機器人理財使用意願 | ⏳ 未查 | — | NDLTD：http://ndltd.ncl.edu.tw/handle/dqk4c3 |
| F3 | 機器人理財消除行為偏誤（台北大學） | ⏳ 未查 | — | NDLTD：https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?o=dnclcdr&s=id=%22108NTPU0121042%22.&searchmode=basic |
| F4 | Robo Advising and Investor Profiling | ⏳ 未查 | — | MDPI 官網直接下載（開放取用）：https://doi.org/10.3390/fintech3010007 |
| F5 | Robo-advisor 系統性文獻回顧 | ✅ 已取得 | `downloads/F5-cardillo-chiappini-2024-robo-advisors-slr.pdf` | 已完成 |
| F6 | 永續 Robo-advisor 商業模式 | ⏳ 未查（低優先） | — | MDPI 官網直接下載（開放取用）：https://doi.org/10.3390/su132313009 |
| F7 | Robo-advisor 與一般投資人金融化 | ✅ 已取得 | `downloads/F7-tan-2020-robo-advisors-financialization.pdf` | 已完成 |

### G 類（台灣共同基金投資人行為與風險偏好）

| 編號 | 標題（簡） | 狀態 | 檔案 / 摘要來源 | 建議查詢網站 |
|---|---|---|---|---|
| G1 | 共同基金投資人風險偏好（吳忠義 2008） | ✅ 已取得＋已精讀 | `reading-summaries/G1-wu-2008-...md`（+`pdf-export/`） | 已完成 |
| G2 | 台灣地區共同基金投資行為實證（鄭芳盈 2007） | ❌ 確認未授權 | matrix 內文摘要 | 北商 Airiti 亦未授權此篇，無其他管道，僅能引用摘要 |
| G3 | 基金投資人現狀偏誤（林亞萱 2013） | ⚠️ 僅國圖紙本 | matrix 內文完整摘要 | 僅「國圖紙本論文」，需親自到國家圖書館調閱：https://hdl.handle.net/11296/bx5udf |
| G4 | 市場狀態與基金投資人投資行為（林敏婷 2010） | ⚠️ 僅國圖紙本 | matrix 內文完整摘要 | 僅「國圖紙本論文」，需親自到國家圖書館調閱：https://hdl.handle.net/11296/dwd5gh |

### 課堂補充文獻（已精讀，非正式矩陣編號）

| 文獻 | 狀態 | 檔案 |
|---|---|---|
| 徐火志（2006）改良式RFM+SOM分群 | ✅ 已取得＋已精讀 | `class-readings/hsu-2006-refined-rfm-som-customer-segmentation-reading-summary.md` |
| Wang et al.（2025）機器學習公債殖利率預測 | ✅ 已取得＋已精讀 | `class-readings/wang-2025-ml-treasury-yield-forecasting-reading-summary.md` |
| Ni Rui（2025）集群分析金融商品推薦最佳化 | ✅ 已取得＋已精讀 | `class-readings/ni-2025-cluster-analysis-financial-product-recsys-reading-summary.md` |
| FundRecLLM（2023）LLM基金推薦 | ✅ 已取得＋已精讀 | `class-readings/fundrecllm-2023-llm-fund-recommendation-reading-summary.md` |

### 總計

- **✅ 全文已取得**：34 篇（含已精讀 13 篇：A6、A7、A12、B2、B7、B10、E5、G1 共 8 篇矩陣文獻 + 4 篇課堂參考；未精讀 14 篇：A13、B1、B5、E6、F5、F7、C4、C5、D4、A1、A2、A4、A8、A9、B3、B4、B8、B11/B-cand-4 —— 2026-09-22 使用者手動新增 A1、A2、A4、A8、A9、B3、B4、B8、B11 共 9 篇）
- **⚠️ 僅摘要（全文暫不可得，非因未查找而是管道已確認不通）**：B9/B-cand-2、B-cand-5、B-cand-6、A-cand-2、A-cand-3、D5、G3、G4
- **❌ 確認全文無法取得**：A5、B6、B-cand-3、C1、E2、E7/E-cand-2、G2
- **🔵 開放取用但尚未實際下載**：C3、C6、C7（隨時可查，優先權低是因為官方文件不會過期）
- **⏳ 尚未查找**：A3、A10、A11、A-cand-1、C2、C8、D1、D2、D3、D-cand-1、E1、E3、E4、F1、F2、F3、F4、F6

---

## A 類：投資人分群、RFM 與機器學習分群方法

| # | 論文標題 | 作者 | 年份 | 來源 | 核心方法 / 內容 | 本研究關聯 | 優先級 | 連結 |
|---|---|---|---:|---|---|---|---|---|
| A1 | RFM-Net: A Convolutional Neural Network for Customer Segment Classification | — | 2026 | Applied Sciences / MDPI | CNN + RFM 特徵分類；準確率 94.33% | 分群方法比較基準；RFM 特徵設計參考。**✅ 2026-09-22 全文已取得**（使用者手動下載），存於 `literature/downloads/A1-RFM-Net_A Convolutional Neural Network for Customer Segment Classification.pdf` | 中 | https://www.mdpi.com/2076-3417/16/5/2223 |
| A2 | Artificial Intelligence-Driven CLV Forecasting: Integrating RFM Analysis with ML for Strategic Customer Retention | Akter et al. | 2025 | JCSTS / ResearchGate | K-means++、XGBoost、AHP 加權 RFM、動態 CLV | 特徵加權與 K-means++ 應用參考。**✅ 2026-09-22 全文已取得**（使用者手動下載），存於 `literature/downloads/A2-AI-Driven CLV Forecasting.pdf` | 中 | https://www.researchgate.net/publication/389495515_Artificial_Intelligence-Driven_Customer_Lifetime_Value_CLV_Forecasting_Integrating_RFM_Analysis_with_Machine_Learning_for_Strategic_Customer_Retention |
| A3 | Enhancing Customer Repurchase Prediction: Integrating Classification Algorithms with RFM Analysis for Precision and Actionable Insights | — | 2025 | ScienceDirect | RFM + 分類演算法、10-fold 交叉驗證 | 模型評估與驗證方法參考 | 低 | https://www.sciencedirect.com/science/article/pii/S0970389625000266 |
| A4 | Unlocking High-Value Football Fans: Unsupervised ML for Customer Segmentation and Lifetime Value | — | 2024 | Frontiers in Sports and Active Living | AHP 加權 RFM + K-means，識別 8 個群體 | 無監督分群流程與群體命名參考。**✅ 2026-09-22 全文已取得**（使用者手動下載），存於 `literature/downloads/A4-Football Fans AHP+K-means.pdf` | 中 | https://doi.org/10.3389/fspor.2024.1362489 |
| A5 | 以 RFM 模型結合群集分析建立顧客分群暨商品推薦之研究 | — | 2022 | 東海大學碩士論文 | RFM + 群集分析 + 商品推薦流程 | 台灣碩士論文範本；研究設計與章節結構可對照。**⚠️ 全文受限（NDLTD 授權限制，未取得）→ 改讀 A12** | 高 | https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?o=dnclcdr&s=id=%22110THU01026098%22.&searchmode=basic |
| A6 | Profiling investor behavior in the Malaysian derivatives market using K-means clustering | Tan et al. | 2025 | Frontiers in Artificial Intelligence | K-means、IHS transformation、decision tree validation；1,100 萬筆交易資料 | 金融交易行為分群方法參考；雖非基金但場景接近。**✅ 2026-08-26 全文已取得** | 高 | https://doi.org/10.3389/frai.2025.1640776 |
| A7 | RFM ranking – An effective approach to customer segmentation | Christy et al. | 2021 | Journal of King Saud University - Computer and Information Sciences | RFM、K-means、Fuzzy C-Means | 支撐本研究交易 RFM / 行為 RFM 特徵工程。**✅ 2026-08-26 全文已取得** | 高 | https://doi.org/10.1016/j.jksuci.2018.09.004 |
| A8 | RFM model for customer purchase behavior using K-Means algorithm | Anitha; Patil R. P.（待查證） | 2021 | Journal of King Saud University - Computer and Information Sciences | RFM、K-means、Silhouette Coefficient | 補強分群品質評估指標設計。**✅ 2026-09-22 全文已取得**（使用者手動下載），存於 `literature/downloads/A8-RFM+K-means+Silhouette.pdf` | 中 | https://www.sciencedirect.com/science/article/pii/S1319157819309802 |
| A9 | Tracking Customer Segments in Alternative Finance using time-evolving Cluster Analysis | Lennert Aerts | 2020 | Erasmus University Rotterdam Master Thesis | K-means、K-prototypes、GMM、DBSCAN、cluster tracking | 若後續做分群穩定性或混合型資料，可作方法參考。**✅ 2026-09-22 全文已取得**（使用者手動下載），存於 `literature/downloads/A9-K-means:K-prototypes:GMM:DBSCAN cluster tracking.pdf` | 中 | https://thesis.eur.nl/pub/52256/Aerts.pdf |
| A10 | Intuitive-K-prototypes: A mixed data clustering algorithm with improved prototype representation and attribute weights | 作者待補 | 2024 | Pattern Recognition / Elsevier | K-prototypes、混合型資料分群、attribute weighting | 若同時使用數值與類別特徵，支撐 K-prototypes 合理性 | 中 | https://www.sciencedirect.com/science/article/pii/S0031320324008136 |
| A11 | Using RFM, AUM, and K-means clustering for customer segmentation | Uchechukwu Emmanuel / Cowrywise | 2025 | Metabase Community / Cowrywise 產業案例 | RFM + AUM + K-means | FinTech / 財富管理平台分群實務案例；適合作背景，不宜作核心學術引用 | 低 | https://www.metabase.com/community-posts/using-rfm-aum-and-k-means-clustering-customers-segmentation |
| A12 | 基於RFM分析法之顧客適性化產品推薦機制（An Adaptive Product Recommendation System Based on RFM Method） | — | 2010 | 崇越論文大賞（**全文開放 PDF**） | RFM 分析 + 自組織地圖（SOM）+ 適性化商品推薦機制；考量產品購買週期與顧客消費特性 | **A5 之替代閱讀文獻**；RFM 結合分群與商品推薦的流程設計可對照；全文可直接下載 | 高 | https://thesis.topco-global.com/TopcoTRC/2010_Thesis/C0026.pdf（PDF 全文）／https://www.airitilibrary.com/Article/Detail/U0078-0601201112112856（Airiti） |
| A13 | Segmenting Bank Customers via RFM Model and Unsupervised Machine Learning | Aliyev, Ahmadov, Gadirli, Mammadova & Alasgarov | 2020 | arXiv:2008.08662（未見正式出版） | 亞塞拜然某私人銀行真實客戶資料；RFM＋K-means／DBSCAN 等多種分群演算法比較 | 銀行真實資料分群演算法選擇背景，可支撐 K-means vs 其他演算法之取捨論述；**✅ 開放取用**，僅 arXiv 預印本。**✅ 2026-09-21 全文已下載**，存於 `literature/downloads/A13-aliyev-2020-rfm-bank-segmentation.pdf` | 中 | https://arxiv.org/abs/2008.08662 |

---

## B 類：基金與金融商品推薦系統

| # | 論文標題 | 作者 | 年份 | 來源 | 核心方法 / 內容 | 本研究關聯 | 優先級 | 連結 |
|---|---|---|---:|---|---|---|---|---|
| B1 | Modeling Behavior Sequence for Personalized Fund Recommendation with Graphical Deep Collaborative Filtering | Chou, Chen & Huang | 2022 | Expert Systems with Applications, Vol. 192 | GraphDCF；基金交易序列與圖式協同過濾；資料集為台灣某商業銀行之基金、客戶與歷史交易紀錄 | 最核心基金推薦文獻；支撐推薦模型與交易序列設計；台灣真實銀行資料場景直接對應研究缺口。**✅ 2026-09-21 已於北商圖書館 ScienceDirect Online (SDOL) 取得全文 PDF**，存於 `literature/downloads/B1-chou-chen-huang-2022-graphdcf.pdf` | 高 | https://doi.org/10.1016/j.eswa.2021.116311（ScienceDirect） |
| B2 | Personalized Fund Recommendation with Dynamic Utility Learning | Wei & Liu | 2025 | Financial Innovation | Incremental utility learning、點擊序列、探索 / 利用 | 連接數位行為資料與基金推薦；與 GA4 行為資料高度相關。**✅ 2026-07-28 全文已下載** | 高 | https://doi.org/10.1186/s40854-024-00720-5 |
| B3 | Mutual Fund Recommendation System with Personalized Explanations | — | 2023 | ResearchGate | 知識圖譜、ML、可解釋推薦 | 支撐金融推薦可解釋性；需查證來源品質。**✅ 2026-09-22 全文已取得**（使用者手動下載），存於 `literature/downloads/B3-MUTUAL FUND RECOMMENDATION SYSTEM WITH PERSONALIZED EXPLANATIONS.pdf` | 中 | https://www.researchgate.net/publication/367530626_MUTUAL_FUND_RECOMMENDATION_SYSTEM_WITH_PERSONALIZED_EXPLANATIONS |
| B4 | A Hybrid Recommendation Engine for Fintech Platforms: Leveraging Behavioral Analytics for User Engagement and Conversion | — | 2025 | ResearchGate | 混合推薦、CF、Content-based、Deep Learning、行為分析 | 可作 FinTech 混合推薦架構參考；需查證來源品質。**✅ 2026-09-22 全文已取得**（使用者手動下載），存於 `literature/downloads/B4-A Hybrid Recommendation Engine for Fintech Platforms.pdf` | 中 | https://www.researchgate.net/publication/394559448_A_Hybrid_Recommendation_Engine_for_Fintech_Platforms_Leveraging_Behavioral_Analytics_for_User_Engagement_and_Conversion |
| B5 | FAR-Trans: An Investment Dataset for Financial Asset Recommendation | Sanz-Cruzado, Droukas & McCreadie | 2024 | arXiv:2407.08692 | 金融資產推薦資料集、資產定價與散戶交易紀錄；歐洲某大型金融機構真實交易資料，並提供11種FAR演算法基準比較 | 可作外部資料集與推薦評估基準背景。**✅ 2026-09-22 全文已下載**，存於 `literature/downloads/B5-far-trans-2024-arxiv.pdf` | 中 | https://arxiv.org/abs/2407.08692 |
| B6 | Explainable mutual fund recommendation system developed based on knowledge graph embeddings | Hsu, Chen, Chou & Huang | 2022 | Applied Intelligence, Vol. 52, pp. 10779–10804 | Knowledge Graph Embedding、可解釋共同基金推薦；預測並解釋客戶次月基金申購行為 | 補強信任與可解釋性；與 B1 為同一研究群（共同作者 Chiao-Ting Chen、Szu-Hao Huang），可形成台灣基金推薦文獻群。**⚠️ 2026-09-21 確認：SpringerLink 需機構聯合登入（Shibboleth WAYF）或付費 €39.95，全文無法取得，改以公開摘要佐證**（摘要已取得，見待查證表） | 高 | https://doi.org/10.1007/s10489-021-03136-1 |
| B7 | A Systematic Literature Review of Financial Product Recommendation Systems | Wu & Li | 2025 | Information / MDPI | 系統性文獻回顧；金融商品推薦特殊性 | 第二章推薦系統總覽與研究缺口核心來源。**✅ 2026-07-28 全文已取得** | 高 | https://doi.org/10.3390/info16030196 |
| B8 | Research on Personalized Financial Product Recommendation by Integrating Large Language Models and Graph Neural Networks | Zhao et al. | 2025 | arXiv / ACM ICSECA | LLM embeddings + heterogeneous graph + GNN | 最新技術趨勢；可用來說明本研究不採 LLM/GNN 的邊界。**✅ 2026-09-22 全文已取得**（使用者手動下載），存於 `literature/downloads/B8-Research on Personalized Financial Product Recommendation.pdf` | 中 | https://arxiv.org/abs/2506.05873 |
| B9 | A survey on recommendation systems for financial services | Sharaf, Hemdan, El-Sayed & El-Bahnasawy | 2022 | Multimedia Tools and Applications, 81(12), 16761–16781 | 金融服務推薦綜述 | 推薦系統背景文獻，與 B7 形成 2022／2025 兩篇綜述對照。DOI 已確認，全文待查（SpringerLink，預期需機構登入） | 中 | https://doi.org/10.1007/s11042-022-12564-1 |
| B10 | Application of KL distance-based intelligent recommendation method to fund recommendation for users with investment behavior in Asia Region | Chiou-Wei & Lee | 2024 | Heliyon, 10(12), e32959 | 改良式 KL 距離＋K-medoids 分群基金推薦；混合推薦模型表現最佳（MAE≈0.82–0.83） | 課堂已精讀（見 `class-readings/chiou-wei-2024-kl-km-reading-summary.md`）；台灣作者（高雄科技大學）；**✅ 開放取用全文**，資料集為「銀行基金經理客戶資料」但未明確揭露地區與規模，屬限制 | 高 | https://doi.org/10.1016/j.heliyon.2024.e32959（PMC 開放取用：https://pmc.ncbi.nlm.nih.gov/articles/PMC11252857/） |
| B11 | Fund2Vec: Mutual Funds Similarity using Graph Learning | Satone, Desai & Mehta | 2021 | arXiv:2106.12987（未見正式出版） | Node2Vec 圖學習；基金相似度（結構相似而非僅重疊度） | 基金相似度可用於內容導向推薦之外的 baseline 討論；僅 arXiv 預印本，引用時需註明未經同儕審查。**✅ 2026-09-22 全文已取得**（使用者手動下載），存於 `literature/downloads/B11-Fund2Vec- Mutual Funds Similarity using Graph Learning.pdf` | 中 | https://arxiv.org/abs/2106.12987 |

---

## C 類：FinTech、數位券商、GA4 與 AI 治理

| # | 論文 / 報告標題 | 作者 / 機構 | 年份 | 來源 | 核心內容 | 本研究關聯 | 優先級 | 連結 |
|---|---|---|---:|---|---|---|---|---|
| C1 | FinTech, Investor Sophistication, and Financial Portfolio Choices | — | 2023 | Review of Corporate Finance Studies / Oxford | FinTech 平台影響投資人成熟度與投資組合選擇 | Ch1 背景；數位券商對投資行為影響。**⚠️ 2026-09-22 確認：北商圖書館未訂閱 Oxford Academic**（整合查詢搜尋「Oxford」0筆結果），全文暫無法取得，僅能引用摘要 | 高 | https://academic.oup.com/rcfs/article/12/4/834/7192186 |
| C2 | The Digital Transformation of Investment Behavior: A Systematic Review of Gambling Tendencies in Modern Financial Markets | — | 2024 | ResearchGate | 數位化投資行為、行為偏誤系統性回顧 | 支撐數位平台與投資人行為改變；需查證來源品質 | 中 | https://www.researchgate.net/publication/396368845_The_digital_transformation_of_investment_behavior_a_systematic_review_of_gambling_tendencies_in_modern_financial_markets |
| C3 | Artificial Intelligence in Capital Markets: Use Cases, Risks, and Challenges | IOSCO | 2023 | IOSCO 官方報告 | AI 在資本市場應用、風險與監理挑戰 | Ch1 背景、Ch5 限制與監理討論 | 高 | https://www.iosco.org/library/pubdocs/pdf/IOSCOPD788.pdf |
| C4 | The use of artificial intelligence and machine learning by market intermediaries and asset managers | IOSCO Board | 2021 | IOSCO Final Report | AI/ML 治理、測試、監控、揭露、資料品質與偏誤 | 金融推薦模型治理、資料品質與可解釋性權威來源。**✅ 2026-09-22 全文已下載**（官網直接開放取用），存於 `literature/downloads/C4-iosco-2021-ai-ml-governance.pdf` | 高 | https://www.iosco.org/library/pubdocs/pdf/IOSCOPD684.pdf |
| C5 | Enhancing Investors’ Trust: 2022 CFA Institute Investor Trust Study | CFA Institute | 2022 | CFA Institute | 投資人信任、科技、個人化、people plus technology | 支撐數位券商為何需要個人化服務與信任設計。**✅ 2026-09-22 全文已下載**（官網直接開放取用），存於 `literature/downloads/C5-cfa-institute-2022-investor-trust.pdf` | 高 | https://www.cfainstitute.org/sites/default/files/-/media/documents/article/Enhancing-Investors-Trust-Report_2022_Online.pdf |
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
| D4 | 網路關鍵字搜尋行為反映投資人情緒之研究 | — | 2023 | Airiti Library | Google 搜尋趨勢與投資人情緒；三篇研究構成，涵蓋2012年7月至2022年6月共10年期間資料，分析Google搜尋趨勢指數對股票報酬與股價盈餘比交互作用之影響 | 支撐數位搜尋 / 行為資料可作投資人意圖代理變數。**✅ 2026-09-22 全文已下載**（北商 Airiti proxy 直接授權下載），存於 `literature/downloads/D4-internet-keyword-search-investor-sentiment-2023.pdf` | 中 | https://www.airitilibrary.com/Article/Detail/U0002-1107202310513600 |
| D5 | 推薦系統之應用——以共同基金電子交易平台為例（The Recommendation System Application for a Mutual Fund Electronic Trading Platform） | 王怡 | 2023 | 東吳大學巨量資料管理學院碩士學位學程 / 臺博碩（論文編號 111SCU01448003） | 研究台灣 5 家代理銷售共同基金電子交易平台業者之經營實務，探討安全、完善有效率之交易目標，以及運用 AI 找出有效影響因子 | **主題與研究場域高度貼合**：直接指出「國內也有五家代理銷售共同基金的電子交易平台」，可作為第一章市場背景之台灣本土引用（好好證券即屬此類業者）。**⚠️ 全文需臺博碩免費會員登入下載**（帳號需使用者自行註冊），僅取得公開摘要 | 高 | https://hdl.handle.net/11296/xaz6j9 |

---

## E 類：台灣推薦系統、RFM 與金融 CRM 研究

| # | 論文標題 | 作者 | 年份 | 來源 | 核心方法 / 內容 | 本研究關聯 | 優先級 | 連結 |
|---|---|---|---:|---|---|---|---|---|
| E1 | 個人化推薦系統、顧客購買意願與後續退貨行為之影響 | — | 2022 | 淡江大學碩士論文 / 臺博碩 | 電商個人化推薦與購買意願 | 台灣推薦系統對使用者行為影響背景 | 中 | https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?o=dnclcdr&s=id=%22110TKU05121038%22.&searchmode=basic |
| E2 | 應用 RFM 模型制定顧客分群行銷策略之研究——以 A 保健食品公司為例 | — | 2020 | 臺灣科技大學碩士論文 / 臺博碩 | RFM 模型、顧客分群、行銷策略 | 台灣 RFM 分群行銷論文範本；方法論可對照。**⚠️ 全文受限（NDLTD 授權限制，2026-07-28 搜尋未找到開放版本）→ 建議透過學校館際合作申請（論文編號：109NTUS5121030）或參考 E5** | 高 | https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?o=dnclcdr&s=id=%22109NTUS5121030%22.&searchmode=basic |
| E3 | 基於用戶序列之協同過濾推薦 | — | — | 臺博碩 | 使用者序列行為、協同過濾 | 台灣協同過濾推薦系統研究脈絡 | 中 | https://ndltd.ncl.edu.tw/handle/3pake6 |
| E4 | 資料探勘分析於金融機構客戶關係經營之研究 | — | — | 臺灣科技大學碩士論文 | Data Mining、金融機構 CRM、分群 | 金融業資料探勘與 CRM 應用支撐 | 中 | https://etheses.lib.ntust.edu.tw/detail/5f04fdb7c1c54021a137ad835327d677/ |
| E5 | 利用RFM模型與購物籃分析進行電子商務顧客分群與銷售策略之研究（A Research On e-commerce seller's sales strategy using RFM Model and Market Basket Analysis） | 陳一慈 | 2021 | 國立政治大學碩士論文 / Airiti Library（DOI: 10.6814/NCCU202100799） | RFM 模型 + 購物籃分析 + 顧客分群 + 銷售策略；美妝電商案例 | **E2 之替代參考文獻**；同樣是台灣碩論，以 RFM 做顧客分群並轉換行銷策略，方法論脈絡相近；Airiti 上可查，建議透過學校帳號登入存取 | 高 | https://www.airitilibrary.com/Article/Detail/U0004-G0108363104 |
| E6 | 運用機器學習方法推廣綜合券商大財管業務（Expand Integrated Securities Firm's Business Using Machine Learning） | 許仲廷 | 2022 | Journal of Data Analysis, 17卷2期, Pp. 31-58（**Open Access**） | 統一證券保代／海外市場／財富管理三大業務客戶特徵；k-means 分群建立大財管客戶素描；分類演算法辨別新開戶大財管商品偏好 | **最貼近本研究之台灣真實券商客戶分群案例**，同時涵蓋分群＋分類預測（新戶商品偏好），可直接支撐「分群輔助推薦」在台灣券商場景之合理性。**✅ 2026-09-21 全文已下載**，存於 `literature/downloads/E-cand-1-xu-2022-ml-securities-wealth-management.pdf` | 高 | https://doi.org/10.6338/JDA.202206_17(2).0002 |
| E7 | 結合關聯法則與機器學習演算法於適性化產品推薦機制─以零售業RFM衍伸模型為基礎 | 溫國抆（Gunawan Sebastian） | 2024 | 中原大學碩士論文 | 修正版 RFM（含 Periodicity、Length、Customer Engagement Index）+ K-means/Ward 分群 + 關聯規則推薦 + 分類器驗證（KNN、Random Forest 表現最佳） | 場景為零售業（非金融），僅適合作方法論對照（RFM 衍伸特徵設計、分群後接分類/推薦的流程）；**⚠️ 全文embargo至 2029/04/10 才開放下載**，目前僅能引用公開摘要 | 中 | https://doi.org/10.6840/cycu202400186 |

---

## F 類：Robo-advisor、投資人輪廓、信任與透明度

| # | 論文標題 | 作者 | 年份 | 來源 | 核心內容 | 本研究關聯 | 優先級 | 連結 |
|---|---|---|---:|---|---|---|---|---|
| F1 | 台灣投資人對於機器人理財行為意圖之研究 | 陳奕君 | 2020 | 政治大學碩士論文 / Airiti | 台灣投資人對 robo-advisor 的採用意圖 | 台灣數位理財接受度背景 | 中 | https://www.airitilibrary.com/Article/Detail/U0004-G0107351022 |
| F2 | 提升投資人使用機器人理財意願之研究 | — | — | 臺博碩 | 機器人理財、科技接受模型、投資新手 | 台灣數位理財服務採用障礙 | 中 | http://ndltd.ncl.edu.tw/handle/dqk4c3 |
| F3 | 機器人理財服務是否可有效消除投資人行為偏誤 | — | 2019 | 臺北大學碩士論文 / 臺博碩 | Robo-advisor 與行為偏誤 | 數位化服務對投資行為偏誤的影響 | 中 | https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?o=dnclcdr&s=id=%22108NTPU0121042%22.&searchmode=basic |
| F4 | Robo Advising and Investor Profiling | Gaspar & Oliveira | 2024 | FinTech / MDPI | 投資人風險輪廓、RRA、Mean-Variance | 支撐投資人 profiling 與風險屬性適配 | 高 | https://doi.org/10.3390/fintech3010007 |
| F5 | Robo-advisors: A systematic literature review | Cardillo & Chiappini | 2024 | Finance Research Letters | Robo-advisor 系統性文獻回顧 | 數位投資服務與 robo-advisor 背景總覽。**✅ 2026-09-22 於北商圖書館 ScienceDirect Online (SDOL) 取得全文**，存於 `literature/downloads/F5-cardillo-chiappini-2024-robo-advisors-slr.pdf` | 高 | https://doi.org/10.1016/j.frl.2024.105119 |
| F6 | Business Model of Sustainable Robo-Advisors: Empirical Insights for Practical Implementation | Au et al. | 2021 | Sustainability / MDPI | 永續 robo-advisor 採用意願 | 可作 ESG / 價值觀偏好與個人化背景 | 低 | https://doi.org/10.3390/su132313009 |
| F7 | Robo-advisors and the financialization of lay investors | Tan, Gordon Kuo Siong | 2020 | Geoforum, 117 (2020) 46-60 | 演算法透明度、一般投資人、金融教育；新加坡金融科技場景，探討 robo-advisor 如何使投資人在人機互動網絡中角色被動化 | 支撐金融推薦需考量透明度、理解與信任。**✅ 2026-09-22 於北商圖書館 ScienceDirect Online (SDOL) 取得全文**（Complimentary access），存於 `literature/downloads/F7-tan-2020-robo-advisors-financialization.pdf` | 中 | https://doi.org/10.1016/j.geoforum.2020.09.017 |

---

## G 類：台灣共同基金投資人行為與風險偏好

| # | 論文標題 | 作者 | 年份 | 來源 | 核心內容 | 本研究關聯 | 優先級 | 連結 |
|---|---|---|---:|---|---|---|---|---|
| G1 | 共同基金投資人投資行為及風險偏好之研究 | — | 2009 | 臺博碩 / Airiti | 依風險程度將投資人分為保守、穩健、積極 | 台灣基金投資人風險分群參考；KYC 風險等級支撐。**✅ 2026-07-28 全文已取得** | 高 | https://ndltd.ncl.edu.tw/handle/7msk6p |
| G2 | 台灣地區共同基金投資行為實證研究 | 鄭芳盈（指導教授：吳忠敏） | 2007 | Airiti Library（國立臺北科技大學商業自動化與管理研究所碩士論文） | 以客戶風險屬性搭配行銷策略；BPN 神經網路（正確率72.41%）與 CART 分類樹（正確率71.07%）模型比較，依性別、教育、風險偏好分類 | 台灣基金投資人行為分類早期實證。**⚠️ 2026-09-22 確認：即使透過北商圖書館 Airiti proxy 仍顯示「未授權」，全文無法取得，改用摘要佐證** | 中 | https://www.airitilibrary.com/Article/Detail?DocID=U0006-0908200717040800 |
| G3 | 基金投資人是否存在現狀偏誤：來自台灣之證據 | 林亞萱（指導教授：陳皆碩、林芳綺） | 2013 | 臺博碩（國立彰化師範大學會計學系碩士論文） | 檢測台灣共同基金市場投資人現狀偏誤（Status Quo Bias）；以2003–2012年台灣投信投顧基金為樣本，多變量迴歸模型；發現基金當期流量與前期流量正相關，可選擇基金檔數越多現狀偏誤越強 | 解釋分群結果中可能的非理性行為。**⚠️ 2026-09-22 確認：僅「國圖紙本論文」，無電子全文，已取得完整摘要佐證** | 中 | https://hdl.handle.net/11296/bx5udf |
| G4 | 市場狀態與基金投資人投資行為之探討 | 林敏婷（指導教授：張志雄） | 2010 | 臺博碩（義守大學財務金融學系碩士論文，98學年度） | 不同市場狀態（多頭/空頭/盤整）下基金申購與贖回行為；以2001年7月至2009年3月180檔台灣開放式股票型基金為樣本，發現市場狀態顯著影響投資人處分效果 | 外部市場環境對投資行為影響；可放研究限制。**⚠️ 2026-09-22 確認：僅「國圖紙本論文」，無電子全文，已取得完整摘要佐證** | 中 | https://hdl.handle.net/11296/dwd5gh |

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
| 1 | A5 | 以 RFM 模型結合群集分析建立顧客分群暨商品推薦之研究 **⚠️ 全文受限，未取得** | — |
| 1b | A12 | 基於RFM分析法之顧客適性化產品推薦機制（**A5 替代文獻，全文開放**） | 看 RFM 分析如何設計顧客分群與商品推薦流程（PDF 可直接下載） |
| 2 | E2 | 應用 RFM 模型制定顧客分群行銷策略之研究 **⚠️ 全文受限，未取得** | — |
| 2b | E5 | 利用RFM模型與購物籃分析進行電子商務顧客分群與銷售策略之研究（**E2 替代文獻，Airiti 可查**） | 看台灣 RFM 分群與銷售策略轉換寫法（建議以學校帳號登入 Airiti 下載） |
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
| 分群若未連結推薦或服務策略，容易停留在描述層次 | A5（全文受限）、A12、E2、A7、A6 |

---

## 待查證與待補文獻

### 1. 待查證來源

| 編號 | 待查證內容 |
|---|---|
| A5 | **全文受限（NDLTD 授權限制）**；2026-07-28 搜尋未找到開放版本；已以 A12 作為替代閱讀文獻。如仍需原文，建議透過學校圖書館館際合作申請（論文編號：110THU01026098） |
| B1 | ✅ **已解決**：2026-09-21 於北商圖書館 ScienceDirect Online (SDOL) 取得全文 PDF |
| B6 | ⚠️ **確認全文無法取得**（2026-09-21）：SpringerLink 需機構聯合登入或付費，改以公開摘要佐證，不強求全文 |
| E2 | **全文受限（NDLTD 授權限制）**；2026-07-28 搜尋未找到開放版本；已以 E5 作為替代參考文獻。如仍需原文，建議透過學校圖書館館際合作申請（論文編號：109NTUS5121030）或至 NTUST 電子論文系統（etheses.lib.ntust.edu.tw）以學校帳號查詢 |
| A12 | 作者全名待補；年份依 Topco 資料夾為 2010，Airiti 上有 2011/2012 期刊版本，正式引用格式需確認 |
| A1 | 作者資訊與正式引用格式 |
| A3 | 作者、期刊卷期與 DOI |
| B3 | ResearchGate 來源品質與是否有正式出版版本 |
| B4 | ResearchGate 來源品質與是否有正式出版版本 |
| B9 | Sharaf et al. 2022 的 DOI、完整題名與全文；**✅ 2026-09-21 已用 Semantic Scholar 取得摘要**。**⚠️ 2026-09-22 再次嘗試 SpringerLink proxy（eresources.ntub.edu.tw:3939）失敗**：proxy 首頁與文章頁連續多次顯示錯誤頁面，無法進入，暫緩，改用摘要佐證 |
| A8 | 作者全名、期刊資訊與正式引用格式 |
| A10 | 作者與正式書目 |
| D1、D2、G3、G4 | NDLTD 詳細作者、學校、年份 |

### 2. 建議後續補文獻

2020 年後金融商品推薦／客戶分群的補強查詢，已另寫成 [`ntub-library-search-plan-2020plus.md`](ntub-library-search-plan-2020plus.md)，請用北商電子資源系統執行，查回後再併入本矩陣。

```text
□ 2020 年後基金／金融商品推薦期刊（優先：Chiou-Wei 2024、Sharaf 2022、Pérez-Pons 2023）
□ 2020 年後金融業 RFM／財富管理分群
□ 2020 年後台灣券商／財富管理客戶分群（華藝、臺博碩）
□ 冷啟動問題（Cold-start problem）
□ Top-K 推薦評估指標：Precision@K、Recall@K、MAP、NDCG
□ Elbow Method / Silhouette Score 原始或經典方法文獻
□ K-prototypes 原始文獻：Huang (1998)
□ 台灣金融科技 / 數位券商官方報告
□ 個人資料保護法、資料匿名化與研究倫理相關文獻
```
