---
name: english-lesson-review
description: Use when user provides an English class recording (.m4a/.mp3/.wav) or asks about the english-learning workflow. Triggers on phrases like "上課錄音", "英文課", "逐字稿", "課程筆記", "改作業", or when a recording file path is mentioned alongside English learning.
---

# English Lesson Review

> **唯一真相來源**：`english-learning/README.md`（3 步 SOP）。
> 本 skill 只是入口指引；細部行為與 Claude Code 版 skill 一致（`.claude/skills/english-lesson/SKILL.md`）。

## 每堂課 SOP（3 步）

### Step 1 — 轉譯

錄音檔丟進 `english-learning/recordings/`（根目錄），然後：

```bash
cd "/Users/Janice/Desktop/Git Hub workspace/personal-project/english-learning"
bash scripts/lesson.sh new
```

自動：解析日期 → 詢問主題 → Whisper 轉譯（medium，10–15 分）→ 歸檔錄音 → 產生逐字稿與筆記/作業模板。

### Step 2 — 筆記與作業

1. **產筆記**：AI 讀 `transcripts/日期/lesson-NN-<slug>.md`，直接填寫 `notes/.../lesson-NN-<slug>-notes.md`（學習目標、重點摘要、單字表 ≥10、老師糾正、文法重點）
2. **作業初稿由使用者自己寫**（不查字典、不代寫）
3. **改作業**：AI 對照逐字稿填「文法修正」表、「修改後完整版」、「自我複習重點」

### Step 3 — 收尾

```bash
python3 scripts/extract_vocab.py notes/日期/lesson-NN-<slug>-notes.md
bash scripts/update_index.sh
```

再更新 `homework-tracker.md` 狀態。

## Quick Reference

| 情境 | 做法 |
|------|------|
| 新課錄音 | `bash scripts/lesson.sh new` |
| 中文亂碼 / 幻覺重複 | `--model large` |
| 日期解析錯 | 加 `--date YYYY-MM-DD` |
| 找過去的課 | README 課程索引，或 `ls transcripts/` |
| 更新索引 | `bash scripts/update_index.sh`（自動，勿手動編表格） |

## 原則

- 錄音檔**絕不進 git**（.gitignore 已排除）
- 課堂編號 = 上課順序；腳本偵測到日期倒退會警告
- 作業初稿保留原樣，AI 只做修正與講解
