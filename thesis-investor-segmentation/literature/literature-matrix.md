# 文獻矩陣

論文：應用投資人行為分群與個人化推薦模型於數位券商基金投資服務之研究

最後更新：2026-04-14 | 文獻總數：26 篇（國際 16 篇 + 台灣本土 10 篇）

---

## 目錄

1. [A 類：投資人分群方法](#a-類投資人分群方法)（5 篇）
2. [B 類：個人化基金推薦系統](#b-類個人化基金推薦系統)（5 篇）
3. [C 類：FinTech 與數位券商應用](#c-類fintech-與數位券商應用)（3 篇）
4. [D 類：台灣本土相關研究（原有）](#d-類台灣本土相關研究)（4 篇）
5. [E 類：台灣推薦系統與顧客分群研究（新增）](#e-類台灣推薦系統與顧客分群研究)（4 篇）
6. [F 類：台灣機器人理財與數位投資行為（新增）](#f-類台灣機器人理財robo-advisor與數位投資行為)（3 篇）
7. [G 類：台灣共同基金投資人行為（新增）](#g-類台灣共同基金投資人行為與風險偏好)（4 篇）
8. [研究缺口彙整](#研究缺口彙整)
9. [建議引用順序](#建議引用順序)
10. [待補充文獻](#待補充文獻建議繼續搜尋)

---

## A 類：投資人分群方法

| # | 論文標題 | 作者 | 年份 | 期刊／來源 | 核心方法 | 本研究關聯 | 連結 |
|---|---------|------|------|-----------|---------|-----------|------|
| A1 | RFM-Net: A Convolutional Neural Network for Customer Segment Classification | — | 2026 | *Applied Sciences* (MDPI) | CNN + RFM 特徵分類；準確率 94.33% | 分群方法比較基準；RFM 特徵設計參考 | [DOI 10.3390/app16052223](https://www.mdpi.com/2076-3417/16/5/2223) |
| A2 | Artificial Intelligence-Driven CLV Forecasting: Integrating RFM Analysis with ML for Strategic Customer Retention | Akter, J.; Roy, A.; Rahman, S.; Mohona, S.; Ara, J. | 2025 | *JCSTS* | K-means++ + XGBoost + AHP 加權 RFM；動態 CLV 計算 | 特徵加權設計；K-means++ 應用 | [DOI 10.32996/jcsts.2025.7.1.18](https://www.researchgate.net/publication/389495515_Artificial_Intelligence-Driven_Customer_Lifetime_Value_CLV_Forecasting_Integrating_RFM_Analysis_with_Machine_Learning_for_Strategic_Customer_Retention) |
| A3 | Enhancing Customer Repurchase Prediction: Integrating Classification Algorithms with RFM Analysis for Precision and Actionable Insights | — | 2025 | *ScienceDirect* | RFM + 分類演算法；10-fold 交叉驗證 | 模型評估設計；驗證方法參考 | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0970389625000266) |
| A4 | Unlocking High-Value Football Fans: Unsupervised ML for Customer Segmentation and Lifetime Value | — | 2024 | *Frontiers in Sports and Active Living* | AHP 加權 RFM + K-means；識別 8 個群體 | 無監督分群流程；群體命名方法 | [DOI 10.3389/fspor.2024.1362489](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2024.1362489/full) |
| A5 | 以 RFM 模型結合群集分析建立顧客分群暨商品推薦之研究 | — | 2022 | 東海大學碩士論文 | RFM + 群集分析 + 商品推薦完整流程；**台灣研究** | **最直接參考**：台灣碩士論文範本，研究設計可對照 | [臺博碩論文系統](https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?o=dnclcdr&s=id=%22110THU01026098%22.&searchmode=basic) |

---

## B 類：個人化基金推薦系統

| # | 論文標題 | 作者 | 年份 | 期刊／來源 | 核心方法 | 本研究關聯 | 連結 |
|---|---------|------|------|-----------|---------|-----------|------|
| B1 | Modeling Behavior Sequence for Personalized Fund Recommendation with Graphical Deep Collaborative Filtering (GraphDCF) | Chou, Y.-C.; Chen, C.-T.; Huang, S.-H. | 2022 | *Expert Systems with Applications*, Vol. 192 | 圖深度協同過濾；購買/贖回行為序列建圖；提升精準度 2.3% | 推薦模型核心文獻；行為序列特徵設計參考 | [DOI 10.1016/j.eswa.2021.116311](https://www.sciencedirect.com/science/article/abs/pii/S0957417421016122) |
| B2 | Personalized Fund Recommendation with Dynamic Utility Learning | Wei, J.; Liu, J. | 2025 | *Financial Innovation* | ε-greedy 演算法 + 增量學習；動態效用學習 | 推薦模型進階方法；動態偏好捕捉 | [DOI 10.1186/s40854-024-00720-5](https://link.springer.com/article/10.1186/s40854-024-00720-5) |
| B3 | Mutual Fund Recommendation System with Personalized Explanations | — | 2023 | ResearchGate | 知識圖譜 + ML；強調推薦可解釋性（XAI） | 推薦可解釋性設計；第五章實務建議參考 | [ResearchGate](https://www.researchgate.net/publication/367530626_MUTUAL_FUND_RECOMMENDATION_SYSTEM_WITH_PERSONALIZED_EXPLANATIONS) |
| B4 | A Hybrid Recommendation Engine for Fintech Platforms: Leveraging Behavioral Analytics for User Engagement and Conversion | — | 2025 | ResearchGate | 混合式推薦（CF + Content-based + DL）；行為分析提升轉換率 | 混合推薦架構設計；FinTech 場景應用 | [ResearchGate](https://www.researchgate.net/publication/394559448_A_Hybrid_Recommendation_Engine_for_Fintech_Platforms_Leveraging_Behavioral_Analytics_for_User_Engagement_and_Conversion) |
| B5 | FAR-Trans: An Investment Dataset for Financial Asset Recommendation | — | 2024 | *arXiv* | 首個公開金融資產推薦數據集；含資產定價與散戶交易紀錄 | 推薦模型評估基準；**可作為外部比較數據集** | [arXiv:2407.08692](https://arxiv.org/abs/2407.08692) |

---

## C 類：FinTech 與數位券商應用

| # | 論文標題 | 作者 | 年份 | 期刊／來源 | 核心貢獻 | 本研究關聯 | 連結 |
|---|---------|------|------|-----------|---------|-----------|------|
| C1 | FinTech, Investor Sophistication, and Financial Portfolio Choices | — | 2023 | *Review of Corporate Finance Studies* (Oxford) | 數位 FinTech 平台影響投資人成熟度與投資組合選擇 | Ch1 研究背景；數位券商對投資行為影響的理論支撐 | [Oxford RCFS](https://academic.oup.com/rcfs/article/12/4/834/7192186) |
| C2 | The Digital Transformation of Investment Behavior: A Systematic Review of Gambling Tendencies in Modern Financial Markets | — | 2024 | ResearchGate | 系統性文獻回顧；過度自信、損失趨避、羊群效應等行為偏差 | Ch2 文獻探討；投資人行為偏差理論框架 | [ResearchGate](https://www.researchgate.net/publication/396368845_The_digital_transformation_of_investment_behavior_a_systematic_review_of_gambling_tendencies_in_modern_financial_markets) |
| C3 | Artificial Intelligence in Capital Markets: Use Cases, Risks, and Challenges | IOSCO | 2023 | IOSCO 官方報告 | 監管角度 AI 在資本市場應用；Robo-Advisor、投資建議、資料偏差風險 | Ch1 背景；Ch5 研究限制與監管討論 | [IOSCO PDF](https://www.iosco.org/library/pubdocs/pdf/IOSCOPD788.pdf) |

---

## D 類：台灣本土相關研究

| # | 論文標題 | 作者 | 年份 | 來源 | 核心內容 | 本研究關聯 | 連結 |
|---|---------|------|------|------|---------|-----------|------|
| D1 | 投資人可否從券商推薦的股票獲利？ | — | — | 臺灣博碩士論文知識加值系統 | 台灣股市散戶是否能從券商推薦中獲利；事件研究法 | Ch2 文獻；台灣券商推薦效果研究脈絡 | [臺博碩](https://ndltd.ncl.edu.tw/handle/46963616466150231805) |
| D2 | 台灣股票市場散戶投資人電視頻道偏好與投資行為關係之研究 | — | — | 臺灣博碩士論文知識加值系統 | 媒體偏好影響投資性格與行為偏誤；人口統計 × 行為分析 | Ch2 文獻；投資人行為分群變數設計參考 | [臺博碩](https://ndltd.ncl.edu.tw/handle/b3agwt) |
| D3 | 券商推薦個股的資訊內涵之探討 | 徐楚雯 | 2019 | 國立臺灣科技大學碩士論文 | 券商推薦對股價影響；公司規模、股價動能、外資持股等影響因素 | Ch2 文獻；推薦資訊內涵討論 | [臺科大數位論文庫](https://etheses.lib.ntust.edu.tw/thesis/detail/5fbb589dce8828c2ef89fe78e80010e3/) |
| D4 | 網路關鍵字搜尋行為反映投資人情緒之研究 | — | 2023 | Airiti Library | Google 搜尋趨勢指數對股票報酬與市場波動的影響；作為投資人情緒代理指標 | Ch2 文獻；GA4 行為數據作為情緒代理的理論支撐 | [Airiti Library](https://www.airitilibrary.com/Article/Detail/U0002-1107202310513600) |

---

## 研究缺口彙整

根據上述 16 篇文獻，本研究的差異化貢獻可對應陳述如下：

| 研究缺口 | 現有研究 | 本研究如何填補 |
|---------|---------|--------------|
| **雙軌數據整合** | 多數研究僅使用交易資料（B1, B2）或僅使用行為資料 | 同時整合 GA4 使用者行為事件 + 基金交易紀錄，構建更豐富的特徵空間 |
| **台灣在地化場景** | 大多數推薦系統研究採用中國或全球數據（B1, B2, B5） | 聚焦台灣數位券商場景（好好證券），具在地化應用價值 |
| **行為特徵工程** | 推薦系統多以純交易序列為輸入（B1, B2） | 加入 GA4 網站行為事件（搜尋、頁面停留、點擊）作為補充特徵 |
| **比較實驗設計** | 少有研究明確比較「個人化推薦 vs. 熱門推薦」效果（B3, B4） | 明確設置熱門推薦為 Baseline，完整對照個人化推薦的增量效益 |

---

## 建議引用順序

---

## E 類：台灣推薦系統與顧客分群研究

> 本節為本次新增的台灣本土文獻，涵蓋推薦系統、RFM 分群行銷策略及協同過濾應用。

| # | 論文標題 | 作者 | 年份 | 來源 | 核心方法 | 本研究關聯 | 連結 |
|---|---------|------|------|------|---------|-----------|------|
| E1 | 個人化推薦系統、顧客購買意願與後續退貨行為之影響 | — | 2022 | 淡江大學碩士論文（臺博碩） | 電商個人化推薦對購買意願影響；大數據分析應用 | Ch2 文獻：推薦系統對用戶行為影響之台灣在地研究 | [臺博碩](https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?o=dnclcdr&s=id=%22110TKU05121038%22.&searchmode=basic) |
| E2 | 應用 RFM 模型制定顧客分群行銷策略之研究——以 A 保健食品公司為例 | — | 2020 | 台灣科技大學碩士論文（臺博碩） | RFM 模型 + 顧客分群 + 行銷策略制定；CRM 應用 | Ch2 文獻、Ch3：**台灣 RFM 分群行銷論文範本**，方法論可直接對照 | [臺博碩](https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?o=dnclcdr&s=id=%22109NTUS5121030%22.&searchmode=basic) |
| E3 | 基於用戶序列之協同過濾推薦 | — | — | 臺灣博碩士論文知識加值系統 | 使用者序列行為 + 協同過濾；推薦系統實作 | Ch2 文獻：台灣協同過濾推薦系統研究脈絡 | [臺博碩](https://ndltd.ncl.edu.tw/handle/3pake6) |
| E4 | 資料探勘分析於金融機構客戶關係經營之研究 | — | — | 台灣科技大學碩士論文 | 資料探勘（Data Mining）應用於金融機構 CRM；分群技術架構 | Ch2 文獻：金融業資料探勘應用台灣研究；Ch3 方法論支撐 | [台科大論文庫](https://etheses.lib.ntust.edu.tw/detail/5f04fdb7c1c54021a137ad835327d677/) |

---

## F 類：台灣機器人理財（Robo-Advisor）與數位投資行為

> 機器人理財是數位券商個人化服務的重要背景，與本研究的推薦機制直接相關。

| # | 論文標題 | 作者 | 年份 | 來源 | 核心內容 | 本研究關聯 | 連結 |
|---|---------|------|------|------|---------|-----------|------|
| F1 | 台灣投資人對於機器人理財行為意圖之研究 | 陳奕君 | 2020 | 國立政治大學碩士論文（Airiti Library） | 客戶—理財專員—銀行關係 × 個人資訊科技創新觀點；採用意圖影響因素 | Ch1 背景：台灣投資人對數位理財服務接受度；Ch2 文獻 | [Airiti Library](https://www.airitilibrary.com/Article/Detail/U0004-G0107351022) |
| F2 | 提升投資人使用機器人理財意願之研究 | — | — | 臺灣博碩士論文知識加值系統 | 機器人理財結合人類智慧；對理財新手的吸引力；科技接受模型（TAM） | Ch1 背景：台灣數位理財服務採用障礙；Ch2 文獻 | [臺博碩](http://ndltd.ncl.edu.tw/handle/dqk4c3) |
| F3 | 機器人理財服務是否可有效消除投資人行為偏誤 | — | 2019 | 國立臺北大學碩士論文（臺博碩） | 機器人理財 × 行為偏誤消除效果驗證；行為財務學應用 | Ch2 文獻：數位化服務對投資行為偏誤的影響；研究假設設計參考 | [臺博碩](https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?o=dnclcdr&s=id=%22108NTPU0121042%22.&searchmode=basic) |

---

## G 類：台灣共同基金投資人行為與風險偏好

> 本節補充台灣在地共同基金投資人行為研究，提供第二章文獻的本土理論基礎。

| # | 論文標題 | 作者 | 年份 | 來源 | 核心內容 | 本研究關聯 | 連結 |
|---|---------|------|------|------|---------|-----------|------|
| G1 | 共同基金投資人投資行為及風險偏好之研究 | — | 2009 | 臺博碩 / Airiti Library | 依風險程度將投資人分三群（保守、穩健、積極）；行為偏誤與商品適合度 | Ch2 文獻：**台灣基金投資人風險分群參考**；KYC 風險等級設計理論支撐 | [臺博碩](https://ndltd.ncl.edu.tw/handle/7msk6p) \| [Airiti](https://www.airitilibrary.com/Article/Detail/U0031-0207200917353049) |
| G2 | 台灣地區共同基金投資行為實證研究 | 鄭芳盈 | 2007 | Airiti Library | BPN + CART 分類模型；依性別、教育、風險偏好分群；投資行為預測準確率 70%+ | Ch2 文獻：台灣基金投資人行為分類的早期實證研究；方法論演進參照 | [Airiti Library](https://www.airitilibrary.com/Article/Detail?DocID=U0006-0908200717040800) |
| G3 | 基金投資人是否存在現狀偏誤：來自台灣之證據 | — | — | 臺灣博碩士論文知識加值系統 | 現狀偏誤（Status Quo Bias）在台灣基金市場的實證；基金流量分析 | Ch2 文獻：台灣投資人行為偏誤類型；有助解釋分群結果中的非理性行為 | [臺博碩](https://ndltd.ncl.edu.tw/handle/bx5udf) |
| G4 | 市場狀態與基金投資人投資行為之探討 | — | — | 臺灣博碩士論文知識加值系統 | 不同市場狀態下台灣基金投資人申購與贖回行為模式差異 | Ch2 文獻：外部市場環境對投資行為分群的影響；可作為研究限制討論 | [臺博碩](https://ndltd.ncl.edu.tw/r/42769455951077663518) |

```
Ch1 緒論（研究背景）：C1, C2, C3, F1, F2
Ch2 文獻探討：
  2.1 投資人行為分析：C2, D2, D4, G3, G4, F3
  2.2 投資人分群方法：A1, A2, A3, A4, A5, E2, G1, G2
  2.3 推薦系統：B1, B2, B3, B4, B5, E1, E3
  2.4 金融科技與數位券商（台灣）：C1, C3, D1, D3, F1, F2, F3
  2.5 資料探勘與金融應用：E4, G2
Ch3 研究方法：A1, A2, B1, B2, E2
Ch4 實驗結果：B5（外部比較數據集）
Ch5 結論與建議：C3（監管討論）, F1, F2（台灣數位投資服務應用建議）
```

---

## 待補充文獻（建議繼續搜尋）

以下類型的文獻建議後續補充，以達到 **30 篇以上**的學術水準（目前 26 篇，還需 4+ 篇）：

```
□ 冷啟動問題（Cold-start problem）相關研究（推薦系統領域）
□ 協同過濾評估指標（Precision@K, NDCG）的方法論論文
□ 台灣金融科技發展近況報告（金管會年報、金融監理沙盒相關）
□ 個人資料保護法與研究倫理相關文獻（論文第5章研究限制必備）
□ K-means 最佳分群數選擇方法（Elbow Method, Silhouette Score）原始論文
□ 台灣電子商務平台 RFM 分析應用（2021–2024 年新研究）
□ 數位金融用戶體驗（UX）與投資決策關係——台灣研究
```
