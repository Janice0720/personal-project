#!/bin/bash
# 用途：自動選擇正確的 Python 環境來執行轉譯腳本
# 使用：bash scripts/run.sh /path/to/recording.m4a [--topic "主題"] [--model medium]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# 依序找 Python（優先 Anaconda，其次系統）
for PY in \
  "/opt/anaconda3/bin/python3" \
  "/opt/homebrew/bin/python3" \
  "/usr/local/bin/python3" \
  "$(which python3 2>/dev/null)"; do
  if [ -x "$PY" ] && "$PY" -c "import whisper" 2>/dev/null; then
    echo "✓ 使用 Python：$PY"
    export PATH="$PATH:/opt/homebrew/bin"
    cd "$PROJECT_DIR"
    "$PY" scripts/transcribe.py "$@"
    exit $?
  fi
done

echo "[錯誤] 找不到安裝了 openai-whisper 的 Python 環境"
echo "請參考 scripts/INSTALL.md 安裝"
exit 1
