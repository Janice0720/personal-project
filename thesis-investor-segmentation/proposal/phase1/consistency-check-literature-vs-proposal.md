# 文獻矩陣與 Proposal 草稿一致性檢查

## 檢查範圍

本次檢查以下文件：

1. `literature/literature-matrix.md`：原始文獻矩陣，採 A–G 分類，共 26 篇。
2. `literature/phase1/phase1-literature-matrix-2026-06-22.md`：Research Assistant 補強文獻矩陣，採 1–22 編號。
3. `proposal/phase1/proposal-draft-master.md`：Proposal 初稿主檔。
4. `proposal/phase1/04-phase1-literature-context-gap-final.md`：Phase 1 文獻脈絡與研究缺口整合稿。
5. `thesis/chapters/chapter-02-literature-review/01-investor-behavior-segmentation-rfm.md` 與 `02-recommendation-fintech-digital-brokerage.md`：第二章素材。

---

## 一致的部分

### 1. 研究主軸一致

文獻矩陣與 Proposal 草稿均指向同一個研究定位：

> 在台灣數位券商基金投資服務場域中，整合 GA4 / 網站行為資料與基金交易資料，建立投資人行為分群，並比較個人化基金推薦與熱門推薦 baseline 的效果。

這個主軸在文獻矩陣、研究缺口、研究貢獻與 Proposal 初稿中是一致的。

### 2. 六大文獻分類一致

Proposal 草稿的六大文獻分類，能對應到既有文獻矩陣：

| Proposal 分類 | 對應文獻矩陣 |
|---|---|
| 投資人行為與數位金融 | C、D、F、G 類 |
| 投資人／顧客分群方法 | A、E、G 類 |
| RFM 與機器學習分群 | A、E 類 |
| 個人化推薦系統 | B、E 類 |
| 基金／金融商品推薦 | B 類 + Phase 1 補強文獻 1–6 |
| FinTech 與數位券商應用 | C、D、F 類 + IOSCO / CFA 等補強來源 |

### 3. 研究缺口一致

目前五項研究缺口與文獻矩陣的支撐方向一致：

1. 既有研究偏重交易資料或靜態屬性。
2. 較少整合網站行為資料與基金交易資料。
3. 台灣數位券商基金投資服務場域實證不足。
4. 基金推薦需處理金融商品風險、適合度與投資人保護。
5. 需要與熱門推薦 / popularity-based baseline 做比較。

---

## 需要修正或統一的地方

### 1. 文獻編號系統不一致

目前有兩套編號：

- `literature/literature-matrix.md` 使用 A1–G4。
- `literature/phase1/phase1-literature-matrix-2026-06-22.md` 使用 1–22。

Proposal 初稿主要引用 A–G 類編號，但補強文獻矩陣使用數字編號。正式寫作前，建議建立一份「整合版文獻矩陣」，把補強文獻併入 A–G 分類，避免第二章出現兩套引用邏輯。

### 2. Research Assistant 補強矩陣的限制說明需更新

`phase1-literature-matrix-2026-06-22.md` 第 6 行寫到「未取得目前已有文獻清單」，但專案內其實已有 `literature/literature-matrix.md`。這不是內容錯誤，而是該 worker 執行時未讀到既有文獻矩陣。

正式使用時建議修正為：

> 本補強矩陣為在既有文獻矩陣之外補充近年金融商品推薦、基金推薦、RFM / 分群與 GA4 行為資料相關文獻；後續需與既有 A–G 分類文獻進行去重與整併。

### 3. 部分文獻有重複或同主題重疊

下列文獻在既有矩陣與補強矩陣中可能重疊，正式版需去重：

- GraphDCF / Chou et al. 2021/2022：既有 B1；補強矩陣編號 1。
- Dynamic Utility Learning / Wei & Liu 2025：既有 B2；補強矩陣編號 3。
- RFM + K-means：既有 A 類、E2；補強矩陣編號 10、11、22。
- Robo-advisor / investor profiling：既有 F 類；補強矩陣編號 14–17。
- IOSCO / AI in Capital Markets：既有 C3；補強矩陣編號 18。

### 4. 待查證來源需保留標記

補強矩陣中仍有「待查證」項目，例如 Sharaf et al. 2022、部分 ScienceDirect / Google Analytics segment 文件、NDLTD / Airiti 人工查證項目。這些可以先作為研究方向，但不建議在正式 proposal 中直接當成已確認引用。

---

## 結論

整體而言，Proposal 草稿與文獻矩陣在「研究主軸、文獻分類、研究缺口與方法方向」上是一致的；主要問題不是論點不一致，而是文獻管理層級需要統一。

正式進入 Proposal 初稿定稿前，建議下一步是：

1. 建立整合版文獻矩陣：把 A–G 分類與補強 1–22 編號合併。
2. 去除重複文獻。
3. 將 Proposal 內的引用提示改成統一格式，例如「作者（年份）」或 APA。
4. 保留未查證來源為「待補查」，不要放入正式引用清單。
