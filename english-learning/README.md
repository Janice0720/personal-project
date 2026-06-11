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

```
english-learning/
├── recordings/YYYY-MM-DD/lesson-NN-<主題>.m4a      ← 原始錄音備份
├── transcripts/YYYY-MM-DD/lesson-NN-<主題>.md      ← Whisper 逐字稿
├── notes/YYYY-MM-DD/lesson-NN-<主題>-notes.md      ← 課後學習筆記
└── scripts/
    ├── run.sh           ← 一鍵轉譯入口（用這個）
    ├── transcribe.py    ← Whisper 轉譯主腳本
    └── INSTALL.md       ← 環境安裝說明
```

---

## 2. 每堂課 SOP

### Step 1｜轉譯錄音（Terminal，約 4-5 分鐘）

```bash
cd "/Users/Janice/Desktop/Git Hub workspace/personal-project/english-learning"
bash scripts/run.sh /path/to/錄音檔.m4a --topic "今天的課程主題"
```

完成後自動產生：
- `transcripts/YYYY-MM-DD/lesson-NN-<主題>.md` — 逐字稿
- `notes/YYYY-MM-DD/lesson-NN-<主題>-notes.md` — 空白筆記範本

> **中英混合錄音品質不佳？** 改用較大模型：`--model medium`（約 10-15 分鐘）

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

### Step 3｜更新課程索引

在下方 [課程索引](#4-課程索引) 表格新增一行：

```
| YYYY-MM-DD | Lesson NN | 主題 | [查看](transcripts/YYYY-MM-DD/lesson-NN.md) | [查看](notes/YYYY-MM-DD/lesson-NN-notes.md) |
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
| 中文被轉成亂碼 | 改用 `--model medium` |
| 逐字稿編號跳號（lesson-02 而非 01） | 檢查 `transcripts/YYYY-MM-DD/` 是否有殘留舊檔並刪除 |

---

## 4. 課程索引

| 日期 | 課堂 | 主題 | 逐字稿 | 筆記 |
|------|------|------|--------|------|
| 2026-06-11 | Lesson 01 | 職場英文口說 — KYC 稽核 & 工作壓力 | [查看](transcripts/2026-06-11/lesson-01.md) | [查看](notes/2026-06-11/lesson-01-notes.md) |
