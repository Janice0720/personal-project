# literature/

本資料夾收錄論文「應用投資人行為分群與個人化推薦模型於數位券商基金投資服務之研究」的文獻管理檔案。

---

## 資料夾結構

```
literature/
├── README.md                  ← 本檔案
├── literature-matrix.md       ← 整合版文獻矩陣（主要維護檔，A–G 七類）
├── reading-summaries/         ← 論文正式引用文獻的精讀摘要（對應矩陣代號）
│   ├── A12-cheng-2010-rfm-som-adaptive-recommendation-reading-summary.md
│   ├── B2-wei-liu-2025-dynamic-utility-fund-recommendation-reading-summary.md
│   ├── B7-wu-li-2025-financial-product-recsys-slr-reading-summary.md
│   ├── E5-chen-2021-rfm-market-basket-ecommerce-segmentation-reading-summary.md
│   └── G1-wu-2008-mutual-fund-investor-behavior-risk-preference-reading-summary.md
└── class-readings/            ← 課堂參考文獻（未列入矩陣正式代號）
    ├── chiou-wei-2024-kl-km-reading-summary.md
    ├── chiou-wei-2024-kl-km-fund-recommendation-report.md
    ├── fundrecllm-2023-llm-fund-recommendation-reading-summary.md
    ├── hsu-2006-refined-rfm-som-customer-segmentation-reading-summary.md
    ├── ni-2025-cluster-analysis-financial-product-recsys-reading-summary.md
    └── wang-2025-ml-treasury-yield-forecasting-reading-summary.md
```

---

## 各檔案說明

### `literature-matrix.md`

整合版文獻矩陣，為本資料夾唯一正式維護的文獻清單。  
整合來源：原始 A–G 矩陣 ＋ Phase 1 補強矩陣（已合併，備份已刪除）。  
分七大類收錄約 40 筆文獻，含優先級、研究缺口對應、閱讀順序與待查證清單。

---

### `reading-summaries/`

對應 `literature-matrix.md` 中已精讀的正式文獻，檔名前綴為矩陣代號。

| 代號 | 論文 | 用途 |
|------|------|------|
| A12 | 鄭婕妤（2010）RFM ＋ SOM 適性化推薦 | A5 替代文獻；分群流程與混合式推薦設計參考 |
| B2 | Wei & Liu（2025）動態效用學習基金推薦 | 連接 GA4 行為序列與推薦的核心方法參考 |
| B7 | Wu & Li（2025）金融商品推薦系統 SLR | 領域全景地圖；第二章研究缺口定位依據 |
| E5 | 陳一慈（2021）RFM ＋購物籃分析 | E2 替代文獻；台灣 RFM 分群論文範本 |
| G1 | 吳忠義（2008）共同基金投資人風險偏好 | 台灣基金投資人風險屬性分群；KYC 等級依據 |

---

### `class-readings/`

課堂報告或補充閱讀文獻，未列入矩陣正式代號，不作為論文主要引用來源。

| 檔案 | 說明 |
|------|------|
| `chiou-wei-2024-kl-km-reading-summary.md` | KL 散度 ＋ K-medoids 基金推薦；精讀摘要 |
| `chiou-wei-2024-kl-km-fund-recommendation-report.md` | 同論文課堂報告投影片素材（配套） |
| `fundrecllm-2023-llm-fund-recommendation-reading-summary.md` | LLM 基金推薦框架；研究邊界說明參考 |
| `hsu-2006-refined-rfm-som-customer-segmentation-reading-summary.md` | 改良式 RFM ＋ SOM；指標正規化與客戶分層參考 |
| `ni-2025-cluster-analysis-financial-product-recsys-reading-summary.md` | 分群演算法比較地圖；方法選型決策依據 |
| `wang-2025-ml-treasury-yield-forecasting-reading-summary.md` | 機器學習預測模型比較；評估指標與可解釋性參考 |
