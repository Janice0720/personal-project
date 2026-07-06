#!/usr/bin/env python3
"""
English Learning Transcription Script
用途：將英文課程錄音轉成 Markdown 逐字稿，並依日期/主題自動分類
使用：python3 transcribe.py <錄音檔路徑> [--topic "課程主題"] [--slug english-name] [--date "2026-06-11"] [--model medium]
"""

import argparse
import os
import sys
import re
import shutil
from datetime import datetime
from pathlib import Path

# ─── 設定根目錄 ────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
RECORDINGS_DIR = PROJECT_DIR / "recordings"
TRANSCRIPTS_DIR = PROJECT_DIR / "transcripts"
NOTES_DIR = PROJECT_DIR / "notes"


def parse_timestamp_from_filename(filename: str) -> str | None:
    """從 Zoom/錄音 app 產生的時間戳記檔名解析日期，例如 1781183036899_1115.M4A"""
    match = re.match(r"(\d{10,13})", filename)
    if match:
        ts_str = match.group(1)
        ts = int(ts_str)
        if len(ts_str) == 13:
            ts //= 1000
        try:
            return datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
        except Exception:
            pass
    return None


def sanitize_filename(text: str) -> str:
    """將主題文字轉為安全的檔名"""
    text = text.strip().lower()
    text = re.sub(r"[^\w\s\-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text[:60]


def find_next_lesson_number(transcripts_root: Path) -> int:
    """找下一個課堂編號（全課程連續編號：掃描所有日期資料夾取最大值 + 1）"""
    nums = []
    for f in transcripts_root.glob("*/lesson-*.md"):
        m = re.match(r"lesson-(\d+)", f.stem)
        if m:
            nums.append(int(m.group(1)))
    return max(nums) + 1 if nums else 1


def warn_if_date_out_of_order(transcripts_root: Path, date_str: str) -> None:
    """編號依處理順序遞增；若這堂課的日期早於已有課程，編號會與日期順序不一致，先提醒"""
    existing_dates = [d.name for d in transcripts_root.iterdir() if d.is_dir()]
    if existing_dates and date_str < max(existing_dates):
        print(f"⚠️  注意：這堂課日期（{date_str}）早於已有課程（最晚 {max(existing_dates)}），")
        print("    自動編號會晚於日期較新的課。若要維持「編號=上課順序」，請手動重編舊檔後再跑。")


def copy_recording(src: Path, date_str: str, lesson_num: int, file_slug: str) -> Path:
    """將錄音檔複製到 recordings/{date}/ 並重新命名"""
    dest_dir = RECORDINGS_DIR / date_str
    dest_dir.mkdir(parents=True, exist_ok=True)
    suffix = src.suffix.lower()
    slug_part = f"-{file_slug}" if file_slug else ""
    dest_name = f"lesson-{lesson_num:02d}{slug_part}{suffix}"
    dest = dest_dir / dest_name
    if not dest.exists():
        shutil.copy2(src, dest)
        print(f"  ✓ 錄音檔已複製至 {dest.relative_to(PROJECT_DIR)}")
    return dest


# 給 Whisper 的領域提示：課堂主要為英文口說，含金融/職場/數據分析詞彙。
# 提供 initial_prompt 能讓專業詞（KYC、mutual fund 等）更準確。
DEFAULT_PROMPT = (
    "This is an English speaking lesson about finance, securities, KYC, "
    "investment, data analysis, and career topics."
)


def transcribe_audio(
    audio_path: Path,
    model_name: str = "medium",
    language: str = "en",
    initial_prompt: str = DEFAULT_PROMPT,
) -> str:
    """使用 OpenAI Whisper 轉譯音訊，回傳逐字稿文字"""
    try:
        import whisper
    except ImportError:
        print("\n[錯誤] 尚未安裝 openai-whisper，請先執行：")
        print("  pip install openai-whisper")
        print("  或依照 scripts/INSTALL.md 的指引安裝\n")
        sys.exit(1)

    print(f"  ⏳ 正在載入 Whisper {model_name} 模型（首次載入需下載，請稍候）…")
    model = whisper.load_model(model_name)

    print(f"  ⏳ 正在轉譯音訊（{audio_path.name}，語言={language}）…")
    result = model.transcribe(
        str(audio_path),
        verbose=False,
        language=language,
        # 抑制「Do. Do. Do.」這類在靜音/停頓段的重複幻覺
        condition_on_previous_text=False,
        initial_prompt=initial_prompt,
    )
    return result["text"]


def build_transcript_md(
    transcript_text: str,
    date_str: str,
    lesson_num: int,
    topic: str,
    audio_filename: str,
) -> str:
    """組合 Markdown 逐字稿內容"""
    topic_display = topic if topic else "（未命名課程）"
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    paragraphs = []
    sentences = re.split(r"(?<=[.!?])\s+", transcript_text.strip())
    chunk, count = [], 0
    for s in sentences:
        chunk.append(s)
        count += 1
        if count >= 5:
            paragraphs.append(" ".join(chunk))
            chunk, count = [], 0
    if chunk:
        paragraphs.append(" ".join(chunk))

    body = "\n\n".join(paragraphs)

    return f"""# Lesson {lesson_num:02d}：{topic_display}

**日期**：{date_str}
**來源錄音**：`{audio_filename}`
**轉譯時間**：{now}
**模型**：OpenAI Whisper

---

## 逐字稿

{body}

---

## 學習筆記（待填寫）

> 請在課後補充重點單字、文法、或老師的重要說明。

| 單字／片語 | 中文意思 | 例句 |
|-----------|---------|------|
|           |         |      |

---

*此逐字稿由 Whisper 自動生成，若有錯誤請手動修正。*
"""


def create_notes_template(date_str: str, lesson_num: int, topic: str, file_slug: str) -> Path:
    """建立空白課後筆記範本"""
    notes_dir = NOTES_DIR / date_str
    notes_dir.mkdir(parents=True, exist_ok=True)
    slug_part = f"-{file_slug}" if file_slug else ""
    notes_path = notes_dir / f"lesson-{lesson_num:02d}{slug_part}-notes.md"

    if not notes_path.exists():
        topic_display = topic if topic else "（未命名課程）"
        notes_path.write_text(
            f"""# 課後筆記 — Lesson {lesson_num:02d}：{topic_display}

**日期**：{date_str}

---

## 今日學習目標

- 

## 重點摘要

- 

## 單字／片語

| 單字／片語 | 詞性 | 中文意思 | 例句 |
|-----------|------|---------|------|
|           |      |         |      |

## 文法重點

- 

## 作業 / 下次複習

- 
""",
            encoding="utf-8",
        )
        print(f"  ✓ 課後筆記範本已建立 {notes_path.relative_to(PROJECT_DIR)}")
    return notes_path


def create_homework_template(
    date_str: str, lesson_num: int, topic: str, file_slug: str
) -> Path:
    """建立作業範本（題目／初稿／文法修正／完整版／複習重點）"""
    notes_dir = NOTES_DIR / date_str
    notes_dir.mkdir(parents=True, exist_ok=True)
    slug_part = f"-{file_slug}" if file_slug else ""
    hw_path = notes_dir / f"lesson-{lesson_num:02d}{slug_part}-homework.md"

    if not hw_path.exists():
        topic_display = topic if topic else "（未命名課程）"
        hw_path.write_text(
            f"""# 作業 — Lesson {lesson_num:02d}：{topic_display}

**題目**：（填入老師指派的題目）
**繳交日期**：

---

## 我的初稿

（先不查字典、用自己會的句子寫，保留原汁原味方便事後對照）

---

## 文法修正

| 原句 | 問題 | 建議 |
|------|------|------|
|      |      |      |

---

## 修改後完整版

（整合修正後的完整版本）

---

## 自我複習重點

-
""",
            encoding="utf-8",
        )
        print(f"  ✓ 作業範本已建立 {hw_path.relative_to(PROJECT_DIR)}")
    return hw_path


def main():
    parser = argparse.ArgumentParser(description="英文課錄音逐字稿轉換工具")
    parser.add_argument("audio", help="錄音檔路徑（.m4a / .mp3 / .wav 等）")
    parser.add_argument("--topic", "-t", default="", help="課程主題（可中文，顯示於標題與索引，例如：職場英文口說）")
    parser.add_argument(
        "--slug",
        "-s",
        default="",
        help="檔名用的英文短代稱（選填；未提供時自動從 --topic 衍生）。例如：kyc-career",
    )
    parser.add_argument("--date", "-d", default="", help="上課日期 YYYY-MM-DD（預設自動從檔名解析）")
    parser.add_argument(
        "--model",
        "-m",
        default="medium",
        choices=["tiny", "base", "small", "medium", "large"],
        help="Whisper 模型大小（越大越準確，但越慢；中英混雜口說課建議 medium，預設 medium）",
    )
    parser.add_argument(
        "--language",
        "-l",
        default="en",
        help="主要語言（預設 en；課堂主要說英文時鎖定 en 可大幅減少亂碼）",
    )
    parser.add_argument(
        "--no-copy",
        action="store_true",
        help="不複製錄音檔至 recordings/ 資料夾",
    )
    args = parser.parse_args()

    audio_path = Path(args.audio).expanduser().resolve()
    if not audio_path.exists():
        print(f"[錯誤] 找不到錄音檔：{audio_path}")
        sys.exit(1)

    # ── 決定日期 ──
    date_str = args.date
    if not date_str:
        date_str = parse_timestamp_from_filename(audio_path.name)
    if not date_str:
        date_str = datetime.fromtimestamp(audio_path.stat().st_mtime).strftime("%Y-%m-%d")
    print(f"\n📅 上課日期：{date_str}")

    # ── 課題目 ──
    topic = args.topic
    if not topic:
        topic = input("請輸入課程主題（按 Enter 略過）：").strip()

    # ── 課堂編號（全課程連續編號，掃描所有日期資料夾）──
    warn_if_date_out_of_order(TRANSCRIPTS_DIR, date_str)
    transcript_date_dir = TRANSCRIPTS_DIR / date_str
    transcript_date_dir.mkdir(parents=True, exist_ok=True)
    lesson_num = find_next_lesson_number(TRANSCRIPTS_DIR)
    print(f"📖 課堂編號：Lesson {lesson_num:02d}")

    # ── 檔名 slug（優先用 --slug，否則自動從 topic 衍生）──
    file_slug = sanitize_filename(args.slug) if args.slug else sanitize_filename(topic)

    # ── 複製錄音 ──
    if not args.no_copy:
        copy_recording(audio_path, date_str, lesson_num, file_slug)

    # ── 轉譯 ──
    transcript_text = transcribe_audio(audio_path, args.model, args.language)

    # ── 寫入 Markdown ──
    slug_part = f"-{file_slug}" if file_slug else ""
    transcript_path = transcript_date_dir / f"lesson-{lesson_num:02d}{slug_part}.md"
    md_content = build_transcript_md(
        transcript_text, date_str, lesson_num, topic, audio_path.name
    )
    transcript_path.write_text(md_content, encoding="utf-8")
    print(f"  ✓ 逐字稿已儲存 {transcript_path.relative_to(PROJECT_DIR)}")

    # ── 課後筆記 + 作業範本 ──
    notes_path = create_notes_template(date_str, lesson_num, topic, file_slug)
    hw_path = create_homework_template(date_str, lesson_num, topic, file_slug)

    print(f"\n✅ 完成！請開啟以下檔案：")
    print(f"   逐字稿：{transcript_path}")
    print(f"   筆記　：{notes_path}")
    print(f"   作業　：{hw_path}")


if __name__ == "__main__":
    main()
