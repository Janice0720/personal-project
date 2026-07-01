#!/bin/bash
# 用途：自動選擇正確的 Python 環境來執行 update_index.py
# 使用：bash scripts/update_index.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

for PY in \
  "/opt/anaconda3/bin/python3" \
  "/opt/homebrew/bin/python3" \
  "/usr/local/bin/python3" \
  "$(which python3 2>/dev/null)"; do
  if [ -x "$PY" ]; then
    cd "$PROJECT_DIR"
    "$PY" scripts/update_index.py
    exit $?
  fi
done

echo "[錯誤] 找不到 Python 3 環境"
exit 1
