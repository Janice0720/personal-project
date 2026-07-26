# Phase 1 文件閱讀順序與閱讀目標

## 建議閱讀順序總覽

| 順序 | 文件 | 閱讀目標 | 建議花費心力 |
|---:|---|---|---|
| 1 | `proposal/phase1/proposal-draft-master.md` | 先掌握 Proposal 主線：研究定位、第二章架構、研究缺口與研究貢獻。 | 最高 |
| 2 | `proposal/phase1/consistency-check-literature-vs-proposal.md` | 確認目前文件哪裡一致、哪裡需要修正，避免後續引用混亂。 | 高 |
| 3 | `literature/literature-matrix.md` | 掌握已整併的 Phase 1 主要文獻矩陣、核心閱讀順序與研究缺口對應。 | 高 |
| 4 | `literature/phase1/phase1-literature-matrix-2026-06-22.md` | 需要回查 Research Assistant 原始補強紀錄時再看；一般閱讀不必優先讀。 | 低 |
| 5 | `thesis/chapters/chapter-02-literature-review/01-investor-behavior-segmentation-rfm.md` | 深讀第二章前三類：投資人行為、顧客分群、RFM / 機器學習分群。 | 中 |
| 6 | `thesis/chapters/chapter-02-literature-review/02-recommendation-fintech-digital-brokerage.md` | 深讀第二章後三類：推薦系統、基金推薦、FinTech / 數位券商。 | 中 |
| 7 | `proposal/phase1/02-research-gap-analysis.md` | 若要加強研究缺口論述，再讀這份細節素材。 | 中 |
| 8 | `proposal/phase1/03-research-contribution-claims.md` | 若要加強研究貢獻與口試說法，再讀這份細節素材。 | 中 |

---

## 第一輪：先抓主線，不要急著看所有細節

### 讀：`proposal/phase1/proposal-draft-master.md`

你的目標不是逐字修改，而是回答四個問題：

1. 我的研究到底要解決什麼問題？
2. 為什麼「GA4 行為資料 + 基金交易資料」值得研究？
3. 為什麼需要「投資人分群」？
4. 為什麼要跟「熱門推薦 baseline」比較？

讀完後，你應該能用 3–5 句話說出研究主軸：

> 本研究聚焦台灣數位券商基金投資服務，整合網站行為資料與基金交易資料，建立投資人行為分群，並比較個人化推薦與熱門推薦 baseline 的效果，以補足既有研究在雙軌資料整合、台灣數位券商場域與基金推薦實證上的不足。

---

## 第二輪：檢查文獻與 Proposal 是否接得起來

### 讀：`proposal/phase1/consistency-check-literature-vs-proposal.md`

你的目標是知道目前最大風險：

- 不是研究方向錯。
- 文獻矩陣已完成第一輪整併，但來源查證、正式引用格式與部分待查證文獻仍未完成。

你要特別注意：

1. 正式閱讀與引用應以 `literature/literature-matrix.md` 整合版為主。
2. `phase1-literature-matrix-2026-06-22.md` 只作原始補強紀錄，不再作主要閱讀清單。
3. 待查證來源不能直接放進正式引用。
4. Proposal 草稿裡的「引用提示」後續要改成正式作者年份。

---

## 第三輪：回到文獻矩陣建立證據基礎

### 先讀：`literature/literature-matrix.md`

目標：掌握目前整合版文獻矩陣如何支撐你的研究。

建議閱讀重點：

- A 類：支撐 RFM、K-means、分群方法。
- B 類：支撐基金推薦與個人化推薦模型。
- C 類：支撐 FinTech、AI 監理與數位券商背景。
- E / F / G 類：支撐台灣本土文獻與在地研究缺口。

### 原始補強紀錄：`literature/phase1/phase1-literature-matrix-2026-06-22.md`

目標：只有在需要回查 Research Assistant 原始搜尋結果、來源連結或補強矩陣的舊編號時才閱讀。正式閱讀與引用請優先使用 `literature/literature-matrix.md`。

---

## 第四輪：補第二章細節

### 讀：`thesis/chapters/chapter-02-literature-review/01-investor-behavior-segmentation-rfm.md`

目標：準備第二章前半部。

讀完你要能回答：

1. 投資人行為為什麼需要分群？
2. 傳統顧客分群與投資人分群差在哪？
3. RFM 為什麼可以轉換成基金投資服務的行為特徵？
4. 為什麼不能只用交易資料，也要納入網站行為資料？

### 讀：`thesis/chapters/chapter-02-literature-review/02-recommendation-fintech-digital-brokerage.md`

目標：準備第二章後半部。

讀完你要能回答：

1. 推薦系統有哪些基本方法？
2. 基金推薦和一般電商推薦差在哪？
3. 為什麼金融商品推薦要考慮風險、適合度與投資人保護？
4. 為什麼台灣數位券商場域是合理研究場景？

---

## 第五輪：準備 Proposal 口試或與指導教授討論

### 讀：`proposal/phase1/02-research-gap-analysis.md`

目標：把「為什麼這題值得做」講清楚。

你應該能說出五個缺口：

1. 既有研究偏重交易資料或靜態屬性。
2. 較少整合網站行為與交易資料。
3. 台灣數位券商場域實證不足。
4. 基金推薦需處理金融商品特殊性。
5. 個人化推薦需要與熱門推薦 baseline 比較。

### 讀：`proposal/phase1/03-research-contribution-claims.md`

目標：把「這篇論文完成後貢獻在哪」講清楚。

你應該能分成四類說明：

1. 理論 / 文獻貢獻。
2. 方法貢獻。
3. 實務應用貢獻。
4. 台灣數位券商 / 基金投資服務場域貢獻。

---

## 你目前最重要的閱讀目標

不是把所有文件一次讀完，而是先建立三層理解：

1. **一句話研究定位**：這篇論文到底在做什麼。
2. **五個研究缺口**：為什麼值得做。
3. **三個方法關鍵字**：分群、推薦、baseline 比較。

如果你只能先讀 30 分鐘，建議只讀：

1. `proposal/phase1/proposal-draft-master.md`
2. `proposal/phase1/consistency-check-literature-vs-proposal.md`
3. `literature/literature-matrix.md` 的「建議核心閱讀順序」
