# Week 4：自動化與加強型評估事件——不寫程式也能追蹤的行為數據

本週正式進入第二階段「事件追蹤與參數實務」。我們將認識 GA4 的四大事件類別，重點掌握「自動收集事件」與「加強型評估事件」的運作機制，並在 GA4 後台完成加強型評估的設定與驗證，讓 MovieTribe 無需寫程式碼就能啟動五種以上的基礎行為追蹤。

## 目錄

- [1. 本週學習目標](#1-本週學習目標)
- [2. 前三週快速回顧](#2-前三週快速回顧)
- [3. 核心概念：四大事件類別金字塔](#3-核心概念四大事件類別金字塔)
  - [3.1 金字塔總覽與選用原則](#31-金字塔總覽與選用原則)
  - [3.2 自動收集事件](#32-自動收集事件)
  - [3.3 加強型評估事件](#33-加強型評估事件)
  - [3.4 建議事件與自訂事件](#34-建議事件與自訂事件)
- [4. 深入解析：加強型評估的六大事件](#4-深入解析加強型評估的六大事件)
  - [4.1 捲動 scroll](#41-捲動-scroll)
  - [4.2 外連點擊 click](#42-外連點擊-click)
  - [4.3 站內搜尋 view_search_results](#43-站內搜尋-view_search_results)
  - [4.4 影片參與 video_start / video_progress / video_complete](#44-影片參與-video_start--video_progress--video_complete)
  - [4.5 檔案下載 file_download](#45-檔案下載-file_download)
  - [4.6 表單互動 form_start / form_submit](#46-表單互動-form_start--form_submit)
- [5. 實作步驟](#5-實作步驟)
  - [5.1 確認與設定加強型評估](#51-確認與設定加強型評估)
  - [5.2 觀察即時報表中的事件流](#52-觀察即時報表中的事件流)
  - [5.3 使用 DebugView 進行深度驗證](#53-使用-debugview-進行深度驗證)
- [6. MovieTribe 具體應用情境](#6-movietribe-具體應用情境)
- [7. 本週任務](#7-本週任務)
- [8. FAQ — 常見問題](#8-faq--常見問題)
- [9. 參考資源](#9-參考資源)

---

## 1. 本週學習目標

完成本週課程後，你將能夠：

- 說明 GA4 四大事件類別的階層關係與各自適用時機
- 正確判斷一個追蹤需求應該用哪一類事件實現
- 在 GA4 後台完成加強型評估事件的啟用與細項設定
- 透過即時報表（Real-time Report）觀察事件觸發狀態
- 無需寫任何程式碼，為 MovieTribe 啟動至少 5 種基礎行為追蹤

---

## 2. 前三週快速回顧

| 週次 | 主題 | 你學到的核心能力 |
|------|------|------------------|
| Week 1 | GA4 環境搭建 | 建立 GA4 資源與 GTM 容器，完成基礎安裝，在即時報表看到數據流入 |
| Week 2 | 維度與指標 | 分辨維度（描述標籤）與指標（量化數值），理解範圍與高基數 |
| Week 3 | GTM 基礎 | 掌握代碼、觸發條件、變數三大組件的聯動關係，完成 Google 代碼發布 |

**本週的定位**：Week 1-3 幫你把「基礎建設」蓋好了，從 Week 4 開始，我們要讓這些基礎建設真正發揮功效——追蹤使用者的實際行為。

---

## 3. 核心概念：四大事件類別金字塔

### 3.1 金字塔總覽與選用原則

GA4 把所有可追蹤的事件分成四大類別，形成一個金字塔結構。越底層越「自動」，越上層越「客製」：

```
                    ▲
                   ╱ ╲
                  ╱自訂╲          ④ 自訂事件（Custom Events）
                 ╱事件  ╲            完全自己定義
                ╱────────╲
               ╱  建議    ╲       ③ 建議事件（Recommended Events）
              ╱  事件      ╲         Google 定好名稱與參數
             ╱──────────────╲
            ╱  加強型評估     ╲    ② 加強型評估事件（Enhanced Measurement）
           ╱  事件            ╲      開一個開關就能啟用
          ╱────────────────────╲
         ╱   自動收集事件        ╲ ① 自動收集事件（Automatically Collected）
        ╱  （GA4 裝好就有）       ╲    安裝完成就自動運作
       ╱────────────────────────╲
```

用餐廳類比來理解：

| 層級 | 餐廳類比 | 你需要做的事 |
|------|---------|-------------|
| ① 自動收集 | 餐廳自動供應的白開水和餐巾紙 | 什麼都不用做，坐下就有 |
| ② 加強型評估 | 菜單上已有的附餐飲料，勾選即可 | 在菜單上打勾（開關開啟） |
| ③ 建議事件 | 廚師推薦的特餐組合，有固定搭配 | 按推薦組合點餐（用 Google 建議的名稱與參數） |
| ④ 自訂事件 | 客製化餐點，想吃什麼都行 | 自己告訴廚師要什麼（自行定義事件名稱與參數） |

**選用原則：優先使用低層級的事件。** 越低層級越穩定、不容易出錯，且 Google 的報表和機器學習模型對這些事件有更好的支援。當你有新的追蹤需求時，依序問自己：

1. GA4 是否已自動收集？→ 是的話不需做任何設定
2. 加強型評估是否涵蓋？→ 確認開關已啟用即可
3. Google 有建議事件嗎？→ 用建議的名稱格式，透過 GTM 設定
4. 以上都不行？→ 建立自訂事件

### 3.2 自動收集事件（Automatically Collected Events）

只要正確安裝了 GA4，這些事件就會**自動產生**，不需要任何額外設定。就像人體的自動呼吸和心跳。

| 事件名稱 | 觸發時機 | 攜帶的關鍵參數 |
|----------|---------|---------------|
| `page_view` | 每次頁面載入或路由切換 | `page_location`、`page_referrer` |
| `session_start` | 使用者開始新的工作階段（閒置超過 30 分鐘後重新活動） | `ga_session_id`、`ga_session_number` |
| `first_visit` | 使用者首次造訪網站（依 Cookie 判斷） | — |
| `user_engagement` | 頁面在前景停留超過 1 秒，於離開時觸發 | `engagement_time_msec` |

> 回想 Week 1：你在即時報表中看到的 `page_view`、`session_start`、`first_visit` 就是這些事件，它們一直默默在工作。

### 3.3 加強型評估事件（Enhanced Measurement Events）

GA4 已經寫好追蹤邏輯，你只需要在後台**開啟開關**。不需要修改 GTM，也不需要寫程式碼。這一層是本週的學習重點。

| 事件名稱 | 追蹤什麼 |
|----------|---------|
| `scroll` | 頁面捲動到 90% |
| `click`（外連） | 點擊離開你網站的連結 |
| `view_search_results` | 使用站內搜尋功能 |
| `video_start` / `video_progress` / `video_complete` | YouTube 嵌入影片的播放行為 |
| `file_download` | 下載檔案（PDF、Excel、ZIP 等） |
| `form_start` / `form_submit` | 表單開始填寫與送出 |

### 3.4 建議事件與自訂事件

這兩層留待 Week 5 詳細實作，本週先理解定位：

- **建議事件（Recommended Events）**：Google 針對特定產業定義好名稱與參數格式（如 `login`、`sign_up`、`share`）。用標準名稱的好處是 GA4 內建報表和預測受眾功能能自動支援
- **自訂事件（Custom Events）**：完全自行定義，適合追蹤網站獨有的業務行為（如 MovieTribe 的 `watch_trailer`、`add_to_watchlist`、`rate_movie`）

---

## 4. 深入解析：加強型評估的六大事件

### 4.1 捲動 `scroll`

使用者將頁面往下捲動至 **90%** 的位置時觸發，每個頁面只觸發一次。

| 項目 | 說明 |
|------|------|
| 攜帶參數 | `percent_scrolled`（固定為 90） |
| 限制 | 只偵測 90% 這個閾值。需要 25%、50%、75% 多段偵測須透過 GTM 設定 |
| MovieTribe 意義 | 判斷訪客是否真的「讀完」一篇電影評論 |

### 4.2 外連點擊 `click`

使用者點擊了一個**離開你網站**的連結時觸發。GA4 會比對連結網域與你的網站網域，不同則判定為外連。

| 項目 | 說明 |
|------|------|
| 攜帶參數 | `link_url`、`link_domain`、`link_classes`、`outbound`（是否為外連） |
| 判定邏輯 | 連結網域 ≠ 目前網站網域 → 觸發。站內連結不會觸發 |
| MovieTribe 意義 | 追蹤訪客點擊去 IMDb、YouTube、Netflix 等外部網站的行為 |

### 4.3 站內搜尋 `view_search_results`

使用者搜尋後，網址出現搜尋查詢參數時觸發。GA4 預設偵測 `q`、`s`、`search`、`query`、`keyword` 等常見參數名稱。

```
搜尋「全面啟動」→ 網址變成 https://www.movietribe.club/?s=全面啟動
                → GA4 偵測到參數 "s" → 觸發事件，search_term = "全面啟動"
```

| 項目 | 說明 |
|------|------|
| 攜帶參數 | `search_term`（搜尋關鍵字） |
| 前提條件 | 搜尋需在網址產生查詢參數。AJAX 即時搜尋不改變網址則不會觸發 |
| MovieTribe 意義 | 了解訪客搜尋什麼電影，作為內容策略的依據 |

### 4.4 影片參與 `video_start` / `video_progress` / `video_complete`

頁面上嵌入的 **YouTube 影片**被播放時觸發。**只支援 YouTube `<iframe>` 嵌入影片**。

| 事件名稱 | 觸發時機 | 關鍵參數 |
|----------|---------|----------|
| `video_start` | 影片開始播放 | `video_title`、`video_url` |
| `video_progress` | 播放進度達 10%、25%、50%、75% | 加上 `video_percent` |
| `video_complete` | 影片播放完畢 | 同上 |

MovieTribe 應用：如果嵌入了 YouTube 電影預告片，可以知道訪客是否看完、在哪個進度離開。

### 4.5 檔案下載 `file_download`

使用者點擊了指向常見文件格式的連結時觸發。GA4 根據副檔名判斷，預設偵測：`pdf`、`doc(x)`、`xls(x)`、`ppt(x)`、`csv`、`zip`、`rar`、`mp3`、`mp4`、`exe` 等。

| 項目 | 說明 |
|------|------|
| 攜帶參數 | `file_name`、`file_extension`、`link_url` |
| MovieTribe 意義 | 追蹤電影推薦清單 PDF 或活動行事曆 Excel 的下載次數 |

### 4.6 表單互動 `form_start` / `form_submit`

使用者與頁面上的 HTML `<form>` 元素互動時觸發。

| 事件名稱 | 觸發時機 | 攜帶參數 |
|----------|---------|----------|
| `form_start` | 首次與表單互動（如點擊輸入框） | `form_id`、`form_name`、`form_destination` |
| `form_submit` | 送出表單 | 同上 |

> 透過 JavaScript 框架（如 React、Vue）建構的表單可能無法被自動偵測。

---

## 5. 實作步驟

### 5.1 確認與設定加強型評估

**操作步驟：**

1. 登入 [GA4 後台](https://analytics.google.com/)，進入 MovieTribe 的 GA4 資源
2. 左下角點擊「**管理**」（齒輪圖示）
3. 在「資源」欄位中，點擊「**資料串流**」→ 點擊你的網站串流
4. 找到「**加強型評估**」區塊，確認總開關為開啟狀態

你會看到各細項的獨立開關：

| 細項 | 對應事件 | 建議設定 |
|------|----------|---------|
| 頁面瀏覽（Page views） | `page_view` | 維持開啟 |
| 捲動（Scrolls） | `scroll` | 維持開啟 |
| 外連點擊（Outbound clicks） | `click` | 維持開啟 |
| 站內搜尋（Site search） | `view_search_results` | 維持開啟 |
| 影片參與（Video engagement） | `video_start` 等 | 維持開啟 |
| 檔案下載（File downloads） | `file_download` | 維持開啟 |
| 表單互動（Form interactions） | `form_start` / `form_submit` | 維持開啟 |

5. 點擊「站內搜尋」旁的齒輪圖示，確認搜尋查詢參數

   在 MovieTribe 網站上進行一次搜尋，觀察網址中的參數名稱。例如 `?s=全面啟動` 表示參數為 `s`。如果參數名稱不在預設清單中，在此手動新增。

6. 確認後點擊「**儲存**」

### 5.2 觀察即時報表中的事件流

**準備**：開啟兩個瀏覽器視窗——視窗 A 放 GA4 即時報表、視窗 B 放 MovieTribe 網站。

逐一操作以下行為，每做完一個動作就回視窗 A 觀察：

| 步驟 | MovieTribe 上的動作 | 預期看到的事件 |
|------|-------------------|---------------|
| 1 | 開啟首頁 | `page_view`、`session_start` |
| 2 | 緩慢捲到頁面底部 | `scroll` |
| 3 | 點擊外部連結（如 YouTube、IMDb） | `click` |
| 4 | 回來使用搜尋功能 | `view_search_results` |
| 5 | 播放嵌入的 YouTube 影片 | `video_start`、`video_progress` |
| 6 | 點擊 PDF 下載連結 | `file_download` |

在即時報表中，點擊「**依事件名稱呈現的事件計數**」卡片查看事件清單，點擊單一事件可查看參數細節。也可以透過「**使用者快照**」看到單一使用者的完整事件序列。

### 5.3 使用 DebugView 進行深度驗證

**DebugView** 可以看到比即時報表更詳細的事件資訊，包含每個事件攜帶的所有參數。

1. 安裝 Chrome 擴充功能 [Google Analytics Debugger](https://chrome.google.com/webstore/detail/google-analytics-debugger/jnkmfdileelhofjcijamephohjechhna)
2. 點擊擴充功能圖示啟用除錯模式
3. 前往 GA4 後台 →「管理」→「**DebugView**」
4. 在另一個視窗瀏覽 MovieTribe，DebugView 會以時間軸呈現每個事件，點擊可展開查看所有參數

---

## 6. MovieTribe 具體應用情境

以下是透過自動收集與加強型評估事件即可回答的商業問題，**不需要寫任何程式碼**：

### 情境一：內容吸引力評估

> 「哪些電影介紹頁真的有人認真在看？」

比較 `page_view` 與 `scroll` 的次數。某頁有 100 次瀏覽但只有 10 次 scroll，代表 90% 的人沒讀到文章底部。搭配 `user_engagement` 的參與時間，進一步判斷內容品質。

### 情境二：外部引導追蹤

> 「訪客看完介紹後，會不會點去 Netflix 或 Disney+ 觀看？」

透過 `click` 事件的 `link_domain` 參數，統計訪客最常前往哪些外部網站。

### 情境三：站內搜尋洞察

> 「訪客在搜尋什麼？有沒有我們還沒收錄的熱門電影？」

透過 `view_search_results` 的 `search_term` 參數彙整熱門關鍵字，作為內容策略依據。

### 情境四：預告片觀看行為

> 「嵌入的 YouTube 預告片，訪客有看完嗎？」

計算 `video_complete` ÷ `video_start` 得出影片完成率，了解預告片是否夠吸引人。

### 情境五：新舊訪客比例

> 「MovieTribe 的新訪客多還是回訪者多？」

比較 `first_visit` 與 `session_start` 的次數，計算新訪客占比。

---

## 7. 本週任務

### 任務一：確認加強型評估設定（預計 5 分鐘）

- [ ] 進入 GA4 後台確認加強型評估全部開啟，截圖設定畫面
- [ ] 確認站內搜尋的查詢參數是否正確

### 任務二：製造事件並觀察即時報表（預計 15 分鐘）

- [ ] 依照 [5.2 節](#52-觀察即時報表中的事件流)逐一執行六種行為
- [ ] 截圖即時報表中出現的事件清單
- [ ] 填寫觀察紀錄：

| 事件 | 是否觸發？ | 觀察筆記 |
|------|-----------|---------|
| `page_view` | [ ] 是 / [ ] 否 | |
| `scroll` | [ ] 是 / [ ] 否 | |
| `click`（外連） | [ ] 是 / [ ] 否 | |
| `view_search_results` | [ ] 是 / [ ] 否 | |
| `video_start` | [ ] 是 / [ ] 否 | |
| `file_download` | [ ] 是 / [ ] 否 | |

### 任務三：事件分類練習（預計 10 分鐘）

判斷以下追蹤需求屬於哪一類事件（①自動收集 ②加強型評估 ③建議事件 ④自訂事件）：

| 追蹤需求 | 答案 |
|---------|------|
| 知道每個頁面有多少人瀏覽 | |
| 訪客把頁面捲到最下面 | |
| 訪客點了「加入收藏」按鈕 | |
| 訪客成功註冊會員 | |
| 訪客為電影打了星星評分 | |
| 訪客下載了電影推薦清單 PDF | |
| 訪客點擊連結前往 Netflix | |

### 挑戰任務（選做）

- [ ] 安裝 Google Analytics Debugger，用 DebugView 觀察事件參數細節
- [ ] 播放 YouTube 嵌入影片，觀察 `video_start` → `video_progress` → `video_complete` 是否依序出現

---

## 8. FAQ — 常見問題

**Q1：加強型評估事件和 GTM 設定的事件會衝突嗎？**

有可能。如果你在 GTM 中也設定了同類追蹤（如捲動），會**重複計算**。建議二擇一：使用加強型評估就不在 GTM 重複設定；需要更精細控制（如多段捲動深度）則關閉該細項改用 GTM。

**Q2：為什麼看不到 `scroll` 事件？**

三個常見原因：頁面太短不需要捲動、沒有捲到 90% 的位置、加強型評估的捲動開關未啟用。

**Q3：站內點擊會觸發 `click` 事件嗎？**

不會。加強型評估的 `click` 只追蹤**外連點擊**（連結網域 ≠ 你的網域）。追蹤站內按鈕點擊需要透過 GTM 設定自訂事件。

**Q4：站內搜尋追蹤沒有觸發怎麼辦？**

前提是搜尋行為會在網址產生查詢參數。如果網站使用 AJAX 或 SPA（單頁應用程式）的即時搜尋，網址不會改變，GA4 就偵測不到，需透過 GTM 搭配資料層手動推送。

**Q5：影片追蹤只支援 YouTube 嗎？**

是的，只支援 YouTube `<iframe>` 嵌入。Vimeo 或自架影片播放器需透過 GTM 搭配自訂 JavaScript 追蹤。

**Q6：「加強型評估」裡的頁面瀏覽和自動收集的 `page_view` 是同一個嗎？**

是同一個事件。加強型評估中的「頁面瀏覽」控制的是進階功能（如偵測瀏覽器 History 狀態變更觸發的頁面瀏覽），而非事件本身。

---

## 9. 參考資源

### 官方文件

- [GA4 自動收集的事件](https://support.google.com/analytics/answer/9234069?hl=zh-Hant) — 完整事件清單與參數說明
- [GA4 加強型評估事件](https://support.google.com/analytics/answer/9216061?hl=zh-Hant) — 各項功能說明
- [GA4 建議事件](https://support.google.com/analytics/answer/9267735?hl=zh-Hant) — 各產業建議事件名稱與參數
- [GA4 DebugView](https://support.google.com/analytics/answer/7201382?hl=zh-Hant) — 偵錯工具操作教學

### 延伸閱讀

- [集客數據行銷 — GA4 事件追蹤完整教學](https://inboundmarketing.com.tw/ga4%E6%95%99%E5%AD%B8/)
- [Haran 的行銷筆記 — GA4 加強型評估事件詳解](https://www.haranhuang.com/google-analytics-4-tutorial-collection.html)
- [MKTGholic 行銷癮 — GA4 事件總整理](https://mktgholic.com/google-analytics-4/)

### 本週使用到的工具

| 工具 | 網址 | 用途 |
|------|------|------|
| Google Analytics 4 | [analytics.google.com](https://analytics.google.com/) | 設定加強型評估、觀察即時報表 |
| Google Analytics Debugger | [Chrome 擴充商店](https://chrome.google.com/webstore/detail/google-analytics-debugger/jnkmfdileelhofjcijamephohjechhna) | 啟用 DebugView 偵錯模式 |

---

> **下週預告 — Week 5：自訂事件實作**
> 我們將學習透過 GTM 設定建議事件與自訂事件，為 MovieTribe 打造專屬的行為追蹤，例如「加入收藏」、「撰寫評論」等網站獨有的互動行為。
