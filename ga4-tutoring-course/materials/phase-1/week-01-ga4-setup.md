# Week 1：數位分析的起源與 GA4 環境搭建

本週是課程的第一步，我們將從「為什麼需要數據分析」出發，理解 GA4 的核心設計思維，並親手完成 GA4 與 GTM 的環境建置，讓 MovieTribe 網站開始收集訪客數據。

## 目錄

- [1. 本週學習目標](#1-本週學習目標)
- [2. 課前準備](#2-課前準備)
- [3. 核心概念講解](#3-核心概念講解)
  - [3.1 什麼是網站分析？](#31-什麼是網站分析)
  - [3.2 GA4 是什麼？](#32-ga4-是什麼)
  - [3.3 為什麼 UA 退場、GA4 登場？](#33-為什麼-ua-退場ga4-登場)
  - [3.4 事件模型的本質](#34-事件模型的本質)
- [4. 實作步驟](#4-實作步驟)
  - [4.1 建立 Google Analytics 4 資源](#41-建立-google-analytics-4-資源)
  - [4.2 建立 GTM 帳戶與容器](#42-建立-gtm-帳戶與容器)
  - [4.3 在 GTM 中設定 Google 代碼](#43-在-gtm-中設定-google-代碼)
  - [4.4 在 MovieTribe 網站上安裝 GTM 代碼](#44-在-movietribe-網站上安裝-gtm-代碼)
- [5. 即時驗證：確認數據正在流入](#5-即時驗證確認數據正在流入)
- [6. 本週任務（Small Win）](#6-本週任務small-win)
- [7. 常見問題 FAQ](#7-常見問題-faq)
- [8. 參考資源連結](#8-參考資源連結)

---

## 1. 本週學習目標

完成本週課程後，你將能夠：

| 項目 | 具體目標 |
|------|----------|
| 觀念理解 | 說明 GA4 與傳統 UA 的核心差異，以及為什麼 GA4 採用「事件模型」 |
| 環境建置 | 獨立建立一個 GA4 資源（Property）與一個 GTM 容器（Container） |
| 代碼安裝 | 將 GTM 代碼片段正確嵌入 MovieTribe 網站 |
| 數據驗證 | 在 GA4 即時報表（Realtime Report）中看到自己的瀏覽數據 |

---

## 2. 課前準備

在上課之前，請確認以下事項已備妥：

- [ ] 擁有一組 Google 帳號（Gmail 即可）
- [ ] 能登入 MovieTribe 網站的後台（需要能修改網站原始碼或安裝外掛）
- [ ] 準備一台電腦，使用 Chrome 瀏覽器（後續會大量使用 Chrome 擴充功能）
- [ ] 安裝 Chrome 擴充功能：[Tag Assistant Companion](https://chrome.google.com/webstore/detail/tag-assistant-companion/jmekfmbnaedffjfnmkpfblhpmjligpaa)（用於驗證代碼安裝狀態）

---

## 3. 核心概念講解

### 3.1 什麼是網站分析？

想像你經營一間實體電影院。你會想知道：

- 今天來了多少觀眾？
- 他們最常看哪個廳的電影？
- 從售票到入場，有多少人中途離開？
- 週末的人潮和平日差多少？

**網站分析（Web Analytics）就是把這些問題搬到線上世界。**

你的 MovieTribe 網站就像一座線上電影院，每天有訪客進進出出。網站分析工具會幫你記錄：「誰來了、看了什麼、待了多久、做了什麼動作」，讓你根據數據做出更好的經營決策。

### 3.2 GA4 是什麼？

**GA4（Google Analytics 4）** 是 Google 提供的免費網站分析工具，目前是最新一代的版本。

| 項目 | 說明 |
|------|------|
| 全名 | Google Analytics 4 |
| 費用 | 免費（企業級版本 Analytics 360 需付費） |
| 用途 | 追蹤與分析網站及 App 的使用者行為 |
| 前一代 | UA（Universal Analytics，通用分析），已於 2024 年全面停止處理資料 |

簡單來說，GA4 就是你的「網站數據儀表板」—— 就像汽車儀表板告訴你時速、油量、引擎溫度一樣，GA4 告訴你網站的流量、訪客行為和內容表現。

### 3.3 為什麼 UA 退場、GA4 登場？

#### 日常生活類比：從登記簿到感應器

想像一間博物館的兩種計算參觀者的方式：

**舊方式（UA 的邏輯）—— 登記簿模式**
- 訪客進門時在登記簿上簽到，記錄「幾點進來的」
- 走到不同展廳時，再簽一次名
- 博物館只知道「有人來了、去了哪幾個展廳」
- 如果訪客只站在一個展品前看了 30 分鐘卻沒移動到其他展廳，登記簿上只會顯示「來了一次就走了」—— 這就是 UA 時代惡名昭彰的「跳出率」問題

**新方式（GA4 的邏輯）—— 感應器模式**
- 博物館在每個展品旁邊都裝了感應器
- 訪客靠近展品 → 紀錄「觀看」事件
- 訪客按下語音導覽 → 紀錄「互動」事件
- 訪客在展品前停留 3 分鐘 → 紀錄「深度參與」事件
- 博物館能精確知道每個訪客和每件展品之間發生了什麼互動

#### UA 與 GA4 的關鍵差異

| 比較項目 | UA（通用分析） | GA4（新一代） |
|----------|---------------|--------------|
| 資料模型 | 以「工作階段」（Session）為核心 | 以「事件」（Event）為核心 |
| 追蹤單位 | 頁面瀏覽（Pageview） | 所有行為都是事件（Event） |
| 跨裝置 | 難以整合手機與電腦的行為 | 內建跨裝置追蹤能力 |
| 隱私合規 | 高度仰賴 Cookie | 為無 Cookie 時代設計 |
| 分析彈性 | 報表格式固定 | 可自由組合探索報表 |
| 現況 | 2024 年已停止服務 | 目前唯一正式版本 |

**一句話總結**：UA 只能記錄「訪客去了哪些頁面」，GA4 能記錄「訪客在每個頁面上做了什麼事」。

### 3.4 事件模型的本質

這是 GA4 最核心的設計理念，理解它之後，後面所有的概念都會變得容易。

#### 什麼是「事件」（Event）？

**事件 = 使用者在你的網站上做的任何一個動作。**

以 MovieTribe 為例：

| 使用者動作 | 對應的 GA4 事件 |
|-----------|----------------|
| 打開 MovieTribe 首頁 | `page_view`（頁面瀏覽） |
| 往下捲動頁面看更多電影 | `scroll`（捲動） |
| 點擊某部電影的介紹連結 | `click`（點擊） |
| 在網站上停留超過 10 秒 | `user_engagement`（使用者互動） |
| 第一次造訪 MovieTribe | `first_visit`（首次造訪） |
| 開始一段新的瀏覽 | `session_start`（工作階段開始） |

#### 事件的結構：事件名稱 + 參數

每一個事件除了名稱之外，還可以攜帶「參數」（Parameters），就像包裹上除了標籤還有明細。

```
事件名稱：page_view（頁面瀏覽）
├── 參數 page_title = "最新電影推薦 — MovieTribe"
├── 參數 page_location = "https://www.movietribe.club/recommendations"
└── 參數 page_referrer = "https://www.google.com"
```

類比：如果事件是一張「收據」，那參數就是收據上的「明細項目」。只知道有一筆消費（事件）不夠，你還需要知道買了什麼、多少錢、在哪間店（參數）。

#### GA4 的四種事件類別

| 類別 | 說明 | 誰設定的 | 範例 |
|------|------|---------|------|
| 自動收集事件（Automatically Collected） | GA4 裝好就自動追蹤 | Google | `page_view`、`session_start`、`first_visit` |
| 加強型評估事件（Enhanced Measurement） | 開啟開關即可追蹤 | Google（需手動啟用） | `scroll`、`click`（站外連結）、`file_download` |
| 建議事件（Recommended Events） | Google 建議的標準命名 | 你自己 | `login`、`sign_up`、`share` |
| 自訂事件（Custom Events） | 完全客製化 | 你自己 | `watch_trailer`、`add_to_watchlist` |

本週我們完成環境建置後，GA4 就會自動開始收集前兩類事件，不需要額外設定。

---

## 4. 實作步驟

以下是今天的動手環節。我們會依序完成四個步驟，建議跟著老師一起操作。

### 4.1 建立 Google Analytics 4 資源

**目標**：建立一個專屬於 MovieTribe 的 GA4 資源，取得「評估 ID」（Measurement ID）。

**操作步驟**：

1. **前往 Google Analytics**
   - 開啟 Chrome 瀏覽器
   - 進入 [analytics.google.com](https://analytics.google.com/)
   - 使用你的 Google 帳號登入

2. **建立帳戶（Account）**
   - 點擊左下角的「管理」齒輪圖示
   - 點擊「+ 建立」→「帳戶」
   - 帳戶名稱填入：`MovieTribe`
   - 資料共用設定：保持預設即可，點擊「下一步」

3. **建立資源（Property）**
   - 資源名稱：`MovieTribe - 主網站`
   - 報表時區：選擇「台灣」（GMT+8）
   - 幣別：選擇「新台幣 TWD」
   - 點擊「下一步」

4. **填寫商家資訊**
   - 產業類別：選擇「藝術與娛樂」
   - 商家規模：選擇最小的選項即可
   - 點擊「下一步」

5. **選擇業務目標**
   - 勾選「瞭解使用者行為」（這對內容型網站最重要）
   - 也可勾選「產生待開發客戶」
   - 點擊「建立」

6. **建立資料串流（Data Stream）**
   - 平台選擇「網頁」
   - 網站網址填入：`www.movietribe.club`
   - 串流名稱填入：`MovieTribe 網站串流`
   - 確認「加強型評估」（Enhanced Measurement）已開啟（預設為開啟）
   - 點擊「建立串流」

7. **記錄你的評估 ID**
   - 建立完成後，畫面會顯示串流詳細資訊
   - 找到「評估 ID」（Measurement ID），格式為 `G-XXXXXXXXXX`
   - **請把這組 ID 記下來**，稍後設定 GTM 時會用到

> **概念釐清**：帳戶（Account）→ 資源（Property）→ 資料串流（Data Stream）的關係，就像「公司 → 品牌 → 網站」。一間公司可以有多個品牌，一個品牌可以有多個網站或 App。

### 4.2 建立 GTM 帳戶與容器

**什麼是 GTM？**

**GTM（Google Tag Manager，Google 代碼管理工具）** 是一個「代碼管理員」。

類比：想像你的網站是一棟辦公大樓，GA4 是其中一家要進駐的公司。你有兩種方式讓公司進駐：

- **不用 GTM**：每次有新公司要進駐，你就得打牆壁、重新拉線路（修改網站程式碼）
- **使用 GTM**：你在大樓蓋好一間「總機管理室」，以後任何新公司進駐，只要在管理室做設定就好，不用動到大樓結構

使用 GTM 的好處是：**你不需要每次都請工程師改網站程式碼，大部分的追蹤設定都能在 GTM 介面中完成。**

**操作步驟**：

1. **前往 Google Tag Manager**
   - 開啟新分頁，進入 [tagmanager.google.com](https://tagmanager.google.com/)
   - 使用同一組 Google 帳號登入

2. **建立帳戶**
   - 點擊「建立帳戶」
   - 帳戶名稱：`MovieTribe`
   - 國家/地區：選擇「台灣」

3. **建立容器（Container）**
   - 容器名稱：`movietribe.club`
   - 目標平台：選擇「網頁」
   - 點擊「建立」
   - 同意服務條款

4. **記錄你的 GTM 容器 ID**
   - 建立完成後，畫面會跳出一段安裝代碼
   - 容器 ID 格式為 `GTM-XXXXXXX`，顯示在畫面右上角
   - **先不要關閉這個視窗**，我們稍後會用到這段代碼

> **小提醒**：GTM 的「帳戶」和 GA4 的「帳戶」是不同的東西，它們各自獨立。但建議用同一組 Google 帳號登入，方便管理。

### 4.3 在 GTM 中設定 Google 代碼

**目標**：在 GTM 裡面建立一個「Google 代碼」（Google Tag），讓 GTM 知道要把收集到的數據送給 GA4。

類比：GTM 是總機管理室，現在我們要在管理室裡「登記 GA4 這家公司的分機號碼」，讓來電能正確轉接。

**操作步驟**：

1. **進入 GTM 工作區**
   - 如果你還在 GTM 首頁，點擊剛才建立的容器 `movietribe.club` 進入工作區（Workspace）

2. **新增代碼（Tag）**
   - 在左側選單點擊「代碼」（Tags）
   - 點擊「新增」

3. **設定代碼類型**
   - 點擊「代碼設定」區塊
   - 選擇「Google 代碼」（Google Tag）
   - 在「代碼 ID」欄位填入你的 GA4 評估 ID：`G-XXXXXXXXXX`（替換為你在 4.1 步驟記下的那組 ID）

4. **設定觸發條件（Trigger）**
   - 點擊下方的「觸發條件」區塊
   - 選擇「All Pages」（所有頁面）
   - 這代表：網站的每一個頁面都會啟動這段追蹤代碼

5. **命名並儲存**
   - 在左上方將代碼命名為：`GA4 設定 — MovieTribe`
   - 點擊右上角「儲存」

6. **預覽測試**
   - 點擊工作區右上角的「預覽」按鈕
   - 會開啟 Tag Assistant 視窗
   - 在「Your website's URL」欄位輸入：`https://www.movietribe.club/`
   - 點擊「Connect」
   - 確認你的代碼出現在「Tags Fired」（已觸發的代碼）區塊中
   - 如果出現在「Tags Fired」下方，代表設定正確

7. **發布（Publish）**
   - 確認預覽無誤後，回到 GTM 工作區
   - 點擊右上角「提交」
   - 版本名稱填入：`v1.0 — GA4 基礎安裝`
   - 版本說明填入：`安裝 GA4 Google 代碼，追蹤所有頁面`
   - 點擊「發布」

> **重要觀念**：在 GTM 中做完設定後，一定要「提交 → 發布」才會正式生效。就像你寫完 Email 要按「送出」一樣，GTM 裡的修改在發布之前都只是草稿。

### 4.4 在 MovieTribe 網站上安裝 GTM 代碼

**目標**：將 GTM 的代碼片段嵌入 MovieTribe 網站的 HTML 中，讓 GTM 能在網站上運作。

**需要安裝的代碼**：

GTM 會提供兩段代碼，分別要放在網頁的不同位置：

**第一段代碼**（放在 `<head>` 標籤中，越上方越好）：

```html
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXXX');</script>
<!-- End Google Tag Manager -->
```

**第二段代碼**（放在 `<body>` 標籤開頭之後）：

```html
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXXX"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
```

> 請將上方的 `GTM-XXXXXXX` 替換為你自己的容器 ID。

**依據網站平台的安裝方式**：

MovieTribe 的網站需要確認使用的平台或框架，常見情況如下：

| 網站平台 | 安裝方式 |
|---------|---------|
| WordPress | 安裝外掛「GTM4WP」或在「佈景主題 → 自訂 → 額外 CSS/JS」中貼入代碼 |
| Wix | 進入「設定 → 自訂代碼」，分別貼入 Head 與 Body 代碼 |
| Squarespace | 進入「設定 → 進階 → 程式碼插入」 |
| 自架網站（HTML） | 直接編輯 HTML 檔案的 `<head>` 與 `<body>` 區段 |

**WordPress 安裝步驟（使用 GTM4WP 外掛）**：

1. 登入 WordPress 後台
2. 前往「外掛」→「安裝外掛」
3. 搜尋 `GTM4WP`（全名：Google Tag Manager for WordPress）
4. 安裝並啟用外掛
5. 前往「設定」→「Google Tag Manager」
6. 在「Google Tag Manager ID」欄位填入你的 `GTM-XXXXXXX`
7. 容器代碼放置方式選擇「Off」之外的選項（建議選「Footer of the page」或「Custom」）
8. 儲存設定

**手動安裝步驟（自架網站）**：

1. 找到網站的主要 HTML 模板檔案（通常是 `index.html` 或版型的 `header` 檔案）
2. 在 `<head>` 標籤內、盡可能靠上方的位置，貼入第一段代碼
3. 在 `<body>` 標籤開始之後，貼入第二段代碼
4. 儲存檔案並上傳到伺服器

> **上課時我們會一起確認 MovieTribe 的實際平台，並選擇最適合的安裝方式。**

---

## 5. 即時驗證：確認數據正在流入

安裝完成後，最重要的一步是確認「數據真的進來了」。

**驗證步驟**：

1. **打開 GA4 即時報表**
   - 前往 [analytics.google.com](https://analytics.google.com/)
   - 進入 MovieTribe 的 GA4 資源
   - 左側選單點擊「報表」→「即時」（Realtime）

2. **製造測試流量**
   - 開啟另一個瀏覽器分頁（或用手機）
   - 前往 `https://www.movietribe.club/`
   - 在網站上隨意瀏覽幾個頁面、滾動頁面

3. **回到 GA4 檢查即時報表**
   - 你應該會看到「過去 30 分鐘的使用者」數字從 0 變成 1（或以上）
   - 在「依事件名稱呈現的事件計數」區塊中，應該能看到：
     - `page_view` — 你瀏覽了幾個頁面
     - `session_start` — 你開始了一段瀏覽
     - `first_visit` — 你是第一次造訪（如果是新的瀏覽器）
     - `user_engagement` — 你與網站產生了互動
     - `scroll` — 你滾動了頁面（如果有的話）

4. **使用 Tag Assistant 進行更詳細的驗證**
   - 回到 GTM，點擊「預覽」
   - 在 Tag Assistant 中連結到 MovieTribe 網站
   - 確認「GA4 設定 — MovieTribe」代碼出現在「Tags Fired」清單中
   - 如果出現在「Tags Not Fired」，代表觸發條件有問題，需要排查

**驗證檢查清單**：

| 檢查項目 | 預期結果 | 狀態 |
|---------|---------|------|
| GA4 即時報表顯示使用者數 > 0 | 看到至少 1 位使用者 | [ ] |
| 即時報表出現 `page_view` 事件 | 有出現 | [ ] |
| 即時報表出現 `session_start` 事件 | 有出現 | [ ] |
| Tag Assistant 顯示代碼已觸發 | Tags Fired 清單中有代碼 | [ ] |
| Tag Assistant 無錯誤訊息 | 無紅色警告 | [ ] |

---



## 6. 常見問題 FAQ

### Q1：GA4 即時報表顯示 0 位使用者，怎麼辦？

**常見原因與排查步驟**：

| 可能原因 | 排查方式 |
|---------|---------|
| GTM 代碼尚未正確安裝 | 使用 Tag Assistant 檢查代碼是否觸發 |
| GTM 修改尚未發布 | 回到 GTM 確認已經「提交 → 發布」 |
| GA4 評估 ID 填錯 | 比對 GA4 資料串流中的 ID 是否與 GTM 中填入的一致 |
| 瀏覽器有 AdBlock 等擋廣告外掛 | 暫時停用阻擋外掛，或換一個瀏覽器測試 |
| 數據有延遲 | 即時報表通常在幾秒到一分鐘內更新，稍等片刻 |

### Q2：GA4 和 GTM 有什麼不同？我會搞混。

用一張表釐清它們的角色分工：

| 項目 | GA4 | GTM |
|------|-----|-----|
| 角色 | 數據分析工具（看報表的地方） | 代碼管理工具（管代碼的地方） |
| 類比 | 公司的「數據分析部門」 | 大樓的「總機管理室」 |
| 你在這裡做什麼 | 看報表、分析數據 | 設定要追蹤什麼、把追蹤代碼部署到網站 |
| 網址 | analytics.google.com | tagmanager.google.com |

**簡單記法**：GTM 負責「收集」數據，GA4 負責「呈現」數據。

### Q3：我能不能不用 GTM，直接在網站上安裝 GA4？

技術上可以，但強烈不建議。原因如下：

| 項目 | 不用 GTM（直接安裝） | 使用 GTM |
|------|---------------------|---------|
| 新增追蹤功能 | 每次都需改網站程式碼 | 在 GTM 介面操作，不需動網站 |
| 操作門檻 | 需要請工程師協助 | 行銷或 PM 可自行操作 |
| 版本管理 | 無法記錄修改歷史 | 每次發布都有版本紀錄 |
| 除錯工具 | 不方便 | Tag Assistant 內建預覽與除錯 |

### Q4：「加強型評估」是什麼？需要額外設定嗎？

加強型評估（Enhanced Measurement）是 GA4 內建的自動追蹤功能。開啟後，GA4 會自動追蹤一些常見的使用者行為，不需要在 GTM 做額外設定：

| 自動追蹤項目 | 說明 |
|-------------|------|
| 頁面瀏覽（Page views） | 使用者瀏覽任何頁面 |
| 捲動（Scrolls） | 使用者將頁面往下捲動至 90% |
| 外連點擊（Outbound clicks） | 使用者點擊前往其他網站的連結 |
| 站內搜尋（Site search） | 使用者使用網站內的搜尋功能 |
| 影片互動（Video engagement） | 使用者播放、暫停嵌入的 YouTube 影片 |
| 檔案下載（File downloads） | 使用者下載檔案（PDF、Excel 等） |

建立 GA4 資料串流時，加強型評估預設是開啟的。我們在 4.1 步驟已經確認過了。

### Q5：安裝完成後，多久才能在 GA4 看到歷史報表？

| 報表類型 | 數據出現時間 |
|---------|-------------|
| 即時報表（Realtime） | 幾秒到 1 分鐘 |
| 標準報表（Standard Reports） | 24-48 小時 |
| 探索報表（Explorations） | 24-48 小時 |

今天我們主要使用「即時報表」來驗證安裝是否成功，不需要等待。

---

## 7. 參考資源連結

### 官方文件

- [GA4 官方說明中心](https://support.google.com/analytics/?hl=zh-Hant) — Google 官方的 GA4 操作指南
- [GTM 官方說明中心](https://support.google.com/tagmanager/?hl=zh-Hant) — Google 官方的 GTM 操作指南
- [GA4 設定助理](https://support.google.com/analytics/answer/9304153?hl=zh-Hant) — 建立 GA4 資源的官方步驟
- [事件簡介](https://support.google.com/analytics/answer/9322688?hl=zh-Hant#zippy=%2C%E5%8D%B3%E6%99%82%E5%A0%B1%E8%A1%A8%2Cdebugview-%E5%A0%B1%E8%A1%A8) — 事件類型、即時報表與 DebugView 報表說明
- [GA4 建議事件](https://support.google.com/analytics/answer/9267735?hl=zh-Hant) — Google 預先定義的事件名稱與參數規範

### 延伸閱讀

- [集客數據行銷 — GA4 新手入門教學](https://inboundmarketing.com.tw/ga4%E6%95%99%E5%AD%B8/) — 中文 GA4 完整教學
- [MKTGholic 行銷癮 — GTM 三大支柱教學](https://mktgholic.com/google-tag-manager/what-is-gtm-tag-trigger-variables/) — 了解 GTM 的代碼、觸發條件、變數
- [Haran 的行銷筆記 — GA4 教學合集](https://www.haranhuang.com/google-analytics-4-tutorial-collection.html) — 系統性的 GA4 進階教學

### 本週使用到的工具

| 工具 | 網址 | 用途 |
|------|------|------|
| Google Analytics 4 | [analytics.google.com](https://analytics.google.com/) | 數據分析平台 |
| Google Tag Manager | [tagmanager.google.com](https://tagmanager.google.com/) | 代碼管理工具 |
| Tag Assistant Companion | [Chrome 擴充商店](https://chrome.google.com/webstore/detail/tag-assistant-companion/jmekfmbnaedffjfnmkpfblhpmjligpaa) | GTM 預覽除錯工具 |

---

> **下週預告**：Week 2 我們將學習 GA4 最核心的兩個概念 —— 維度（Dimensions）與指標（Metrics）。理解了這兩個概念，你就能看懂 GA4 裡的所有報表。
