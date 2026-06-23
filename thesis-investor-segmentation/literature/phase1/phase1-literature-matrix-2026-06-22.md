# Phase 1 文獻矩陣補強：投資人行為分群與個人化基金推薦（2016–2026）

任務範圍：針對「應用投資人行為分群與個人化推薦模型於數位券商基金投資服務之研究」蒐集近 10 年相關學術文獻、產業/官方報告與方法論資料。

重要限制與查證狀態：
- 本次未取得使用者「目前已已有文獻清單」，因此「是否與既有文獻重複」只能標示為「待比對」。
- 臺灣博碩士論文知識加值系統（NDLTD）搜尋時出現驗證碼頁，無法進一步查核個別臺灣學位論文；已在缺口說明列為後續人工查證項。
- 下列文獻以可查證 DOI、出版社頁、arXiv、官方機構頁或可公開存取頁為優先；無法充分確認者未納入主矩陣，或於備註標示「待查證」。

## 一、文獻矩陣

| 編號 | 論文標題 | 作者 | 年份 | 來源 / 期刊 / 學校 | 研究主題分類 | 使用方法 | 資料類型 | 主要發現 | 與本論文關聯 | 可放章節 | 優先級 | 來源連結 |
|---:|---|---|---:|---|---|---|---|---|---|---|---|---|
| 1 | Modeling behavior sequence for personalized fund recommendation with graphical deep collaborative filtering | Yi-Ching Chou; Chiao-Ting Chen; Szu-Hao Huang | 2021/2022 | Expert Systems with Applications | 基金推薦、協同過濾、行為序列 | Graphical Deep Collaborative Filtering（GraphDCF / DECF 類）、客戶節點相似交易序列建圖 | 臺灣商業銀行真實基金交易資料 | 以交易序列與圖結構建模客戶相似性，GraphDCF 較 DCF、NCF 等方法更佳；Semantic Scholar 查得 DOI 與題名。 | 最接近本論文：基金、臺灣資料、交易行為、個人化推薦。可作核心對照與方法基礎。 | 第2章、第三章 | 高 | https://doi.org/10.1016/j.eswa.2021.116311 |
| 2 | Explainable mutual fund recommendation system developed based on knowledge graph embeddings | Pei-Ying Hsu; Chiao-Ting Chen; Chin Chou; Szu-Hao Huang | 2022 | Applied Intelligence, Springer | 可解釋基金推薦、知識圖譜 | Knowledge Graph Embedding、深度學習、可解釋推薦 | 共同基金交易紀錄 | 將客戶與基金特徵嵌入同一潛在空間，同時預測下月基金購買與產生解釋；強調金融推薦需提升信任。 | 可支撐「金融推薦不只看準確率，也需可解釋與信任」；適合比較推薦模型設計。 | 第2章、第三章 | 高 | https://doi.org/10.1007/s10489-021-03136-1 |
| 3 | Personalized fund recommendation with dynamic utility learning | Jiaxin Wei; Jia Liu | 2025 | Financial Innovation, Springer | 基金推薦、動態偏好學習 | Incremental utility learning、quadratic programming、ε-greedy exploration/exploitation | 基金產品點擊序列 / 模擬網頁互動資料 | 以顧客點擊序列動態更新效用函數，平衡探索與利用；適合數位平台即時推薦情境。 | 與 GA4 點擊/事件資料整合高度相關，可補強本論文「使用者數位行為資料」如何回饋推薦。 | 第2章、第三章 | 高 | https://doi.org/10.1186/s40854-024-00720-5 |
| 4 | A Systematic Literature Review of Financial Product Recommendation Systems | Di Wu; Xuhui Li | 2025 | Information, MDPI | 金融商品推薦系統綜述 | Systematic Literature Review；分析 2018–2024 年 65 篇研究 | 文獻資料 | 指出金融商品推薦具有多目標、寬特徵空間、時間敏感、多重互動行為等特性；未來方向包含 multi-behavior sequence recommendation 與 multi-task recommendation。 | 可作第2章總覽與研究缺口來源；幫助界定本論文相對於一般推薦系統的金融特殊性。 | 第2章、研究缺口 | 高 | https://doi.org/10.3390/info16030196 |
| 5 | Research on Personalized Financial Product Recommendation by Integrating Large Language Models and Graph Neural Networks | Yushang Zhao; Yike Peng; Dannier Li; Yuxin Yang; Chengrui Zhou; Jing Dong | 2025 | arXiv / ACM ICSECA 2025 | 金融商品推薦、LLM、GNN | LLM text embeddings + heterogeneous user-product graph + GNN message passing | 公開與真實金融資料集；文字評論與互動圖 | 整合文字語意與使用者-商品關係圖，較單獨 LLM 或 GNN 在 accuracy、recall、NDCG 表現更佳。 | 可放作最新技術趨勢；若本論文不使用 LLM，可用來說明進階方向與研究邊界。 | 第2章、研究缺口 | 中 | https://arxiv.org/abs/2506.05873 |
| 6 | A survey on recommendation systems for financial services | Sharaf et al. | 2022 | Multimedia Tools and Applications（由 Springer 2025 文獻引用） | 金融服務推薦綜述 | Survey | 文獻資料 | 綜整金融服務推薦方法；在 Wei & Liu 2025 的文獻回顧中被引用為金融推薦系統重要綜述。 | 可作推薦系統背景文獻，但仍需補 DOI/全文做精讀。 | 第2章 | 中 | 待查證：Springer 文獻引用為 Sharaf et al. 2022, Multimedia Tools Appl. 81(12):16761–16781 |
| 7 | Profiling investor behavior in the Malaysian derivatives market using K-means clustering | E. H. Tan; Yaman Hamed; Hanita Daud; Mohd Amirul Faiz Abdul Wahab; Ahmad Amirul Adlan Azhar; Sieow Yeek Tan | 2025 | Frontiers in Artificial Intelligence | 投資人行為分群、K-means | K-means、IHS transformation、decision tree validation | Bursa Malaysia 2022 年 FCPO/FKLI 超過 1,100 萬筆交易紀錄 | 分出 5 類衍生性商品投資人，包括高頻高風險虧損型、保守穩健成長型、高頻高收益型等；以決策樹驗證可解釋分群條件。 | 可支撐本論文「以交易行為特徵進行投資人分群」方法設計；雖非基金但金融交易行為相近。 | 第2章、第三章 | 高 | https://doi.org/10.3389/frai.2025.1640776 |
| 8 | Segmenting “digital investors”: evidence from the Italian equity crowdfunding market | Rosangela Feola; Massimiliano Vesci; Ezio Marinato; Roberto Parente | 2019 | Small Business Economics, Springer | 數位投資人分群、股權群眾募資 | 投資人分群 / 實證分析 | 義大利 equity crowdfunding 投資人資料 | 探討數位投資人特徵與群體差異；可作「digital investors」概念來源。 | 可支撐數位投資人分群背景，但商品型態與基金不同。 | 第2章 | 中 | https://doi.org/10.1007/s11187-019-00265-3 |
| 9 | A Preliminary Study of Fintech Industry: A Two-Stage Clustering Analysis for Customer Segmentation in the B2B Setting | A. Sheikh; T. Ghanbarpour; D. Gholamiangonabadi | 2019 | Journal of Business-to-Business Marketing | FinTech 客戶分群 | Two-stage clustering | FinTech B2B 客戶資料 | 以兩階段分群理解 FinTech 客戶差異；Semantic Scholar 顯示被引約 30 次。 | 可作 FinTech 分群方法參考，但 B2B 與投資人基金服務情境差異較大。 | 第2章 | 中 | https://doi.org/10.1080/1051712X.2019.1603420 |
| 10 | RFM ranking – An effective approach to customer segmentation | A. Joy Christy; A. Umamakeswari; L. Priyatharsini; A. Neyaa | 2021 | Journal of King Saud University - Computer and Information Sciences | RFM、客戶分群 | RFM analysis、K-means、Fuzzy C-Means、初始中心點改良 | 企業交易資料 | 以 RFM 衡量 recency/frequency/monetary，再用 K-means 與 Fuzzy C-Means 分群；比較迭代次數、緊密度與執行時間。 | 可直接支撐本論文若使用基金交易的 RFM 或類 RFM 特徵工程。 | 第2章、第三章 | 高 | https://doi.org/10.1016/j.jksuci.2018.09.004 |
| 11 | RFM model for customer purchase behavior using K-Means algorithm | Anitha; Patil R. P.（作者待查證） | 2021 | Journal of King Saud University - Computer and Information Sciences | RFM、K-means | RFM、K-means、Silhouette Coefficient | 零售交易資料 | 以 RFM 與 K-means 進行顧客購買行為分群，並用 Silhouette 驗證分群品質。 | 可補強分群品質評估指標設計；作者與完整書目需後續查證。 | 第三章 | 中 | https://www.sciencedirect.com/science/article/pii/S1319157819309802 |
| 12 | Tracking Customer Segments in Alternative Finance using time-evolving Cluster Analysis | Lennert Aerts | 2020 | Erasmus University Rotterdam Master Thesis | 替代金融、動態分群、K-prototypes | K-means、K-prototypes、GMM、DBSCAN、Agglomerative、cluster tracking | LendingClub P2P lending 資料 | 比較多種分群法追蹤金融客戶區隔隨時間變化；K-means、K-prototypes、GMM 較能平滑追蹤。 | 可支撐本論文若未來要做月/季分群穩定性分析；也支援混合型特徵使用 K-prototypes。 | 第三章、研究限制 | 中 | https://thesis.eur.nl/pub/52256/Aerts.pdf |
| 13 | Intuitive-K-prototypes: A mixed data clustering algorithm with improved prototype representation and attribute weights | 作者待補 | 2024 | Pattern Recognition, Elsevier | K-prototypes、混合型資料分群 | Intuitive-K-prototypes、attribute weighting、mixed data clustering | UCI 混合型資料集 | 改良 K-prototypes 對類別特徵中心表示與權重調整，提升混合資料分群效果。 | 若本論文同時使用 GA4 類別特徵、客戶屬性與交易數值特徵，K-prototypes 是合理方法候選。 | 第三章 | 中 | https://www.sciencedirect.com/science/article/pii/S0031320324008136 |
| 14 | Robo Advising and Investor Profiling | Raquel M. Gaspar; Madalena Oliveira | 2024 | FinTech, MDPI | 機器人理財、投資人風險分群 | Relative Risk Aversion、Mean-Variance Theory、Expected Utility Theory、Sharpe ratio | Riskalyze ETF portfolio / 歷史市場資料 | 主張 RRA 是較客觀的投資人 profiling 指標；比較 Riskalyze 與最適化投資組合，發現 robo 平台可能過度保守且透明度不足。 | 可支撐「投資人輪廓/風險屬性」與推薦適配；亦可放在研究缺口：平台風險分群透明度不足。 | 第2章、研究缺口 | 高 | https://doi.org/10.3390/fintech3010007 |
| 15 | Robo-advisors: A systematic literature review | Giovanni Cardillo; Helen Chiappini | 2024 | Finance Research Letters | 機器人理財綜述 | Systematic Literature Review | 2017–2022 robo-advisor 文獻 | 歸納 robo-advisor 研究流派：分類、行為、績效、演算法模型化，並提出後續研究問題。 | 可作數位投資服務與機器人理財背景；非基金推薦核心但可說明產業脈絡。 | 第2章 | 高 | https://doi.org/10.1016/j.frl.2024.105119 |
| 16 | Business Model of Sustainable Robo-Advisors: Empirical Insights for Practical Implementation | C.-D. Au; L. Klingenberger; M. Svoboda; E. Frère | 2021 | Sustainability, MDPI | 永續機器人理財、採用意願 | Logistic regression | 德國私人投資人問卷 N=305 | 年輕、有經驗、男性、成本意識與生態永續偏好等特徵與使用永續 robo-advisor 意願相關。 | 可支撐本論文個人化推薦可納入 ESG/價值觀偏好與人口/行為特徵。 | 第2章 | 中 | https://doi.org/10.3390/su132313009 |
| 17 | Robo-advisors and the financialization of lay investors | Gordon Kuo Siong Tan | 2020 | Geoforum | Robo-advisor、一般投資人、演算法透明度 | Qualitative / conceptual analysis | 新加坡 robo-advisor 與政策/平台脈絡 | 指出 robo-advisor 可能讓一般投資人被動化，且演算法不透明增加不確定性，亦可能削弱金融教育。 | 可支撐研究缺口：個人化推薦在金融情境需考量透明度、投資人理解與信任。 | 第2章、研究缺口 | 中 | https://doi.org/10.1016/j.geoforum.2020.09.004 |
| 18 | The use of artificial intelligence and machine learning by market intermediaries and asset managers | IOSCO Board | 2021 | IOSCO Final Report FR06/2021 | AI/ML 監理、資產管理、投資服務 | 官方報告、監理指引 | 市場中介與資產管理業調查/監理資料 | 提出六項 AI/ML 監理措施：治理與高階責任、測試監控、技能與挑戰、第三方管理、揭露、資料品質/偏誤等。 | 可作金融推薦模型治理、資料品質、模型監控與可解釋性的官方權威來源。 | 第2章、第三章、第五章限制 | 高 | https://www.iosco.org/library/pubdocs/pdf/IOSCOPD684.pdf |
| 19 | Enhancing Investors’ Trust: 2022 CFA Institute Investor Trust Study | CFA Institute | 2022 | CFA Institute | 投資人信任、科技與個人化 | 全球投資人調查 | 3,588 位零售投資人、976 位機構投資人，15 個市場 | 科技可作信任乘數；個人化與價值觀對齊有助於建立投資人信任；「people plus technology」是重要公式。 | 可支撐為何數位券商需做個人化推薦，而非只提供熱門排行。 | 第1章、第二章 | 高 | https://www.cfainstitute.org/sites/default/files/-/media/documents/article/Enhancing-Investors-Trust-Report_2022_Online.pdf |
| 20 | [GA4] Cohort exploration | Google Analytics Help | 2024–2026 持續更新 | Google 官方文件 | GA4 行為資料、cohort analysis | Cohort exploration；inclusion / return criteria；daily/weekly/monthly cohorts | GA4 device-level event/cohort data | GA4 cohort 可依 acquisition date、event、transaction、conversion 建立使用者群組；文件明確指出 User-ID 不納入 cohort exploration。 | 可支撐本論文 GA4 行為資料處理與限制；尤其是 event/cohort 與 User-ID 對接交易資料時需留意。 | 第三章、研究限制 | 高 | https://support.google.com/analytics/answer/9670133?hl=en |
| 21 | Segments in Google Analytics 4 / GA4 segment types | Google Analytics Help / GA4 教學來源 | 2024–2026 | Google / GA4 教學頁 | GA4 segment、user/session/event scope | User segment、session segment、event segment | GA4 event/session/user data | GA4 分群可用於探索分析，但與 Audiences、報表、廣告用途不同；user/session/event scope 會影響解釋。 | 可支撐 GA4 行為特徵工程：應區分使用者層、session 層與事件層，不可直接混用。 | 第三章 | 中 | https://support.google.com/analytics/answer/9304353 或需後續補官方 segment 文件 |
| 22 | Using RFM, AUM, and K-means clustering for customer segmentation | Uchechukwu Emmanuel / Cowrywise | 2025 | Metabase Community / Cowrywise 產業案例 | FinTech 客戶分群、RFM、AUM | RFM + AUM + K-means | 數位財富管理平台交易/資產資料 | 產業案例示範以 RFM、AUM 與 K-means 分群，用於個人化金融方案與用戶經營。 | 非學術來源，但與本論文數位券商/基金平台應用非常接近，可放產業背景或實務案例。 | 第1章、第二章 | 低 | https://www.metabase.com/community-posts/using-rfm-aum-and-k-means-clustering-customers-segmentation |

## 二、最適合放在第二章文獻探討的文獻

建議優先放入第二章的核心文獻：
1. 編號 4：Wu & Li (2025) — 金融商品推薦系統系統性文獻回顧，可作總覽與研究缺口。
2. 編號 1：Chou et al. (2021/2022) — 個人化基金推薦、臺灣金融資料，與本論文高度貼近。
3. 編號 2：Hsu et al. (2022) — 可解釋共同基金推薦，補強信任與可解釋性。
4. 編號 3：Wei & Liu (2025) — 動態效用學習與點擊序列，連接 GA4 行為資料。
5. 編號 10：Christy et al. (2021) — RFM + K-means 基礎文獻。
6. 編號 14、15、17：Robo-advisor / investor profiling / trust / transparency 脈絡。
7. 編號 18、19：IOSCO 與 CFA Institute 作為官方/專業機構報告，補監理與信任背景。

## 三、可支撐第三章研究方法的文獻

方法面建議引用：
- 分群特徵與演算法：編號 7、10、12、13。
  - 交易特徵：總交易次數、交易金額、報酬、ROI、持有天數、帳戶年資等可參考編號 7。
  - RFM：recency、frequency、monetary 可參考編號 10、11、22。
  - 混合型資料：若同時有數值與類別特徵，可參考 K-prototypes（編號 12、13）。
- 推薦模型：編號 1、2、3、5。
  - Baseline：熱門推薦、協同過濾、NCF、圖式協同過濾、知識圖譜、動態效用學習。
  - 評估指標：accuracy、recall、NDCG、點擊/購買轉換、與熱門推薦 baseline 比較。
- GA4 行為資料：編號 20、21。
  - 注意 GA4 user/session/event scope、cohort 限制、User-ID 串接交易資料問題。
- 模型治理：編號 18。
  - 可放資料品質、偏誤、模型監控、可解釋性、第三方/演算法治理。

## 四、可用來說明研究缺口的文獻

可形成以下研究缺口：
1. 金融商品推薦系統特殊性高：Wu & Li (2025) 指出金融推薦具有多目標、時間敏感、寬特徵空間、多重互動行為；一般推薦方法不能直接移植。
2. 共同基金推薦已有研究，但多偏向銀行交易資料或模型準確率：Chou et al. 與 Hsu et al. 雖有臺灣基金交易資料，但本論文可補「數位券商 GA4 行為 + 交易資料整合」。
3. 使用者數位行為資料與金融交易資料整合仍是缺口：Wei & Liu (2025) 使用 click sequence 展示動態學習方向，但 GA4 事件資料如何與基金交易轉換結合仍可深化。
4. 可解釋性與信任仍不足：Hsu et al.、Tan (2020)、IOSCO (2021)、CFA (2022) 都可支撐金融推薦不能只追求 accuracy。
5. 熱門推薦 baseline 的不足：Wei & Liu (2025) 提到傳統隨機或預定排名無法滿足個人化需求；CFA (2022) 亦指出個人化有助信任。
6. 臺灣數位券商與基金投資人情境的公開研究不足：NDLTD/Airiti 需人工補查；目前已查得最接近臺灣基金推薦的是 Chou/Hsu/Huang 系列研究，但「數位券商 + GA4 + 基金推薦」組合仍可定位為缺口。

## 五、可能與既有文獻重複的項目

因未提供目前已持有文獻清單，無法做完整去重。就本題高度相關性推測，以下很可能已在既有文獻或應優先比對：
- Chou et al. (2021/2022) GraphDCF 基金推薦。
- Hsu et al. (2022) 可解釋共同基金推薦。
- RFM + K-means 基礎文獻，如 Christy et al. (2021)。
- Robo-advisor systematic review，如 Cardillo & Chiappini (2024)。

建議下一步：請使用者提供目前文獻矩陣或 Zotero/EndNote 匯出，我可以進行去重、補 DOI、補 BibTeX 與依章節重排。

## 六、後續待補查清單

1. 臺灣博碩士論文知識加值系統：目前遇到驗證碼，需人工搜尋以下關鍵字：
   - 基金 推薦系統
   - 投資人 分群
   - 機器人理財
   - 數位券商
   - 金融商品 推薦
   - RFM 基金 / 投資
2. Airiti Library：需人工或機構權限查詢臺灣期刊與碩博士論文。
3. 金管會/證期局：目前一般搜尋只取得首頁，建議後續查「金融科技發展路徑圖」、「機器人理財」、「證券投資顧問事業以自動化工具提供證券投資顧問服務」等法規/新聞稿。
4. 若論文第三章確定採用 K-prototypes，需補 Huang (1998) 原始 K-prototypes 文獻與近年改良演算法文獻。
