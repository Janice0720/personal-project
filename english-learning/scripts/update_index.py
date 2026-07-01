#!/usr/bin/env python3
"""
update_index.py
用途：掃描 transcripts/ 資料夾，自動重建並更新 README.md 的課程索引表格
使用：python3 scripts/update_index.py
"""

import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
TRANSCRIPTS_DIR = PROJECT_DIR / "transcripts"
NOTES_DIR = PROJECT_DIR / "notes"
README_PATH = PROJECT_DIR / "README.md"

INDEX_MARKER = "## 4. 課程索引"


def read_topic(transcript_path: Path) -> str:
    """從逐字稿標題行讀取課程主題"""
    try:
        content = transcript_path.read_text(encoding="utf-8")
        m = re.search(r"^# Lesson \d+：(.+)$", content, re.MULTILINE)
        return m.group(1).strip() if m else "（未命名）"
    except Exception:
        return "（未命名）"


def build_table() -> str:
    """掃描所有逐字稿，產生 Markdown 索引表格（含表頭）"""
    header = "| 日期 | 課堂 | 主題 | 逐字稿 | 筆記 | 作業 |"
    divider = "|------|------|------|--------|------|------|"

    rows = []
    for transcript_path in sorted(TRANSCRIPTS_DIR.glob("*/lesson-*.md")):
        date_str = transcript_path.parent.name
        stem = transcript_path.stem  # e.g. lesson-01-kyc-career

        num_match = re.search(r"lesson-(\d+)", stem)
        if not num_match:
            continue
        lesson_label = f"Lesson {int(num_match.group(1)):02d}"
        topic = read_topic(transcript_path)

        transcript_link = f"[查看](transcripts/{date_str}/{stem}.md)"
        notes_file = NOTES_DIR / date_str / f"{stem}-notes.md"
        hw_file = NOTES_DIR / date_str / f"{stem}-homework.md"
        notes_link = f"[查看](notes/{date_str}/{stem}-notes.md)" if notes_file.exists() else "—"
        hw_link = f"[查看](notes/{date_str}/{stem}-homework.md)" if hw_file.exists() else "—"

        rows.append(f"| {date_str} | {lesson_label} | {topic} | {transcript_link} | {notes_link} | {hw_link} |")

    lines = [header, divider] + rows
    return "\n".join(lines) + "\n"


def update_readme(table: str) -> None:
    """將課程索引區段替換為新表格"""
    content = README_PATH.read_text(encoding="utf-8")

    idx = content.find(INDEX_MARKER)
    if idx == -1:
        print(f"[錯誤] 在 README.md 中找不到 '{INDEX_MARKER}' 標題")
        sys.exit(1)

    # 保留標題行之前的所有內容（含標題本身）
    before = content[: idx + len(INDEX_MARKER)]
    README_PATH.write_text(f"{before}\n\n{table}", encoding="utf-8")


def main():
    if not TRANSCRIPTS_DIR.exists():
        print(f"[錯誤] 找不到 transcripts/ 資料夾：{TRANSCRIPTS_DIR}")
        sys.exit(1)

    print("🔍 掃描課程資料夾…")
    table = build_table()

    lesson_count = table.count("\n|") - 1  # 排除表頭與分隔列
    print(f"   找到 {lesson_count} 堂課")

    print("📝 更新 README.md 課程索引…")
    update_readme(table)

    print(f"✅ 課程索引已更新：{README_PATH.relative_to(PROJECT_DIR)}")


if __name__ == "__main__":
    main()
