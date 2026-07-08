# English Learning 英文學習管理

個人英文課程錄音、逐字稿與課後筆記的管理系統。依日期與主題分類，支援快速複習與進度追蹤。

---

## 目錄

1. [每堂課 SOP（只有 3 步）](#1-每堂課-sop只有-3-步)
2. [資料夾結構](#2-資料夾結構)
3. [環境安裝（首次）](#3-環境安裝首次)
4. [課程索引](#4-課程索引)

---

## 1. 每堂課 SOP（只有 3 步）

> **上完課只要記住：丟檔案 → 跑一個指令 → 其他交給 Claude Code。**
> Claude Code 有對應的 skill（`.claude/skills/english-lesson/`），用自然語言呼叫即可。

### Step 1｜轉譯：丟檔案 + 一個指令

把手機/Zoom 的錄音檔直接丟進 `recordings/` 資料夾（不用改名、不用建子資料夾），然後：

```bash
cd "/Users/Janice/Desktop/Git Hub workspace/personal-project/english-learning"
bash scripts/lesson.sh new
```

腳本會自動：偵測新錄音 → 從檔名解析上課日期 → 詢問主題 → Whisper 轉譯（約 10–15 分鐘）→ 歸檔錄音 → 產生逐字稿與筆記/作業模板 → 印出後續 checklist。

> 也可以直接開 Claude Code 說 **「處理新課錄音」**，連指令都不用打——它還會順便讀逐字稿、把筆記填好、幫你把老師指派的作業登記到 tracker。

### Step 2｜學習：寫作業初稿 → 請 AI 修正

1. 打開 `notes/日期/lesson-NN-<slug>-homework.md`，在「我的初稿」**自己寫**（不查字典，保留原樣才看得出進步）
2. 寫完後開 Claude Code 說 **「幫我改作業」**——它會對照這堂課的逐字稿填好文法修正表、完整版與複習重點

### Step 3｜收尾：一句話

開 Claude Code 說 **「幫我收尾這堂課」**——單字進總表、README 索引重建、tracker 狀態更新，一次做完。

（手動等效指令：`python3 scripts/extract_vocab.py <notes檔>` → `bash scripts/update_index.sh` → 編輯 `homework-tracker.md`）

---

## 2. 資料夾結構

> 檔名格式：`lesson-NN-<slug>`。`NN` 為**全課程連續編號，依上課日期遞增**（＝第幾堂課）；`<slug>` 是主題的英文短代稱。主題完整中文記在檔案標題與課程索引。

```
english-learning/
├── recordings/                                      ← 新錄音先丟這裡（根目錄）
│   └── YYYY-MM-DD/lesson-NN-<slug>.m4a              ← 處理後自動歸檔（不進 git）
├── transcripts/YYYY-MM-DD/lesson-NN-<slug>.md       ← Whisper 逐字稿
├── notes/YYYY-MM-DD/
│   ├── lesson-NN-<slug>-notes.md                    ← 課後學習筆記
│   └── lesson-NN-<slug>-homework.md                 ← 作業（初稿→修正→完整版）
├── vocabulary/
│   ├── master-vocab.csv                             ← 所有課堂單字總表（可匯入 Anki）
│   └── README.md                                    ← 單字複習 / Anki 匯入說明
├── homework-tracker.md                              ← 作業狀態追蹤
└── scripts/
    ├── lesson.sh          ← ★ 每堂課的單一入口（bash scripts/lesson.sh new）
    ├── run.sh / transcribe.py    ← Whisper 轉譯（lesson.sh 會自動呼叫）
    ├── notes.sh / generate_notes.py ← 筆記模板產生（Claude Code 讀逐字稿直接填寫更佳）
    ├── extract_vocab.py   ← 筆記單字彙整到總表
    ├── update_index.sh / update_index.py ← 課程索引自動更新
    └── INSTALL.md         ← 環境安裝說明
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
| `whisper not found` | 用 `bash scripts/lesson.sh`，會自動找正確 Python |
| 中文被轉成亂碼 / 出現「Do. Do.」 | 預設已鎖 `--language en`；仍不佳改 `--model large` |
| 錄音檔日期解析錯誤 | 加 `--date 2026-07-01` 手動指定 |
| 編號和上課順序不符 | 編號依處理順序遞增；當堂課錄音當週處理就不會亂（腳本偵測到日期倒退會警告） |

---

## 4. 課程索引

| 日期 | 課堂 | 主題 | 逐字稿 | 筆記 | 作業 |
|------|------|------|--------|------|------|
| 2026-06-04 | Lesson 01 | Intro — 自我介紹與職涯願景 | [查看](transcripts/2026-06-04/lesson-01-intro.md) | [查看](notes/2026-06-04/lesson-01-intro-notes.md) | [查看](notes/2026-06-04/lesson-01-intro-homework.md) |
| 2026-06-11 | Lesson 02 | 職場英文口說練習 — KYC 稽核 & 工作壓力 | [查看](transcripts/2026-06-11/lesson-02-kyc-career.md) | [查看](notes/2026-06-11/lesson-02-kyc-career-notes.md) | [查看](notes/2026-06-11/lesson-02-kyc-career-homework.md) |
| 2026-07-01 | Lesson 03 | 職場電話英文 — 接聽國外機構來電與專業界線 | [查看](transcripts/2026-07-01/lesson-03-phone-english.md) | [查看](notes/2026-07-01/lesson-03-phone-english-notes.md) | [查看](notes/2026-07-01/lesson-03-phone-english-homework.md) |
| 2026-07-08 | Lesson 04 | 職場數學週 — 國泰證券淨值重算與帳務補償計算 | — | [查看](notes/2026-07-08/lesson-04-nav-recalculation-notes.md) | [查看](notes/2026-07-08/lesson-04-nav-recalculation-homework.md) |
