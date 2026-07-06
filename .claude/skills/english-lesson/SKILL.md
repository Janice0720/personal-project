---
name: english-lesson
description: 英文課學習流程助理。當使用者提到「處理新課錄音」「上完英文課」「產出課程筆記」「幫我改作業」「英文作業」「收尾這堂課」，或提供英文課錄音檔路徑時使用。涵蓋：轉譯、筆記產出、作業文法修正、單字彙整、索引與 tracker 更新。
---

# English Lesson 流程助理

專案位置：`english-learning/`（相對於 repo 根目錄）。
完整 SOP 見 `english-learning/README.md`；本 skill 定義 Claude Code 在每個階段該做什麼。

## 使用者只需記住三句話

| 使用者說 | 你做什麼 |
|---------|---------|
| 「處理新課錄音」 | 階段 A：轉譯 + 產筆記 |
| 「幫我改作業」 | 階段 B：作業文法修正 |
| 「幫我收尾這堂課」 | 階段 C：單字 / 索引 / tracker |

---

## 階段 A｜處理新課錄音

1. 執行 `bash scripts/lesson.sh new`（自動偵測 `recordings/` 根目錄的新錄音；轉譯 10–15 分鐘，放背景跑）。
   - 若使用者給了檔案路徑，改用 `bash scripts/lesson.sh <路徑>`。
   - 主題未知時先用 `--topic "待定" --slug tbd`，轉譯完成後讀逐字稿判斷主題，再把逐字稿/筆記/作業/錄音檔名中的 slug 與標題改為正確主題。
2. 轉譯完成後**親自讀逐字稿**，直接把 `notes/日期/lesson-NN-<slug>-notes.md` 填寫完整（不要留空模板、不需 API key 的 generate_notes.py）：
   - 今日學習目標（2–3 條）
   - 課堂重點摘要（3–5 條）
   - 重點單字／片語表（≥10 個，只取老師明確教授、示範或糾正的；例句用逐字稿原句）
   - 老師的關鍵糾正表（學生原句 → 老師建議；沒有就標註無）
   - 文法重點
3. 從逐字稿找出**老師指派的作業**，寫進 `-homework.md` 的「題目」與「繳交日期」，並在 `homework-tracker.md` 加一列（狀態 ⬜）。
4. 提醒使用者：「作業初稿請自己寫（不查字典），寫完說『幫我改作業』」。

## 階段 B｜幫我改作業

前提:使用者已在 `-homework.md` 的「我的初稿」寫好內容。若初稿是空的，請他先寫，**不要代寫初稿**（初稿保留原汁原味是這個學習法的核心）。

1. 讀該堂課的 homework 檔＋逐字稿（了解課堂教過什麼）。
2. 填「文法修正」表：原句 → 問題 → 建議（優先指出與課堂教學內容相關的錯誤）。
3. 填「修改後完整版」：整合修正、貼近使用者原意，不過度改寫。
4. 填「自我複習重點」：抽出 3–5 個值得記的句型與單字。
5. 更新 `homework-tracker.md` 狀態為 ✅ 已完成（待課堂討論）。

## 階段 C｜收尾這堂課

依序執行：

```bash
cd english-learning
python3 scripts/extract_vocab.py notes/日期/lesson-NN-<slug>-notes.md   # 單字入總表
bash scripts/update_index.sh                                            # 重建 README 課程索引
```

再檢查 `homework-tracker.md` 狀態是否正確，最後詢問使用者是否 commit + push。

---

## 注意事項

- **錄音檔絕不進 git**（`.gitignore` 已排除）；`lesson.sh` 會自動歸檔並清理根目錄原始檔。
- 課堂編號 = 上課順序（依日期遞增）。若 `transcribe.py` 印出日期順序警告，先跟使用者確認再繼續。
- 逐字稿是 Whisper 自動產生，可能有辨識錯誤；筆記中引用例句時如明顯是辨識錯誤，修正拼寫但保留原意。
- 課後複習節奏與 Anki 匯入見 `vocabulary/README.md`。
