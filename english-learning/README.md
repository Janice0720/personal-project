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
    ├── run.sh             ← 一鍵轉譯入口（用這個）
    ├── transcribe.py      ← Whisper 轉譯主腳本
    ├── extract_vocab.py   ← 從筆記彙整單字到總表
    └── INSTALL.md         ← 環境安裝說明
```

---

## 2. 每堂課 SOP

### Step 1｜轉譯錄音（Terminal，約 4-5 分鐘）

```bash
cd "/Users/Janice/Desktop/Git Hub workspace/personal-project/english-learning"
bash scripts/run.sh /path/to/錄音檔.m4a --topic "職場英文口說 — KYC" --slug kyc-career
```

完成後自動產生：
- `transcripts/YYYY-MM-DD/lesson-NN-<slug>.md` — 逐字稿
- `notes/YYYY-MM-DD/lesson-NN-<slug>-notes.md` — 空白筆記範本
- `notes/YYYY-MM-DD/lesson-NN-<slug>-homework.md` — 空白作業範本

> 預設使用 `medium` 模型並鎖定 `--language en`，已針對中英混雜口說最佳化（會抑制「Do. Do. Do.」這類靜音段幻覺）。約 10–15 分鐘。
> **想更快測試**：加 `--model small`。**雜訊多/術語多**：加 `--model large`。
> **`--slug` 可省略**：省略時會自動從 `--topic` 衍生檔名。

---

### Step 2｜分析逐字稿產出筆記（Composer，低 token）

開啟 **Cursor Composer**，貼入以下 prompt，再貼上逐字稿內容，送出後將輸出複製到 `notes/` 對應的 `.md` 檔：

```
你是英文課學習助理。以下是一堂英文口說課的逐字稿。請分析並輸出繁體中文 Markdown 筆記，格式如下：

## 課堂主題與摘要
- 今日主題（1句）
- 重點摘要（3-5條）

## 重點單字／片語
| 單字／片語 | 詞性 | 中文意思 | 課堂例句 |
|-----------|------|---------|---------|
（從老師明確教授、示範或糾正的詞彙中提取，至少10個）

## 老師的關鍵糾正
| 學生說的 | 老師建議改成 | 重點說明 |
|--------|------------|--------|
（只列老師明確指出的錯誤）

## 文法重點
（老師強調的文法或表達方式，條列式）

## 作業
（老師明確指派的下次任務，若無則寫「無」）

---
逐字稿：
[貼上 transcripts/YYYY-MM-DD/lesson-NN.md 的內容]
```

---

### Step 3｜彙整單字到總表（複習用）

把這堂課筆記裡的單字加進總表（會自動去重），方便日後用 Anki 複習：

```bash
python3 scripts/extract_vocab.py notes/YYYY-MM-DD/lesson-NN-<slug>-notes.md
```

> 詳細的 Anki 匯入與複習節奏，見 [`vocabulary/README.md`](vocabulary/README.md)。

---

### Step 4｜寫作業

打開自動產生的 `notes/YYYY-MM-DD/lesson-NN-<slug>-homework.md`，依模板完成：

1. **題目**：填入老師指派的題目與繳交日期
2. **我的初稿**：先用自己會的句子寫（別查字典，保留原樣方便對照）
3. **文法修正**：可請 Claude／ChatGPT 逐句對照，填修正表
4. **修改後完整版**：整合修正
5. **自我複習重點**：抽出值得記的句型與單字

完成後到 [`homework-tracker.md`](homework-tracker.md) 更新狀態。

---

### Step 5｜更新課程索引

在下方 [課程索引](#4-課程索引) 表格新增一行：

```
| YYYY-MM-DD | Lesson NN | 主題 | [查看](transcripts/YYYY-MM-DD/lesson-NN-<slug>.md) | [查看](notes/YYYY-MM-DD/lesson-NN-<slug>-notes.md) | [查看](notes/YYYY-MM-DD/lesson-NN-<slug>-homework.md) |
```

---

## 3. 環境安裝（首次）

> 已安裝過可跳過。詳細說明見 [`scripts/INSTALL.md`](scripts/INSTALL.md)。

```bash
brew install ffmpeg
pip install --user openai-whisper
```

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
