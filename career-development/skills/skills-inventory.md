# 技能盤點

> 最後更新：2026-05-19  
> 目標職涯方向：2027 年底前應徵 Microsoft，優先職位為 Cloud Solution Architect - Data、Business Program Manager、Program Manager、Product Analyst / Data Analyst；長期目標為 3–5 年內應徵 Google。  
> 評估基準：以 Microsoft / Google 所需的 Product、Data、Cloud、Program Management、英文溝通能力為主。

## 評分說明

- **熟練度**：1（初學）～ 5（可獨立交付／可教他人）
- **求職相關度**：高 / 中 / 低（對目標職缺的匹配程度）

---

## 核心技能

| 技能 | 熟練度 | 相關度 | 可舉例／證據 | 需加強 |
|------|--------|--------|--------------|--------|
| SQL / 資料查詢 | 3.5 | 高 | 已使用 MySQL、BigQuery 查詢 GA4、交易、庫存、憑證、用戶資料；熟悉 join、filter、group by、去重邏輯；曾處理 `user_pseudo_id`、`ga_session_id`、`event_timestamp`、`event_name` 去重邏輯 | 加強 window function、CTE、cohort、retention、funnel、rolling metrics、面試型 SQL 題 |
| BigQuery / GA4 資料分析 | 4 | 高 | 熟悉 GA4 events_*、event_params 解析、page_location、content_group、px_account_code、ga_session_id 等欄位；能分析網站行為、活動頁導流、基金詳情頁行為 | 加強大型資料效能優化、標準化 event tracking framework、產品指標層設計 |
| Power BI / BI 報表 | 4 | 高 | 已整合 MySQL、BigQuery、Power BI；建立網站數據、用戶行為、交易與庫存分析報表；處理 gateway、refresh、資料大小限制等問題 | 加強 Power BI Service、semantic model、DAX 進階、Microsoft Fabric 整合 |
| Product Analytics | 3.5 | 高 | 分析開戶流程、基金申購流程、活動頁導流、CRM segmentation、用戶交易狀態與庫存報酬標籤 | 加強 activation、retention、churn、LTV、north star metric、A/B testing、product case 面試 |
| User Segmentation / CRM 分群 | 4 | 高 | 已規劃交易新近度、首購潛力客、定期定額客、流失風險客、庫存損益標籤等用戶分群 | 加強模型化分群方法、RFM、clustering、推薦系統、個人化行銷實驗 |
| Funnel Analysis | 3.5 | 高 | 已分析開戶、申購、活動頁、基金詳情頁與後續頁面導流 | 加強標準 funnel metric、drop-off diagnosis、conversion experiment design |
| PM 規格撰寫 / 需求文件 | 4 | 高 | 已撰寫前台 / 後台規格，包含線上變更基本資料、TISA 條款、後台產品流程、基金資料維護模組等 | 加強大型科技公司 PRD / RFC / Program brief 寫法、英文文件能力 |
| 後台產品管理 | 3.5 | 中高 | 參與開戶審核自動化、交易紀錄查詢、基金資料維護、帳務 / 名單下載、資料交換流程 | 加強產品 roadmap、優先序判斷、使用者需求驗證、系統架構溝通 |
| ETL / 資料驗證 | 3.5 | 高 | 參與基金淨值來源整合、用戶庫存單位數對帳、集保 / 華南資料交換、資料異常排查 | 加強 Data Engineering、Airflow / dbt 概念、Data Factory、資料品質監控 |
| MongoDB / NoSQL 概念 | 2.5 | 中 | 了解 MongoDB aggregation、lookup、基金淨值資料來源整合邏輯，曾處理 string date 轉換錯誤 | 加強 aggregation pipeline、索引、效能、資料建模 |
| Python | 1.5 | 高 | 目前為學習中，已規劃從基礎語法、pandas、資料清理開始補強 | 必須加強 pandas、numpy、API、JSON、資料分析專案、automation script |
| Statistics / 統計分析 | 2 | 高 | 有商業分析與指標判斷基礎，但尚未系統化應用於實驗設計 | 加強 hypothesis testing、p-value、confidence interval、regression、sample size |
| A/B Testing / Experimentation | 1.5 | 高 | 目前具備產品改善與 campaign 分析經驗，但尚未完整設計正式實驗 | 加強實驗假設、對照組 / 實驗組、primary metric、guardrail metric、結果判讀 |
| Azure / Cloud 基礎 | 1.5 | 高 | 目前主要熟悉 BigQuery、Power BI、資料庫與 BI，Azure 尚未系統性學習 | 準備 AZ-900、DP-900；學 Azure SQL、Data Factory、Data Lake、Fabric |
| Data Engineering / Data Pipeline | 2 | 高 | 已理解資料從網站事件、資料庫、ETL 到 BI 的流程，但較少親手建 pipeline | 加強 batch / streaming、ETL / ELT、lakehouse、warehouse、data governance |
| Cloud Solution Architecture | 1.5 | 高 | 有資料流與系統流程理解，但尚未具備架構師層級的 solution design 能力 | 加強 architecture diagram、scalability、security、monitoring、customer scenario design |
| API / 系統流程理解 | 2.5 | 中高 | 能與工程師討論資料流、事件追蹤、前後台流程與資料交換 | 加強 REST API、HTTP、JSON、auth、frontend/backend flow、system design basics |
| 金融科技 Domain Knowledge | 4 | 中高 | 熟悉基金交易、開戶、定期定額、集保、TDCC、基金憑證、交易對帳、TISA 議題 | 將金融 domain 轉化為 Microsoft / Google 可理解的 customer scenario 與 business impact |
| SEO / Growth / Campaign Analysis | 3.5 | 中 | 曾分析 PMax、GSC、活動頁、TISA 專題頁、內容導流、campaign performance | 若目標轉 Product/Data，可保留為加分項；需避免履歷過度偏行銷 |
| Recommendation / Personalization | 2 | 高 | 碩論方向可能聚焦投資人分群、個人化推薦、基金推薦 | 加強推薦系統基礎、Precision@K、Recall@K、MAP、協同過濾、分群模型 |

---

## 工具與平台

| 工具 | 熟練度 | 相關度 | 可舉例／證據 | 需加強 |
|------|--------|--------|--------------|--------|
| Google Analytics 4 | 4 | 高 | 熟悉事件追蹤、頁面行為、活動頁導流、content_group、event_params、使用者行為分析 | 加強完整 tracking governance、GA4 → BigQuery 資料模型最佳化 |
| BigQuery | 3.5 | 高 | 查詢 GA4 events_*、拆解 event_params、串接 Power BI、分析 px_account_code 與使用者行為 | 加強查詢優化、partition、cluster、cost control、window function |
| Power BI Desktop | 4 | 高 | 建立多來源報表、交易 / 庫存 / 網站分析、處理資料模型與 DAX 邏輯 | 加強 DAX 進階、資料模型最佳化、RLS、performance tuning |
| Power BI Service / Gateway | 3 | 高 | 已處理 gateway 安裝、排程 refresh、MySQL / BigQuery 連線問題 | 加強 service deployment、workspace governance、gateway mapping、Fabric 整合 |
| MySQL | 3.5 | 高 | 查詢 tenant、asset_order、tenant_inventory_info 等核心資料表 | 加強 query optimization、index 基礎、stored procedure 概念 |
| MongoDB | 2.5 | 中 | 理解基金淨值資料 lookup、aggregation 與 createDate / DayEndDate 轉換問題 | 加強 aggregation、資料建模、效能分析 |
| Looker Studio / Looker | 2.5 | 中 | 有網站分析與 dashboard 概念，理解 Looker filtering / path regex 使用情境 | 加強 LookML / semantic layer 概念 |
| Google Search Console | 3 | 中 | 追蹤 TISA 文章索引、SEO 搜尋結果、sitemap 狀態 | 若主攻 Data / Cloud，可作為 growth analytics 加分項 |
| Excel / Google Sheets | 4 | 中 | 常用於資料整理、名單、分析輔助、報表前處理 | 加強自動化與 Python / BI 取代重複人工流程 |
| Notion / Notion AI | 3.5 | 中 | 規劃年度目標、專案管理、學習計畫、研究進度管理 | 加強 Notion database、formula、project dashboard 設計 |
| Cursor AI | 3 | 中 | 用於規格轉靜態 HTML、AI 輔助開發與文件撰寫流程 | 加強 AI agent workflow、repo-based development、prompt systemization |
| Git / GitHub | 2 | 中高 | 有基本概念，未來作品集需要使用 | 加強 Git flow、README、portfolio repo、commit discipline |
| Python / Jupyter Notebook | 1.5 | 高 | 目前需要建立資料分析作品集 | 加強 notebook workflow、pandas project、visualization |
| Microsoft Azure | 1 | 高 | 目標職位需要，尚未系統學習 | AZ-900、DP-900、Azure SQL、Data Factory、Data Lake、Fabric |
| Microsoft Fabric | 1 | 高 | 目標 CSA Data / Power BI Data Analyst 加分工具 | 學 lakehouse、warehouse、semantic model、Power BI integration |
| Azure Data Factory | 1 | 高 | CSA Data / Data Engineer 相關 | 學資料匯入、pipeline、trigger、monitoring |
| Azure SQL / Synapse / Databricks | 1 | 高 | CSA Data 相關核心技術 | 建立基礎概念與至少一個作品集 demo |
| Microsoft 365 / Copilot | 1.5 | 中高 | Sales Specialist - Workforce AI / AI solution 相關 | 學 Copilot、Copilot Studio、Teams、Viva、Power Platform 基礎 |
| LinkedIn | 2.5 | 高 | 需要經營為 Microsoft / Google recruiter 可讀 profile | 加強英文 About、Headline、Featured Projects、定期貼文 |

---

## 軟技能

| 項目 | 自我評估 | 面試可講的故事 |
|------|----------|----------------|
| 跨部門溝通 | 4 / 5。能在 PM、工程、行銷、客服、基金事務、主管之間溝通需求與資料問題。優勢是能理解不同角色的語言並協助對齊。 | 1. GA4 / BigQuery 事件追蹤與網站行為分析，需與工程、行銷、產品共同定義事件與指標。<br>2. 開戶 / 交易 / 基金資料維護等後台功能，需與工程、客服、基金事務共同確認需求與驗收。<br>3. 集保 / 華南資料交換與對帳問題，需協調資料、後台、帳務與營運需求。 |
| 需求拆解與優先序 | 3.5 / 5。能將模糊需求拆解為資料表、追蹤事件、功能規格、報表指標，但仍需加強大型科技公司的 prioritization framework。 | 1. 將「想知道活動是否帶動開戶」拆成活動頁流量、後續頁面、開戶流程、轉換率等分析問題。<br>2. 將「用戶分群」拆成交易狀態、交易新近度、定期定額、庫存損益等標籤邏輯。<br>3. 將後台功能需求轉換成 PM spec、欄位邏輯、驗收條件與 QA 檢核項。 |
| 數據解讀與決策 | 4 / 5。能從 GA4、交易、庫存、活動頁與 CRM 資料中提出洞察，並支援行銷與產品決策。 | 1. 透過 GA4 分析 TISA / 活動頁使用者行為與後續導流。<br>2. 透過交易資料設計用戶活躍度、首購潛力、定期定額、流失風險等標籤。<br>3. 透過庫存與交易資料支援基金平台營運與用戶分群策略。 |
| 結構化思考 | 3.5 / 5。能用表格、規格文件、資料邏輯拆解問題，但需要更熟練 MECE、root cause、case interview 架構。 | 1. Power BI / SQL 問題排查時，能分層確認資料來源、連線、轉換、模型、報表與 gateway。<br>2. 建立 PM spec 時，能拆分範圍、目標、anti-goals、流程、欄位、例外情境。 |
| Ownership / 主動性 | 4 / 5。經常主動發現資料、流程、追蹤、報表問題並推動改善。 | 1. 主動建立網站事件追蹤與分析框架。<br>2. 主動設計交易與活躍度標籤，支援 CRM 與產品分析。<br>3. 主動排查 Power BI / Gateway / BigQuery 連線與 refresh 問題。 |
| Stakeholder Management | 3.5 / 5。已有內部 stakeholder 協作經驗，但需要補強 enterprise / customer-facing 場景。 | 1. 向總經理、副總、產品經理匯報網站電子商務功能與使用情況。<br>2. 與工程師討論事件追蹤、資料表邏輯、後台功能與驗收條件。<br>3. 與行銷單位討論活動成效、SEO、PMax 與 CRM 名單。 |
| 英文溝通 | 2 / 5。可閱讀技術資料與準備英文履歷，但英文口說、英文面試、英文簡報仍是主要缺口。 | 可準備英文版故事：GA4 tracking framework、Power BI dashboard、CRM segmentation、product analytics case。需持續練習 1 分鐘自介、3 分鐘專案介紹、behavioral answer。 |
| 學習能力 / Growth Mindset | 4 / 5。邊工作邊讀研究所，持續學習 Python、資料分析、PM、AI 工具與職涯轉型。 | 1. 錄取資訊與決策科學研究所在職專班。<br>2. 一邊工作一邊補 Python、資料分析、論文研究與職涯準備。<br>3. 主動研究 Microsoft / Google 職缺並倒推能力缺口。 |
| 文件化能力 | 4 / 5。擅長把流程、規格、分析、計畫整理成文件，適合 PM / Program Manager 路線。 | 1. 撰寫前後台規格文件。<br>2. 整理 TISA 條款、content-api 協議文件。<br>3. 建立職涯規劃、學習計畫與 AI agent brief。 |

---

## 技能缺口與學習計畫

| 缺口 | 為何重要 | 計畫 | 目標完成日 |
|------|----------|------|------------|
| Python / pandas | Microsoft Product/Data Analyst、Google Data 相關職位都需要能獨立處理資料，而不只依賴 BI 工具 | 2026.05–2026.07 完成 Python 基礎；2026.07–2026.09 完成 pandas 資料分析；2027.02 前完成一個 end-to-end Python 分析作品 | 2027-02-28 |
| SQL 面試能力 | 科技公司 Data / Product Analyst 面試常考 SQL，需從工作查詢升級為面試解題能力 | 每週 3–5 題 LeetCode SQL / DataLemur；重點練 window function、cohort、retention、funnel、rolling metrics | 2027-05-31 |
| Azure Fundamentals | Microsoft 目標職缺需要 Azure 語言，Cloud Solution Architect - Data 更是核心能力 | 2026.08 前學完 AZ-900 Microsoft Learn；完成筆記與基礎架構圖練習 | 2026-08-31 |
| Azure Data / DP-900 | CSA Data / Data & AI / Fabric 相關職缺需要 Azure Data 基礎 | 2026.09–2026.10 學 DP-900；理解 relational、non-relational、analytics workload、Azure SQL、Data Lake | 2026-10-31 |
| Microsoft Fabric / Power BI Service | Microsoft Data / BI / CSA Data 職缺加分，能放大既有 Power BI 優勢 | 2026.11–2026.12 學 Fabric、Lakehouse、Warehouse、Semantic Model；做一個 Fabric / Power BI 架構作品 | 2026-12-31 |
| Data Engineering / Pipeline | CSA Data 需要不只會分析，還要能理解資料平台如何建置與維運 | 學 ETL / ELT、Data Factory、Data Lake、batch / streaming、monitoring；完成 Data Pipeline / BI case | 2027-03-31 |
| Statistics | Google / Microsoft Data role 需要統計推論與實驗判讀能力 | 2026.09 前完成 hypothesis testing、p-value、confidence interval、regression basics | 2026-09-30 |
| A/B Testing | 大型科技公司重視 experimentation mindset，Product/Data role 必備 | 2026.09–2026.11 完成一份 A/B testing case，包含假設、實驗組、對照組、指標、風險 | 2026-11-30 |
| Product Metrics | 要從 dashboard maker 升級為能影響產品決策的人 | 2026.07 起建立 activation、retention、churn、conversion、DAU/MAU、LTV、north star metric 筆記；套用到 FundSwap 案例 | 2026-12-31 |
| Program Management | Microsoft Business Program Manager / Program Manager 需要 scope、risk、dependency、timeline 能力 | 2026.10 起整理專案案例；練習寫 program brief、risk log、dependency map、launch plan | 2027-03-31 |
| Cloud Solution Architecture | Cloud Solution Architect - Data 需要能設計解決方案並向客戶說明 trade-off | 2027.03–2027.05 完成金融平台 Azure Data Platform 架構 case，包含架構圖、服務選型、安全與 business value | 2027-05-31 |
| 英文口說 / 面試 | Microsoft / Google 面試與工作環境需要英文表達，這可能是主要瓶頸 | 每週 2 次英文口說練習；2027.01 起練 behavioral；2027.04 起進行 mock interview | 2027-07-31 |
| 英文履歷 / LinkedIn | 需要讓 Microsoft recruiter 看懂你的國際科技人才定位 | 2026.12 完成英文履歷初版；2027.04 完成 LinkedIn 優化；依 CSA Data、PgM、Data Analyst 做不同版本 | 2027-04-30 |
| 作品集 | 轉職大型科技公司不能只有現職經歷，需要可展示成果 | 完成 3–5 個作品：Product Analytics、A/B Testing、Data Pipeline / BI、Azure Data Platform、碩論推薦系統 | 2027-07-31 |
| Customer-facing Consulting | CSA / Solution 類職缺需要面對客戶釐清需求與說明價值 | 練習 customer scenario、pain point discovery、ROI、solution proposal；用金融平台作為模擬客戶 | 2027-05-31 |
| System Design Basics | TPM / CSA Data 需要理解 API、資料流、系統限制與風險 | 2026.08–2026.10 學 REST API、HTTP、JSON、database、cache、queue、logging、monitoring | 2026-10-31 |
| Referral / Networking | Microsoft / Google 內推與弱連結有助於提高面試機會 | 2027.04 起整理內推素材；2027.05 起與 Microsoft、Appier、Shopee、LINE 相關人士建立連結 | 2027-07-31 |
