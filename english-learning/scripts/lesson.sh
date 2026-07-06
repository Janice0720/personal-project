#!/bin/bash
# ═══════════════════════════════════════════════════════════════
# lesson.sh — 每堂課的「單一入口」
#
# 上完課只要做兩件事：
#   1. 把手機/Zoom 的錄音檔丟進 recordings/ 資料夾（根目錄即可）
#   2. 執行：bash scripts/lesson.sh new
#
# 其他用法：
#   bash scripts/lesson.sh new                    # 自動偵測 recordings/ 根目錄的新錄音
#   bash scripts/lesson.sh /path/to/錄音.m4a      # 直接指定檔案
#   （兩種用法都可加 --topic "主題" --slug english-name，
#     不加的話轉譯時會互動式詢問）
# ═══════════════════════════════════════════════════════════════

set -u
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
RECORDINGS_DIR="$PROJECT_DIR/recordings"

# ── 解析參數 ──────────────────────────────────────────────────
if [ $# -lt 1 ]; then
  echo "用法：bash scripts/lesson.sh new                # 自動偵測新錄音"
  echo "      bash scripts/lesson.sh <錄音檔路徑>       # 指定檔案"
  echo "      （可加 --topic \"主題\" --slug english-name）"
  exit 1
fi

TARGET="$1"
shift  # 其餘參數（--topic/--slug/--model 等）原樣傳給 transcribe.py

# ── new 模式：自動偵測 recordings/ 根目錄的錄音檔 ─────────────
if [ "$TARGET" = "new" ]; then
  # 只找根目錄（不含日期子資料夾）的音訊檔
  CANDIDATES=()
  while IFS= read -r -d '' f; do
    CANDIDATES+=("$f")
  done < <(find "$RECORDINGS_DIR" -maxdepth 1 -type f \
           \( -iname '*.m4a' -o -iname '*.mp3' -o -iname '*.wav' -o -iname '*.aac' \) -print0)

  if [ ${#CANDIDATES[@]} -eq 0 ]; then
    echo "找不到待處理的錄音檔。"
    echo "請先把錄音檔放到：$RECORDINGS_DIR/"
    exit 1
  fi
  if [ ${#CANDIDATES[@]} -gt 1 ]; then
    echo "偵測到多個待處理錄音檔，請一次處理一個："
    printf '  %s\n' "${CANDIDATES[@]}"
    echo "指定檔案執行：bash scripts/lesson.sh <上面其中一個路徑>"
    exit 1
  fi
  TARGET="${CANDIDATES[0]}"
  echo "🎙  偵測到新錄音：$(basename "$TARGET")"
fi

if [ ! -f "$TARGET" ]; then
  echo "[錯誤] 找不到錄音檔：$TARGET"
  exit 1
fi

# ── Step 1：轉譯（transcribe.py 會自動歸檔錄音到 recordings/日期/）──
bash "$SCRIPT_DIR/run.sh" "$TARGET" "$@"
STATUS=$?
if [ $STATUS -ne 0 ]; then
  echo ""
  echo "❌ 轉譯失敗（原始錄音檔保留原位，未刪除）"
  exit $STATUS
fi

# ── Step 2：轉譯成功後，清掉 recordings/ 根目錄的原始檔 ──────
#    （transcribe.py 已將錄音複製進 recordings/日期/lesson-NN-slug.m4a）
case "$TARGET" in
  "$RECORDINGS_DIR"/*)
    if [ "$(dirname "$TARGET")" = "$RECORDINGS_DIR" ]; then
      rm "$TARGET"
      echo "  ✓ 原始檔已清除（歸檔版本保留在 recordings/日期/ 內）"
    fi
    ;;
esac

# ── Step 3：印出接下來要做的事 ────────────────────────────────
cat <<'CHECKLIST'

═══════════════════════════════════════════════
✅ 轉譯完成！接下來（可請 Claude Code 代勞）：

  【學習】
  1. 產出筆記：開 Claude Code 說「幫我產出最新一堂課的筆記」
     （或手動：bash scripts/notes.sh --latest）
  2. 寫作業初稿：打開 notes/日期/lesson-NN-*-homework.md
     自己先寫「我的初稿」（不查字典）
  3. 改作業：初稿寫完後，開 Claude Code 說「幫我改作業」

  【收尾】（也可請 Claude Code 一句話做完：「幫我收尾這堂課」）
  4. 單字入總表：python3 scripts/extract_vocab.py <notes檔>
  5. 更新索引：bash scripts/update_index.sh
  6. 更新 homework-tracker.md 的作業狀態
═══════════════════════════════════════════════
CHECKLIST
