"""
將 專案摘要_FinCheck個人財務健檢AI系統.md 轉換為 PDF
使用 reportlab UnicodeCIDFont（STSong-Light），原生支援繁體中文
"""
import re
import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, Preformatted, KeepTogether
)
from reportlab.platypus.flowables import Flowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

# ── 路徑 ──────────────────────────────────────────────────────────────────
BASE  = os.path.dirname(os.path.abspath(__file__))
MD_IN = os.path.join(BASE, "專案摘要_FinCheck個人財務健檢AI系統.md")
PDF_OUT = os.path.join(BASE, "專案摘要_FinCheck個人財務健檢AI系統.pdf")

# ── 字型註冊 ──────────────────────────────────────────────────────────────
pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
FONT = "STSong-Light"

# ── 顏色 ──────────────────────────────────────────────────────────────────
C_H1       = colors.HexColor("#0f2d5c")
C_H2       = colors.HexColor("#1a4a8a")
C_H3       = colors.HexColor("#2a5fa5")
C_BODY     = colors.HexColor("#1a1a1a")
C_CODE_BG  = colors.HexColor("#f4f4f4")
C_QUOTE_BG = colors.HexColor("#eef4ff")
C_BORDER   = colors.HexColor("#ccd6e8")
C_TBL_HDR  = colors.HexColor("#1a4a8a")
C_TBL_ALT  = colors.HexColor("#f2f6fc")
C_WHITE    = colors.white
C_RULE     = colors.HexColor("#ccd6e8")

# ── Paragraph Styles ──────────────────────────────────────────────────────
def S(name, **kw):
    base = kw.pop("parent", None)
    defaults = dict(fontName=FONT, fontSize=10, leading=18,
                    textColor=C_BODY, spaceAfter=4)
    if base:
        defaults.update({k: getattr(base, k) for k in vars(base) if not k.startswith("_")})
    defaults.update(kw)
    return ParagraphStyle(name, **defaults)

ST_H1     = S("h1", fontSize=20, leading=28, textColor=C_H1, spaceAfter=6, spaceBefore=2)
ST_H2     = S("h2", fontSize=14, leading=20, textColor=C_H2, spaceAfter=4, spaceBefore=14,
               leftIndent=8, borderPadding=(0, 0, 0, 8))
ST_H3     = S("h3", fontSize=11, leading=17, textColor=C_H3, spaceAfter=3, spaceBefore=8)
ST_BODY   = S("body", fontSize=10, leading=18, spaceAfter=6)
ST_BULLET = S("bullet", fontSize=10, leading=17, leftIndent=14, firstLineIndent=-8,
               bulletIndent=5, spaceAfter=3)
ST_CODE   = S("code", fontName="Courier", fontSize=8, leading=13,
               textColor=colors.HexColor("#333333"), spaceAfter=8,
               backColor=C_CODE_BG, leftIndent=10, rightIndent=4)
ST_QUOTE  = S("quote", fontSize=9.5, leading=16, textColor=colors.HexColor("#3a3a5a"),
               leftIndent=14, rightIndent=6, spaceAfter=8,
               backColor=C_QUOTE_BG, borderPadding=6)
ST_FOOTER = S("footer", fontSize=8, leading=12, textColor=colors.HexColor("#888888"),
               alignment=TA_CENTER)

# ── 工具函式 ──────────────────────────────────────────────────────────────
def clean(text: str) -> str:
    """移除行內 Markdown，保留可印文字"""
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*(.+?)\*",   r"<i>\1</i>", text)
    text = re.sub(r"`(.+?)`",     r"\1", text)
    text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text)
    # 移除目錄錨點連結 [文字](#anchor)
    text = re.sub(r"\[(.+?)\]\(#.+?\)", r"\1", text)
    return text

def plain(text: str) -> str:
    """完全純文字（給表格用）"""
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*",   r"\1", text)
    text = re.sub(r"`(.+?)`",     r"\1", text)
    text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text)
    text = re.sub(r"\[(.+?)\]\(#.+?\)", r"\1", text)
    return text


# ── Markdown 解析 ─────────────────────────────────────────────────────────
def parse_md(content: str):
    tokens = []
    lines = content.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]

        # 分隔線
        if re.match(r"^-{3,}$", line.strip()):
            tokens.append({"type": "hr"})
            i += 1
            continue

        # 程式碼區塊
        if line.startswith("```"):
            block = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                block.append(lines[i])
                i += 1
            tokens.append({"type": "code", "lines": block})
            i += 1
            continue

        # 引用
        if line.startswith("> "):
            parts = []
            while i < len(lines) and lines[i].startswith("> "):
                parts.append(lines[i][2:])
                i += 1
            tokens.append({"type": "blockquote", "text": " ".join(parts)})
            continue

        # 表格
        if "|" in line and i + 1 < len(lines) and re.match(r"^\|[\-| :]+\|$", lines[i+1].strip()):
            rows = []
            while i < len(lines) and "|" in lines[i]:
                cells = [c.strip() for c in lines[i].split("|")]
                cells = [c for c in cells if c != ""]
                rows.append(cells)
                i += 1
            header = rows[0] if rows else []
            data   = [r for r in rows[2:] if r] if len(rows) > 2 else []
            tokens.append({"type": "table", "header": header, "rows": data})
            continue

        # 標題
        m = re.match(r"^(#{1,3})\s+(.*)", line)
        if m:
            lvl = len(m.group(1))
            tokens.append({"type": f"h{lvl}", "text": m.group(2)})
            i += 1
            continue

        # 無序清單
        if re.match(r"^[-*]\s+", line):
            items = []
            while i < len(lines) and re.match(r"^[-*]\s+", lines[i]):
                items.append(re.sub(r"^[-*]\s+", "", lines[i]))
                i += 1
            tokens.append({"type": "ul", "items": items})
            continue

        # 有序清單
        if re.match(r"^\d+\.\s+", line):
            items = []
            while i < len(lines) and re.match(r"^\d+\.\s+", lines[i]):
                items.append(re.sub(r"^\d+\.\s+", "", lines[i]))
                i += 1
            tokens.append({"type": "ol", "items": items})
            continue

        # 空行
        if line.strip() == "":
            tokens.append({"type": "blank"})
            i += 1
            continue

        # 一般段落（合併連續行）
        para = []
        while i < len(lines):
            l = lines[i]
            if (l.strip() == "" or l.startswith("#") or l.startswith(">")
                    or l.startswith("```") or "|" in l
                    or re.match(r"^[-*]\s+", l) or re.match(r"^\d+\.\s+", l)
                    or re.match(r"^-{3,}$", l.strip())):
                break
            para.append(l)
            i += 1
        if para:
            tokens.append({"type": "p", "text": " ".join(para)})
    return tokens


# ── flowable 產生 ─────────────────────────────────────────────────────────
def build_story(tokens):
    story = []

    for tok in tokens:
        t = tok["type"]

        if t == "blank":
            story.append(Spacer(1, 3*mm))

        elif t == "hr":
            story.append(Spacer(1, 2*mm))
            story.append(HRFlowable(width="100%", thickness=0.5,
                                     color=C_RULE, spaceAfter=4))

        elif t == "h1":
            story.append(Paragraph(clean(tok["text"]), ST_H1))
            story.append(HRFlowable(width="100%", thickness=2,
                                     color=C_H1, spaceAfter=6))

        elif t == "h2":
            story.append(Spacer(1, 3*mm))
            story.append(Paragraph(clean(tok["text"]), ST_H2))
            story.append(HRFlowable(width="100%", thickness=0.5,
                                     color=C_BORDER, spaceAfter=2))

        elif t == "h3":
            story.append(Paragraph(clean(tok["text"]), ST_H3))

        elif t == "p":
            story.append(Paragraph(clean(tok["text"]), ST_BODY))

        elif t == "ul":
            for item in tok["items"]:
                story.append(Paragraph("• " + clean(item), ST_BULLET))

        elif t == "ol":
            for idx, item in enumerate(tok["items"], 1):
                story.append(Paragraph(f"{idx}. " + clean(item), ST_BULLET))

        elif t == "code":
            code_text = "\n".join(tok["lines"])
            story.append(Preformatted(code_text, ST_CODE))

        elif t == "blockquote":
            story.append(Paragraph(clean(tok["text"]), ST_QUOTE))

        elif t == "table":
            header = tok["header"]
            rows   = tok["rows"]
            if not header:
                continue

            col_count = len(header)
            page_w    = A4[0] - 40*mm   # 頁寬扣邊距
            col_w     = page_w / col_count

            tdata = [[plain(h) for h in header]]
            for row in rows:
                padded = [plain(row[c]) if c < len(row) else "" for c in range(col_count)]
                tdata.append(padded)

            tbl = Table(tdata, colWidths=[col_w]*col_count, repeatRows=1)

            ts = TableStyle([
                ("FONTNAME",        (0,0), (-1,-1), FONT),
                ("FONTSIZE",        (0,0), (-1,-1), 9),
                ("LEADING",         (0,0), (-1,-1), 14),
                ("BACKGROUND",      (0,0), (-1,0), C_TBL_HDR),
                ("TEXTCOLOR",       (0,0), (-1,0), C_WHITE),
                ("FONTSIZE",        (0,0), (-1,0), 9),
                ("ALIGN",           (0,0), (-1,0), "CENTER"),
                ("VALIGN",          (0,0), (-1,-1), "MIDDLE"),
                ("GRID",            (0,0), (-1,-1), 0.4, C_BORDER),
                ("ROWBACKGROUNDS",  (0,1), (-1,-1), [C_WHITE, C_TBL_ALT]),
                ("TOPPADDING",      (0,0), (-1,-1), 4),
                ("BOTTOMPADDING",   (0,0), (-1,-1), 4),
                ("LEFTPADDING",     (0,0), (-1,-1), 6),
                ("RIGHTPADDING",    (0,0), (-1,-1), 6),
            ])
            tbl.setStyle(ts)
            story.append(KeepTogether(tbl))
            story.append(Spacer(1, 4*mm))

    return story


# ── 頁首 / 頁尾 callback ──────────────────────────────────────────────────
def on_first_page(canvas, doc):
    _draw_footer(canvas, doc)

def on_later_pages(canvas, doc):
    _draw_footer(canvas, doc)

def _draw_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont(FONT, 8)
    canvas.setFillColor(colors.HexColor("#888888"))
    canvas.drawCentredString(
        A4[0] / 2,
        12 * mm,
        f"FinCheck 個人財務健檢 AI 系統  ·  第 {doc.page} 頁"
    )
    canvas.restoreState()


# ── 主程式 ────────────────────────────────────────────────────────────────
def main():
    print("讀取 Markdown...")
    with open(MD_IN, "r", encoding="utf-8") as f:
        content = f.read()

    print("解析 Markdown...")
    tokens = parse_md(content)

    print("建立 PDF...")
    doc = SimpleDocTemplate(
        PDF_OUT,
        pagesize=A4,
        leftMargin=20*mm, rightMargin=20*mm,
        topMargin=20*mm, bottomMargin=22*mm,
        title="FinCheck 個人財務健檢 AI 系統",
        author="FinCheck 專案組",
    )

    story = build_story(tokens)
    doc.build(story, onFirstPage=on_first_page, onLaterPages=on_later_pages)
    print(f"完成！輸出：{PDF_OUT}")


if __name__ == "__main__":
    main()
