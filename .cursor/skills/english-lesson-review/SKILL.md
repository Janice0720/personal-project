---
name: english-lesson-review
description: Use when user provides an English class recording (.m4a/.mp3/.wav) and wants a transcript plus structured study notes. Triggers on phrases like "上課錄音", "英文課", "逐字稿", "課程筆記", or when a recording file path is mentioned alongside English learning.
---

# English Lesson Review

## Overview

Two-step, token-efficient workflow for English class recordings:
1. **Local Whisper** (0 tokens) → transcript Markdown file
2. **Composer prompt** (low tokens, no history) → study notes

Never use Agent for the analysis step — Composer reads only the transcript + short prompt.

## Workflow

### Step 1 — Transcribe (Shell, 0 tokens)

```bash
cd "/Users/Janice/Desktop/Git Hub workspace/personal-project/english-learning"
bash scripts/run.sh /path/to/recording.m4a --topic "課程主題" --model small
```

Outputs:
- `transcripts/YYYY-MM-DD/lesson-NN-<topic>.md`
- `notes/YYYY-MM-DD/lesson-NN-<topic>-notes.md` (empty template)

> Model guide: `small` = fast (4-5 min, good enough); `medium` = slower (10-15 min, better accuracy)

### Step 2 — Analyze (Composer, low tokens)

Open **Composer**, paste the prompt below, then paste the full transcript content at the end.
Composer outputs the completed notes; copy-paste into `notes/.../lesson-NN-notes.md`.

---

## Composer Prompt Template

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
[在此貼上 transcripts/YYYY-MM-DD/lesson-NN.md 的逐字稿內容]
```

---

## File Structure

```
english-learning/
├── recordings/YYYY-MM-DD/lesson-NN-<topic>.m4a
├── transcripts/YYYY-MM-DD/lesson-NN-<topic>.md   ← Whisper output
├── notes/YYYY-MM-DD/lesson-NN-<topic>-notes.md   ← Composer output (copy here)
└── scripts/
    ├── run.sh          ← one-command entry point
    └── transcribe.py   ← Whisper wrapper
```

## Quick Reference

| 情境 | 做法 |
|------|------|
| 新課錄音 → 逐字稿 | `bash scripts/run.sh <file> --topic "..."` |
| 逐字稿 → 筆記 | Composer + 上方 prompt template |
| 中文消失 / 亂碼 | 改用 `--model medium`（較慢但更準） |
| 找過去的課 | `ls transcripts/` 或 `notes/` |
| 更新 README 索引 | 手動在 `README.md` 的表格加一行 |

## Common Mistakes

| 問題 | 原因 | 解法 |
|------|------|------|
| 中文被轉成亂碼英文 | `small` 模型中英切換弱 | 改 `--model medium` |
| 逐字稿存成 lesson-02（而非 lesson-01） | 前次轉譯留有殘檔 | 檢查 `transcripts/YYYY-MM-DD/` 並刪除重複 |
| `whisper` not found | 使用了錯誤的 Python | 用 `bash scripts/run.sh`（自動選正確 Python） |
