import os
import re

# thesis/exports/build/preprocess.py -> thesis/chapters
BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", "chapters"))

CH1 = [f"{BASE}/chapter-01-introduction/01-introduction-draft.md"]
CH2 = [
    f"{BASE}/chapter-02-literature-review/01-investor-behavior-segmentation-rfm.md",
    f"{BASE}/chapter-02-literature-review/02-recommendation-fintech-digital-brokerage.md",
    f"{BASE}/chapter-02-literature-review/03-gap-analysis.md",
]
CH3 = [
    f"{BASE}/chapter-03-methodology/02-research-framework.md",
    f"{BASE}/chapter-03-methodology/03-research-process.md",
    f"{BASE}/chapter-03-methodology/04-data-sources.md",
    f"{BASE}/chapter-03-methodology/05-data-preprocessing.md",
    f"{BASE}/chapter-03-methodology/06-investor-segmentation.md",
    f"{BASE}/chapter-03-methodology/07-recommendation-models.md",
    f"{BASE}/chapter-03-methodology/08-evaluation-methods.md",
]

TITLE_LINE_RE = re.compile(r"^論文題目：.*$", re.MULTILINE)
NUMBERED_HEADING_RE = re.compile(r"^(#{1,6})\s+(\d+(?:\.\d+)+)\s+(.*)$")
BARE_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def strip_title_line(text):
    text = TITLE_LINE_RE.sub("", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def renumber_headings_stateful(text):
    """Numbered headings (X.Y[.Z]) get level = dot_count+1.
    Bare headings (### N. Title, #### Title, etc.) shift by the same
    delta as the most recently seen numbered heading (source convention:
    all numbered headings were flat '##', i.e. level 2)."""
    lines = text.split("\n")
    out = []
    shift = 0
    for line in lines:
        m = NUMBERED_HEADING_RE.match(line)
        if m:
            number = m.group(2)
            title = m.group(3)
            dots = number.count(".")
            new_level = min(dots + 1, 6)
            shift = new_level - 2  # source numbered headings were always level 2
            out.append(f"{'#' * new_level} {number} {title}")
            continue
        m2 = BARE_HEADING_RE.match(line)
        if m2 and set(m2.group(1)) == {"#"}:
            old_level = len(m2.group(1))
            title = m2.group(2)
            new_level = min(max(old_level + shift, 1), 6)
            out.append(f"{'#' * new_level} {title}")
            continue
        out.append(line)
    return "\n".join(out)


def process_ch1():
    text = read(CH1[0])
    text = strip_title_line(text)
    text = re.sub(
        r"^# .*$",
        "# 第一章　緒論",
        text,
        count=1,
        flags=re.MULTILINE,
    )
    text = renumber_headings_stateful(text)
    return text


def process_ch2():
    parts = []
    for i, path in enumerate(CH2):
        text = read(path)
        text = strip_title_line(text)
        if i in (0, 1):
            # drop this file's own H1 (working-file title, not real numbered content)
            text = re.sub(r"^# .*\n+", "", text, count=1, flags=re.MULTILINE)
        # i == 2 (gap-analysis): its H1 IS a real section (2.5) -> handled by renumber pass
        parts.append(text.strip())
    combined = "\n\n---\n\n".join(parts)
    combined = renumber_headings_stateful(combined)
    return "# 第二章　文獻探討\n\n" + combined


def process_ch3():
    parts = []
    for path in CH3:
        text = read(path)
        text = strip_title_line(text)
        parts.append(text.strip())
    combined = "\n\n---\n\n".join(parts)
    combined = renumber_headings_stateful(combined)
    return "# 第三章　研究方法\n\n" + combined


YAML_HEADER = """---
title: ""
lang: zh-TW
toc-title: 目錄
---

"""


def main():
    out = [process_ch1(), process_ch2(), process_ch3()]
    combined = YAML_HEADER + "\n\n".join(out)
    outpath = os.path.join(os.path.dirname(__file__), "combined.md")
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(combined)
    print("wrote", outpath, len(combined), "chars")


if __name__ == "__main__":
    main()
