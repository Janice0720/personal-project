#!/usr/bin/env python3
"""
單字彙整腳本
用途：從課後筆記（notes/*.md）的「重點單字／片語」表格抽取單字，
      彙整（去重）到 vocabulary/master-vocab.csv，供長期複習與匯入 Anki。

使用：
    python3 extract_vocab.py notes/2026-06-11/lesson-01-....-notes.md
    python3 extract_vocab.py --all          # 掃描 notes/ 下所有筆記重建總表
"""

import argparse
import csv
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
NOTES_DIR = PROJECT_DIR / "notes"
VOCAB_DIR = PROJECT_DIR / "vocabulary"
MASTER_CSV = VOCAB_DIR / "master-vocab.csv"

# Anki 友善欄位（直接匯入即可：word 當正面，其餘當背面）
FIELDS = ["word", "pos", "meaning", "example", "lesson", "date_added"]


def clean_cell(text: str) -> str:
    """去掉 Markdown 粗體標記與多餘空白"""
    text = text.replace("**", "").strip()
    return re.sub(r"\s+", " ", text)


def norm_key(word: str) -> str:
    """單字去重用的正規化鍵：去括號註解、轉小寫"""
    word = re.sub(r"\(.*?\)|（.*?）", "", word)  # 去掉 (Know Your Customer) 之類註解
    return clean_cell(word).lower()


def parse_lesson_date(md_path: Path) -> tuple[str, str]:
    """從檔名/路徑解析 lesson 編號與日期"""
    m = re.search(r"lesson-(\d+)", md_path.stem)
    lesson = f"Lesson {int(m.group(1)):02d}" if m else md_path.stem
    dm = re.search(r"(\d{4}-\d{2}-\d{2})", str(md_path))
    date = dm.group(1) if dm else ""
    return lesson, date


def extract_rows(md_path: Path) -> list[dict]:
    """從一份筆記抽取單字表格列"""
    lesson, date = parse_lesson_date(md_path)
    lines = md_path.read_text(encoding="utf-8").splitlines()

    rows = []
    in_vocab_table = False
    for line in lines:
        stripped = line.strip()
        # 找到含「單字」的表頭即視為單字表開始
        if stripped.startswith("|") and "單字" in stripped:
            in_vocab_table = True
            continue
        if not in_vocab_table:
            continue
        if not stripped.startswith("|"):
            in_vocab_table = False  # 表格結束
            continue
        if re.match(r"^\|[\s\-:|]+\|$", stripped):
            continue  # 分隔列 |---|---|

        cells = [clean_cell(c) for c in stripped.strip("|").split("|")]
        if len(cells) < 3 or not cells[0]:
            continue
        # 容忍 3 欄（無詞性）或 4 欄（含詞性）
        if len(cells) >= 4:
            word, pos, meaning, example = cells[0], cells[1], cells[2], cells[3]
        else:
            word, pos, meaning, example = cells[0], "", cells[1], cells[2]
        rows.append(
            {
                "word": word,
                "pos": pos,
                "meaning": meaning,
                "example": example,
                "lesson": lesson,
                "date_added": date,
            }
        )
    return rows


def load_existing() -> tuple[list[dict], set]:
    if not MASTER_CSV.exists():
        return [], set()
    with MASTER_CSV.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    keys = {norm_key(r["word"]) for r in rows}
    return rows, keys


def write_master(rows: list[dict]) -> None:
    VOCAB_DIR.mkdir(parents=True, exist_ok=True)
    with MASTER_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description="從課後筆記彙整單字至 master-vocab.csv")
    parser.add_argument("notes", nargs="?", help="單一筆記檔路徑")
    parser.add_argument("--all", action="store_true", help="掃描 notes/ 下所有 *-notes.md 重建總表")
    args = parser.parse_args()

    if args.all:
        master_rows = []
        seen = set()
        for md in sorted(NOTES_DIR.glob("*/*-notes.md")):
            for row in extract_rows(md):
                k = norm_key(row["word"])
                if k and k not in seen:
                    seen.add(k)
                    master_rows.append(row)
        write_master(master_rows)
        print(f"✅ 已重建 {MASTER_CSV.relative_to(PROJECT_DIR)}，共 {len(master_rows)} 個單字")
        return

    if not args.notes:
        parser.error("請提供筆記檔路徑，或使用 --all")

    md_path = Path(args.notes).expanduser().resolve()
    if not md_path.exists():
        print(f"[錯誤] 找不到筆記檔：{md_path}")
        sys.exit(1)

    master_rows, seen = load_existing()
    added = 0
    for row in extract_rows(md_path):
        k = norm_key(row["word"])
        if k and k not in seen:
            seen.add(k)
            master_rows.append(row)
            added += 1

    write_master(master_rows)
    print(f"✅ 從 {md_path.name} 新增 {added} 個單字（總表現有 {len(master_rows)} 個）")
    print(f"   檔案：{MASTER_CSV}")


if __name__ == "__main__":
    main()
