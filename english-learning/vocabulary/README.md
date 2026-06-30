# 單字總表與複習

集中管理所有課堂單字，並用 **Anki 間隔複習（spaced repetition）** 來真正記住它們。

## 檔案

- `master-vocab.csv` — 所有課堂單字的總表（欄位：word, pos, meaning, example, lesson, date_added）

## 如何更新總表

每次完成課後筆記後，從筆記抽取單字到總表：

```bash
cd "/Users/Janice/Desktop/Git Hub workspace/personal-project/english-learning"

# 方式一：只加入某一課（自動去重）
python3 scripts/extract_vocab.py notes/2026-06-11/lesson-01-kyc-career-notes.md

# 方式二：掃描所有筆記、重建整份總表
python3 scripts/extract_vocab.py --all
```

> 去重邏輯：以單字本身（去掉括號註解、不分大小寫）為準，重複的不會再加。

## 如何匯入 Anki 複習

1. 打開 Anki → `File` → `Import`，選擇 `master-vocab.csv`
2. Type 選 **Basic**，分隔符選 **Comma**，勾選 **Allow HTML**
3. 欄位對應建議：
   - Field 1（Front 正面）→ `word`
   - Field 2（Back 背面）→ `meaning`（可再手動把 example 併入背面）
4. 之後每天打開 Anki 複習，系統會依遺忘曲線自動安排該複習哪些字

> 想做「看中文 → 說英文」的反向卡，可在 Anki 的卡片樣板加一個反向 Card 2。

## 複習節奏建議（上班族版）

- 每天 5–10 分鐘 Anki（通勤時手機就能做）
- 每週日快速掃一次 `master-vocab.csv`，把這週新字唸出聲、各造一個跟工作相關的句子
