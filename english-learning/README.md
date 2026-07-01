# English Learning 英文學習管理

個人英文課程錄音、逐字稿與課後筆記的管理系統。依日期與主題分類，支援快速複習與進度追蹤。

---

## 目錄

1. [資料夾結構](#1-資料夾結構)
2. [每堂課 SOP](#2-每堂課-sop)
3. [環境安裝（首次）](#3-環境安裝首次)
4. [課程索引](#4-課程索引)

---

## 1. 資料夾結構

> 檔名格式：`lesson-NN-<slug>`。`NN` 為**全課程連續編號**（跨日期遞增，看得出是第幾堂課）；`<slug>` 是主題的英文短代稱（由 `--slug` 指定，未給則自動從 `--topic` 衍生）。主題完整中文仍記在檔案標題與下方課程索引。

```
english-learning/
├── recordings/YYYY-MM-DD/lesson-NN-<slug>.m4a       ← 原始錄音備份（不進 git，見 .gitignore）
├── transcripts/YYYY-MM-DD/lesson-NN-<slug>.md       ← Whisper 逐字稿
├── notes/YYYY-MM-DD/
│   ├── lesson-NN-<slug>-notes.md                    ← 課後學習筆記
│   └── lesson-NN-<slug>-homework.md                 ← 作業（初稿→修正→完整版）
├── vocabulary/
│   ├── master-vocab.csv                             ← 所有課堂單字總表（可匯入 Anki）
│   └── README.md                                    ← 單字複習 / Anki 匯入說明
├── homework-tracker.md                              ← 作業狀態追蹤
└── scripts/
    ├── run.sh             ← Step 1：一鍵轉譯入口（用這個）
    ├── transcribe.py      ← Whisper 轉譯主腳本
    ├── notes.sh           ← Step 2：呼叫 Claude API 的入口（自動找正確 Python）
    ├── generate_notes.py  ← Step 2：Claude 筆記產出主腳本
    ├── extract_vocab.py   ← Step 3：從筆記彙整單字到總表
    ├── update_index.sh    ← Step 5：更新索引的入口（自動找正確 Python）
    ├── update_index.py    ← Step 5：課程索引自動更新主腳本
    └── INSTALL.md         ← 環境安裝說明
```

---

## 2. 每堂課 SOP

> 全流程皆在 Terminal 執行，不需手動貼文字給 AI。先 `cd` 到專案根目錄再跑。

```bash
cd "/Users/Janice/Desktop/Git Hub workspace/personal-project/english-learning"
```

---

### Step 1｜轉譯錄音（Whisper，約 10–15 分鐘）

```bash
bash scripts/run.sh /path/to/錄音檔.m4a --topic "職場英文口說 — KYC" --slug kyc-career
```

完成後自動產生：
- `transcripts/YYYY-MM-DD/lesson-NN-<slug>.md` — 逐字稿
- `notes/YYYY-MM-DD/lesson-NN-<slug>-notes.md` — 空白筆記範本（下一步會填入）
- `notes/YYYY-MM-DD/lesson-NN-<slug>-homework.md` — 空白作業範本

> **`--slug` 可省略**：省略時自動從 `--topic` 衍生檔名。
> **想更快測試**：加 `--model small`。**雜訊多/術語多**：加 `--model large`。

---

### Step 2｜AI 自動產出筆記（Claude，約 30–60 秒）

```bash
bash scripts/notes.sh transcripts/YYYY-MM-DD/lesson-NN-<slug>.md
```

腳本讀取逐字稿，產出一份結構化筆記範本（空白表格 + 逐字稿嵌在底部），你直接開檔在上半段填空，不需再切換到逐字稿對照。

> **快速用法**：`--latest` 自動抓最新一堂課，不需手動填路徑：
> ```bash
> bash scripts/notes.sh --latest
> ```
> **重新產出**：加 `--force` 覆蓋已有內容。
> **使用 AI 自動分析**（需 API Key）：加 `--provider openai` 或 `--provider anthropic`。

---

### Step 3｜彙整單字到總表（複習用）

```bash
python3 scripts/extract_vocab.py notes/YYYY-MM-DD/lesson-NN-<slug>-notes.md
```

把這堂課筆記裡的單字加進 `vocabulary/master-vocab.csv`（自動去重），方便日後用 Anki 複習。

> 詳細的 Anki 匯入與複習節奏，見 [`vocabulary/README.md`](vocabulary/README.md)。

---

### Step 4｜寫作業

打開自動產生的 `notes/YYYY-MM-DD/lesson-NN-<slug>-homework.md`，依模板完成：

1. **題目**：填入老師指派的題目與繳交日期
2. **我的初稿**：先用自己會的句子寫（別查字典，保留原樣方便對照）
3. **文法修正**：填入修正建議（可自行用 Cursor 開逐字稿一起看）
4. **修改後完整版**：整合修正
5. **自我複習重點**：抽出值得記的句型與單字

完成後到 [`homework-tracker.md`](homework-tracker.md) 更新狀態。

---

### Step 5｜更新課程索引

```bash
bash scripts/update_index.sh
```

自動掃描 `transcripts/` 資料夾，重建下方課程索引表格並寫入 README.md，不需手動編輯。

---

## 3. 環境安裝（首次）

> 已安裝過可跳過。詳細說明見 [`scripts/INSTALL.md`](scripts/INSTALL.md)。

```bash
brew install ffmpeg
pip install --user openai-whisper
```

> Step 2 預設為純範本模式，**不需要 API Key**。
> 若日後想用 AI 自動產筆記，可加裝 `pip install --user openai` 並設定 `OPENAI_API_KEY`。

**常見問題：**

| 問題 | 解法 |
|------|------|
| `whisper not found` | 用 `bash scripts/run.sh`，腳本會自動找正確 Python |
| 中文被轉成亂碼 / 出現「Do. Do.」 | 預設已鎖 `--language en`；仍不佳改 `--model large` |
| 課堂編號不如預期 | 編號為**全課程連續**，掃描 `transcripts/` 所有日期取最大值 +1；若要重編，檢查是否有殘留舊檔 |

---

## 4. 課程索引

| 日期 | 課堂 | 主題 | 逐字稿 | 筆記 | 作業 |
|------|------|------|--------|------|------|
| 2026-06-11 | Lesson 01 | 職場英文口說 — KYC 稽核 & 工作壓力 | [查看](transcripts/2026-06-11/lesson-01-kyc-career.md) | [查看](notes/2026-06-11/lesson-01-kyc-career-notes.md) | [查看](notes/2026-06-11/lesson-01-kyc-career-homework.md) |
