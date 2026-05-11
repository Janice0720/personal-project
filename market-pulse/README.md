# 市場輿情分析儀表板（Market Pulse Dashboard）

每日自動搜集國內外金融市場新聞，萃取熱門關鍵字、對應產業情感，產出好好證券基金篩選連結。

## 快速開始

### 1. 安裝套件

```bash
pip install -r requirements.txt
```

### 2. 設定環境變數

複製範本並填入 Clarity Cookie：

```bash
cp .env.example .env
```

編輯 `.env`：
```
CLARITY_SESSION_TOKEN=（登入 clarity.vibegens.com 後從瀏覽器 F12 → Network → Cookie 取得）
CLARITY_CSRF_TOKEN=（同上）
```

Cookie 有效期約 30 天（到 2026/05/07），到期後需重新登入並更新。

### 3. 啟動 Dashboard

```bash
streamlit run app.py
```

開啟瀏覽器：http://localhost:8501

---

## 功能說明

| 功能 | 說明 |
|------|------|
| **Top 10 熱門關鍵字** | 來自 Clarity API（主力）+ RSS 標題頻率分析 |
| **熱門產業分析** | 關鍵字對應產業，標示看漲 📈 / 看跌 📉 / 觀望 ➡️ |
| **因果解釋** | 自動產生「為何此關鍵字帶動此產業」說明文字 |
| **好好證券連結** | 點擊直接跳至好好證券對應基金篩選頁面 |
| **每日自動排程** | 每日 08:00 自動更新（可在 `config.py` 調整時間） |
| **手動重新分析** | 點擊「🔄 立即重新分析」按鈕立即重新抓取 |
| **認證失效警示** | Clarity Token 過期時頂部顯示黃色警告 |

---

## 資料來源

### 自動抓取

| 來源 | 類型 |
|------|------|
| [Clarity 趨勢分析](https://clarity.vibegens.com/)（需登入） | 16+ 來源彙整趨勢 |
| Yahoo 股市 RSS - 台灣市場 | 國內股市 |
| Yahoo 股市 RSS - 國際財經 | 國際市場 |
| Yahoo 股市 RSS - 基金新聞 | 基金動態 |
| TWSE 臺灣證交所 RSS | 官方公告 |
| Reuters Business RSS | 國際財經 |

### 人工參考連結（Dashboard 側欄）

- [Clarity 趨勢分析](https://clarity.vibegens.com/)
- [Glint Trade Terminal](https://glint.trade/terminal)
- [TradingView](https://www.tradingview.com/)

---

## 好好證券篩選對照表更新

編輯 `industry_map.py` 中的 `INDUSTRY_FUNDSWAP_MAP`，將產業名稱對應至好好證券的 `fundNameCategory` 參數值：

```python
INDUSTRY_FUNDSWAP_MAP = {
    "半導體／科技": "科技",    # 對應 fundNameCategory=科技
    "貴金屬": "貴金屬",
    # ... 待補充完整清單
}
```

---

## 檔案結構

```
market-pulse/
├── app.py              # Streamlit Dashboard 主程式
├── collector.py        # 新聞抓取（Clarity API + RSS）
├── analyzer.py         # NLP 分析（關鍵字、產業、情感）
├── scheduler.py        # APScheduler 每日排程
├── industry_map.py     # 關鍵字 → 產業對照表
├── config.py           # 設定（API、來源清單、排程時間）
├── .env                # 實際 Token（不 commit）
├── .env.example        # Token 設定範本
├── data/cache/         # 每日分析 JSON 快取（30 天）
├── requirements.txt
└── README.md
```

---

## 常見問題

**Q: 開啟 Dashboard 後顯示黃色警告「Clarity API 認證失效」**

A: 表示 `.env` 中的 Token 已過期或未設定。請重新登入 [clarity.vibegens.com](https://clarity.vibegens.com/)，從瀏覽器 F12 → Network → 任一 API 請求的 Cookie 欄位中取得 `__Secure-authjs.session-token` 與 `__Host-authjs.csrf-token`，更新 `.env` 後重新整理頁面。

**Q: 可以新增更多關鍵字對應更多產業嗎？**

A: 可以。編輯 `industry_map.py` 中的 `KEYWORD_INDUSTRY_MAP`，新增 `"關鍵字": ["產業名稱"]` 即可。
