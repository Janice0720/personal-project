#!/usr/bin/env python3
"""
generate_notes.py
用途：讀取 Whisper 逐字稿，呼叫 AI API 自動產出課後學習筆記
支援 provider：openai（預設）、anthropic

使用：
    python3 scripts/generate_notes.py transcripts/YYYY-MM-DD/lesson-NN-slug.md
    python3 scripts/generate_notes.py --latest              # 自動抓最新一堂課
    python3 scripts/generate_notes.py ... --force           # 強制重新產出
    python3 scripts/generate_notes.py ... --provider anthropic --model claude-opus-4-5
"""

import argparse
import os
import re
import sys
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
TRANSCRIPTS_DIR = PROJECT_DIR / "transcripts"
NOTES_DIR = PROJECT_DIR / "notes"

DEFAULT_PROVIDER = "template"   # 預設不需 API Key
DEFAULT_MODEL_OPENAI = "gpt-4o"
DEFAULT_MODEL_ANTHROPIC = "claude-3-5-haiku-20241022"

NOTES_PROMPT = """\
你是英文口說課的學習助理。以下是一堂英文口說課的逐字稿，請分析並輸出繁體中文 Markdown 課後筆記。

輸出格式要求（嚴格遵守，只輸出 Markdown 內容，不要加任何說明文字）：

## 今日學習目標

- （從課堂內容推斷，2-3條）

---

## 課堂重點摘要

1. （列出3-5條重要觀念或技巧）

---

## 重點單字／片語

| 單字／片語 | 詞性 | 中文意思 | 課堂例句 |
|-----------|------|---------|---------|
（從老師明確教授、示範或糾正的詞彙中提取，至少10個。例句盡量使用逐字稿中的原句）

---

## 老師的關鍵糾正

| 你說的 | 老師建議改成 | 重點說明 |
|--------|------------|--------|
（只列老師明確指出的錯誤與建議；若無則寫一行：| （本堂課無明確糾正記錄） | — | — |）

---

## 老師出的作業

（老師明確指派的作業：先引用原文，再附中文說明。若無則寫「（無）」）

---

## 文法重點

- （老師強調的文法或表達方式，條列式，2-5條）

---

逐字稿：

{transcript}
"""


def find_latest_transcript() -> Path:
    """找最新一堂課的逐字稿（依資料夾日期 + 檔案編號排序）"""
    all_transcripts = sorted(TRANSCRIPTS_DIR.glob("*/lesson-*.md"))
    if not all_transcripts:
        print("[錯誤] transcripts/ 資料夾內找不到任何逐字稿")
        sys.exit(1)
    return all_transcripts[-1]


def infer_notes_path(transcript_path: Path) -> Path:
    """從逐字稿路徑推導對應的 notes 檔路徑"""
    # transcripts/YYYY-MM-DD/lesson-NN-slug.md -> notes/YYYY-MM-DD/lesson-NN-slug-notes.md
    date_str = transcript_path.parent.name
    return NOTES_DIR / date_str / f"{transcript_path.stem}-notes.md"


def parse_lesson_info(transcript_path: Path) -> tuple[int, str, str]:
    """從逐字稿解析 lesson_num、topic、date_str"""
    date_str = transcript_path.parent.name
    content = transcript_path.read_text(encoding="utf-8")
    title_match = re.search(r"^# Lesson \d+：(.+)$", content, re.MULTILINE)
    topic = title_match.group(1).strip() if title_match else "（未命名課程）"
    num_match = re.search(r"lesson-(\d+)", transcript_path.stem)
    lesson_num = int(num_match.group(1)) if num_match else 0
    return lesson_num, topic, date_str


def notes_has_content(notes_path: Path) -> bool:
    """判斷筆記檔是否已有實際 AI 產出的內容（而非空白範本）"""
    if not notes_path.exists():
        return False
    content = notes_path.read_text(encoding="utf-8")
    # 空白範本不含粗體單字（**word**）或超過 20 個字的表格列
    return bool(re.search(r"\|\s*\*\*", content)) or content.count("\n|") > 5


def build_template(transcript_text: str) -> str:
    """不呼叫 API，產出帶逐字稿的結構化空白筆記範本"""
    return f"""\
## 今日學習目標

- 
- 

---

## 課堂重點摘要

1. 
2. 
3. 

---

## 重點單字／片語

| 單字／片語 | 詞性 | 中文意思 | 課堂例句 |
|-----------|------|---------|---------|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

---

## 老師的關鍵糾正

| 你說的 | 老師建議改成 | 重點說明 |
|--------|------------|--------|
|  |  |  |

---

## 老師出的作業

（填入老師指派的作業，若無則寫「無」）

---

## 文法重點

- 

---

## 📋 逐字稿（填筆記時對照用）

{transcript_text.strip()}
"""


def call_openai(transcript_text: str, model: str) -> str:
    try:
        from openai import OpenAI
    except ImportError:
        print("\n[錯誤] 尚未安裝 openai，請先執行：")
        print("  pip install --user openai")
        sys.exit(1)

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("\n[錯誤] 找不到 OPENAI_API_KEY 環境變數")
        print("請執行：export OPENAI_API_KEY='sk-...'")
        print("或永久生效：echo 'export OPENAI_API_KEY=sk-...' >> ~/.zshrc && source ~/.zshrc")
        sys.exit(1)

    client = OpenAI(api_key=api_key)
    prompt = NOTES_PROMPT.format(transcript=transcript_text)

    print(f"  ⏳ 呼叫 {model} 分析逐字稿（約 30-60 秒）…")
    response = client.chat.completions.create(
        model=model,
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


def call_anthropic(transcript_text: str, model: str) -> str:
    try:
        import anthropic
    except ImportError:
        print("\n[錯誤] 尚未安裝 anthropic，請先執行：")
        print("  pip install --user anthropic")
        sys.exit(1)

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("\n[錯誤] 找不到 ANTHROPIC_API_KEY 環境變數")
        print("請執行：export ANTHROPIC_API_KEY='sk-ant-...'")
        print("或永久生效：echo 'export ANTHROPIC_API_KEY=sk-ant-...' >> ~/.zshrc && source ~/.zshrc")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    prompt = NOTES_PROMPT.format(transcript=transcript_text)

    print(f"  ⏳ 呼叫 {model} 分析逐字稿（約 30-60 秒）…")
    message = client.messages.create(
        model=model,
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def build_notes_md(ai_content: str, date_str: str, lesson_num: int, topic: str) -> str:
    return (
        f"# 課後筆記 — Lesson {lesson_num:02d}：{topic}\n\n"
        f"**日期**：{date_str}\n"
        f"**主題**：{topic}\n\n"
        f"---\n\n"
        f"{ai_content.strip()}\n"
    )


def main():
    parser = argparse.ArgumentParser(description="呼叫 Claude 從逐字稿自動產出課後筆記")
    parser.add_argument(
        "transcript",
        nargs="?",
        help="逐字稿檔路徑（transcripts/YYYY-MM-DD/lesson-NN-slug.md）",
    )
    parser.add_argument(
        "--latest",
        action="store_true",
        help="自動選取最新一堂課的逐字稿",
    )
    parser.add_argument(
        "--provider",
        "-p",
        default=DEFAULT_PROVIDER,
        choices=["template", "openai", "anthropic"],
        help="產出方式：template（預設，不需 API Key）、openai、anthropic",
    )
    parser.add_argument(
        "--model",
        "-m",
        default="",
        help="模型名稱（預設 openai=gpt-4o、anthropic=claude-3-5-haiku-20241022）",
    )
    parser.add_argument(
        "--force",
        "-f",
        action="store_true",
        help="即使筆記已有內容也強制重新產出",
    )
    args = parser.parse_args()

    if not args.model:
        args.model = DEFAULT_MODEL_OPENAI if args.provider == "openai" else DEFAULT_MODEL_ANTHROPIC

    if args.latest:
        transcript_path = find_latest_transcript()
    elif args.transcript:
        transcript_path = Path(args.transcript).expanduser().resolve()
    else:
        parser.error("請提供逐字稿路徑，或使用 --latest 自動抓最新一堂課")

    if not transcript_path.exists():
        print(f"[錯誤] 找不到逐字稿：{transcript_path}")
        sys.exit(1)

    notes_path = infer_notes_path(transcript_path)

    if notes_has_content(notes_path) and not args.force:
        print(f"⚠️  筆記已有內容：{notes_path.relative_to(PROJECT_DIR)}")
        print("   若要重新產出，請加上 --force")
        sys.exit(0)

    lesson_num, topic, date_str = parse_lesson_info(transcript_path)
    transcript_text = transcript_path.read_text(encoding="utf-8")

    print(f"\n📖 逐字稿：{transcript_path.relative_to(PROJECT_DIR)}")
    print(f"   課堂：Lesson {lesson_num:02d}　主題：{topic}")

    if args.provider == "template":
        ai_content = build_template(transcript_text)
        print("  ✓ 以範本模式產出（逐字稿嵌入筆記底部）")
    elif args.provider == "openai":
        ai_content = call_openai(transcript_text, args.model)
    else:
        ai_content = call_anthropic(transcript_text, args.model)
    notes_content = build_notes_md(ai_content, date_str, lesson_num, topic)

    notes_path.parent.mkdir(parents=True, exist_ok=True)
    notes_path.write_text(notes_content, encoding="utf-8")

    print(f"  ✓ 課後筆記已寫入：{notes_path.relative_to(PROJECT_DIR)}")
    print(f"\n✅ 完成！下一步：")
    print(f"   python3 scripts/extract_vocab.py {notes_path.relative_to(PROJECT_DIR)}")


if __name__ == "__main__":
    main()
