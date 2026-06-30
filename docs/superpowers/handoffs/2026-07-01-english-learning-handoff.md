# 對話交接：英文學習流程（english-learning）重構完成，待驗證與持續沿用

> **本檔用途**：上半部供**人類**快速瀏覽（專案摘要、目標、狀態）；全檔供**下一個 Agent** 還原上下文並續作。

> 建立時間：2026-07-01（對話當下）
> 原對話／工具：Claude Code

---

## 0. 專案摘要（人類可掃讀，3–8 行內）

- 專案／議題：個人英文課的錄音→逐字稿→筆記→作業→單字複習管理系統（`english-learning/`）。
- 目前一句話結論：六項改善已全部完成並 commit + push 到 `main`（commit `7e66258`）。
- 最緊急下一步：本機重跑一段「辨識較差」的舊錄音，驗證 Whisper 參數調整後幻覺（「Do. Do.」）是否消失。
- 主要風險或依賴：驗證需本機下載/執行 Whisper `medium` 模型，AI 端無法代跑。

---

## 1. 專案目標（Goals）

- 商業／使用者目標：用最低維護成本，持續記錄每堂英文課並真正記住內容（重點在**單字長期複習**與**作業迭代**）。
- 技術或交付物目標：
  - 一鍵把錄音轉成分類好的逐字稿＋筆記＋作業模板。
  - 中英混雜口說的轉譯品質可用（減少 Whisper 幻覺）。
  - 單字集中可匯入 Anki 做間隔複習。
  - repo 不被錄音大檔污染。
- 成功樣子（驗收）：每堂課跑完 SOP 五步即產生齊全檔案；單字進得了 Anki；錄音不進 git。

---

## 2. 進度與狀態總表（給人看也給 AI 用）

**狀態標籤**：進行中 / 待辦 / 未開始 / 已完成 / 卡住

### 2.1 工作項清單（必填表格）

| 編號 | 工作項（簡短） | 狀態 | 負責／備註 |
|------|----------------|------|------------|
| 1 | `.gitignore` 排除 recordings/ 與音訊，取消追蹤既有錄音 | 已完成 | commit `7e66258` |
| 2 | `transcribe.py`：Whisper 加 language=en / condition_on_previous_text=False / initial_prompt | 已完成 | 程式碼已改，**實際辨識效果未驗證** |
| 3 | `transcribe.py`：預設模型統一 medium、新增 `--slug`、全課程連續編號、自動產生作業模板 | 已完成 | `py_compile` 與 `--help` 已通過 |
| 4 | 單字系統：`extract_vocab.py` + `vocabulary/master-vocab.csv`（lesson-01 共 21 字）+ Anki 說明 | 已完成 | `--all` 已成功建表 |
| 5 | lesson-01 檔案改帶 slug（`kyc-career`）命名 + README 索引/結構/SOP 同步 | 已完成 | 用 git mv 保留歷史 |
| 6 | 新增 `homework-tracker.md` 與 SOP Step 4 作業流程 | 已完成 | — |
| 7 | **驗證**：重跑舊錄音確認 Whisper 幻覺改善 | 待辦 | 需使用者本機執行 medium 模型 |
| 8 | lesson-01 作業（containment system）課堂討論 | 卡住 | 等下一堂課；初稿/完整版已寫好 |
| 9 | 持續沿用新 SOP（每堂課五步） | 未開始 | 下一堂課起 |

### 2.2 目前整體進度（選填）

- 系統重構 6/6 完成並上線；剩「品質驗證」與「持續使用」兩類後續事項。

---

## 3. 需求與範圍（給 AI 細讀）

- 範圍：`english-learning/` 目錄內的流程與腳本；逐字稿/筆記/作業/單字的產生與彙整。
- 非目標／不做的事：
  - 不把原始錄音（.m4a 等）納入 git。
  - 不改動同 repo 內的 `personal-fincheck/`（本輪未觸碰）。

---

## 4. 已確定決策（不可輕易推翻）

- 檔名格式 `lesson-NN-<slug>`：`NN` 為**全課程連續編號**（跨日期遞增）；`<slug>` 為主題的英文短代稱。
- 主題中文保留在檔案標題與 README 課程索引；檔名只放 ASCII slug（使用者明確要求「保留主題」，以此折衷）。
- Whisper 預設 `--model medium`、`--language en`。
- 錄音一律由 `.gitignore` 排除，本機/雲端另行備份。
- 單字總表欄位：`word, pos, meaning, example, lesson, date_added`（Anki 友善）。

---

## 5. 詳細待辦與下一步（給下一個 Agent）

- [ ] （對應 §2-#7）請使用者本機跑：`bash scripts/run.sh <一段舊的、辨識差的錄音> --topic "測試" --slug test`，比對逐字稿是否還出現「Do. Do.」重複幻覺；若仍差，建議 `--model large`。
- [ ] （對應 §2-#8）下一堂課回答 lesson-01 作業（containment system），課後到 `homework-tracker.md` 把狀態改為「💬 已於課堂討論」。
- [ ] （對應 §2-#9）每堂新課照 SOP：轉譯 → 筆記 → `extract_vocab.py` 彙整單字 → 寫作業 → 更新 README 索引。
- [ ] （選配）若使用者要開始 Anki 複習，協助依 `vocabulary/README.md` 匯入 `master-vocab.csv`。

---

## 6. 相關路徑與指令

- 專案根：`/Users/Janice/Desktop/Git Hub workspace/personal-project/english-learning`
- 轉譯：`bash scripts/run.sh /path/to/錄音.m4a --topic "中文主題" --slug english-name`
- 彙整單字：`python3 scripts/extract_vocab.py notes/YYYY-MM-DD/lesson-NN-<slug>-notes.md`（或 `--all` 重建）
- 重要檔案：`scripts/transcribe.py`、`scripts/extract_vocab.py`、`README.md`、`homework-tracker.md`、`vocabulary/master-vocab.csv`、`vocabulary/README.md`
- 環境：需 `ffmpeg` + `openai-whisper`（見 `scripts/INSTALL.md`）；`run.sh` 會自動找已裝 whisper 的 Python。
- git：已 push 到 `main`，commit `7e66258`。

---

## 7. 假設與風險

- 假設使用者本機已安裝 whisper/ffmpeg（lesson-01 曾成功轉譯，故大致成立）。
- Whisper 參數改善「理論上」可減少幻覺，但**尚未實測**，可能仍需調 `--model` 或 `initial_prompt`。
- 此 repo 為個人專案、直接 push `main`（非分支 PR 流程），延續時沿用即可。

---

## 8. 給下一個 Agent 的一句話

請先協助使用者完成 §5 第一項（重跑舊錄音驗證轉譯品質）；其餘為每堂課的例行 SOP，照 README 執行即可，勿再把錄音加回 git。
