"""Build a reference.docx template matching 國立臺北商業大學資訊與決策科學研究所 format spec."""
import docx
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


def set_east_asian_font(run, font_name):
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = OxmlElement('w:rFonts')
        rPr.append(rFonts)
    rFonts.set(qn('w:eastAsia'), font_name)
    rFonts.set(qn('w:ascii'), 'Times New Roman')
    rFonts.set(qn('w:hAnsi'), 'Times New Roman')


def style_font(style, size, bold, east_asia='標楷體', ascii_font='Times New Roman', color=None):
    f = style.font
    f.size = Pt(size)
    f.bold = bold
    f.name = ascii_font
    if color:
        f.color.rgb = RGBColor(*color)
    rPr = style.element.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = OxmlElement('w:rFonts')
        rPr.append(rFonts)
    rFonts.set(qn('w:eastAsia'), east_asia)
    rFonts.set(qn('w:ascii'), ascii_font)
    rFonts.set(qn('w:hAnsi'), ascii_font)


def set_line_spacing_1_5(pf):
    pf.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE


doc = Document()

# ---- Page setup: A4（python-docx 預設為 US Letter，未明確設定會誤用），
# 上下 2.5cm、左 3.5cm、右 2.5cm ----
section = doc.sections[0]
section.page_width = Cm(21)
section.page_height = Cm(29.7)
section.top_margin = Cm(2.5)
section.bottom_margin = Cm(2.5)
section.left_margin = Cm(3.5)
section.right_margin = Cm(2.5)

# ---- Normal (body text): 12pt 標楷體, 1.5 line spacing, black ----
normal = doc.styles['Normal']
style_font(normal, 12, False, east_asia='標楷體', ascii_font='Times New Roman', color=(0, 0, 0))
pf = normal.paragraph_format
set_line_spacing_1_5(pf)
pf.space_after = Pt(0)
pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

# ---- Heading 1: 章標題, 18pt bold 標楷體, centered ----
h1 = doc.styles['Heading 1']
style_font(h1, 18, True, east_asia='標楷體', ascii_font='Times New Roman', color=(0, 0, 0))
h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
h1.paragraph_format.space_before = Pt(24)
h1.paragraph_format.space_after = Pt(24)
h1.paragraph_format.page_break_before = True
h1.paragraph_format.keep_with_next = True

# ---- Heading 2: 節標題 X.Y, 18pt bold 標楷體, left-aligned ----
h2 = doc.styles['Heading 2']
style_font(h2, 18, True, east_asia='標楷體', ascii_font='Times New Roman', color=(0, 0, 0))
h2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
h2.paragraph_format.space_before = Pt(18)
h2.paragraph_format.space_after = Pt(6)
h2.paragraph_format.keep_with_next = True

# ---- Heading 3: 小節 X.Y.Z, 16pt bold 標楷體, left-aligned ----
h3 = doc.styles['Heading 3']
style_font(h3, 16, True, east_asia='標楷體', ascii_font='Times New Roman', color=(0, 0, 0))
h3.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
h3.paragraph_format.space_before = Pt(12)
h3.paragraph_format.space_after = Pt(6)
h3.paragraph_format.keep_with_next = True

# ---- Heading 4: 細節 X.Y.Z.W, 14pt bold 標楷體, left-aligned ----
h4 = doc.styles['Heading 4']
style_font(h4, 14, True, east_asia='標楷體', ascii_font='Times New Roman', color=(0, 0, 0))
h4.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
h4.paragraph_format.space_before = Pt(10)
h4.paragraph_format.space_after = Pt(4)
h4.paragraph_format.keep_with_next = True

# ---- Heading 5: 未編號之深層小標題, 12pt bold 標楷體, left-aligned ----
h5 = doc.styles['Heading 5']
style_font(h5, 12, True, east_asia='標楷體', ascii_font='Times New Roman', color=(0, 0, 0))
h5.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
h5.paragraph_format.space_before = Pt(8)
h5.paragraph_format.space_after = Pt(4)
h5.paragraph_format.keep_with_next = True

# ---- Body Text: pandoc styles every non-first paragraph in a section as "Body Text"
# (only the first paragraph after a heading gets "Normal"); without this override it
# silently falls back to Word's built-in Body Text style (adds 6pt space-after),
# producing inconsistent paragraph spacing across the body text. Match Normal exactly.
body_text = doc.styles['Body Text']
style_font(body_text, 12, False, east_asia='標楷體', ascii_font='Times New Roman', color=(0, 0, 0))
bt_pf = body_text.paragraph_format
set_line_spacing_1_5(bt_pf)
bt_pf.space_after = Pt(0)
bt_pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

# ---- Source Code / Verbatim Char: used for ASCII box-drawing architecture diagrams
# and pseudocode blocks. Without an explicit monospace font, pandoc synthesizes an
# empty style that falls back to 標楷體/Times New Roman (proportional), which breaks
# the box-drawing character alignment. ----
try:
    src_style = doc.styles.add_style('Source Code', WD_STYLE_TYPE.PARAGRAPH)
except ValueError:
    src_style = doc.styles['Source Code']
src_style.base_style = normal
style_font(src_style, 11, False, east_asia='細明體', ascii_font='Courier New', color=(0, 0, 0))
src_style.paragraph_format.space_after = Pt(0)
src_style.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE

try:
    verbatim_char = doc.styles.add_style('Verbatim Char', WD_STYLE_TYPE.CHARACTER)
except ValueError:
    verbatim_char = doc.styles['Verbatim Char']
vc_rPr = verbatim_char.element.get_or_add_rPr()
vc_rFonts = vc_rPr.find(qn('w:rFonts'))
if vc_rFonts is None:
    vc_rFonts = OxmlElement('w:rFonts')
    vc_rPr.append(vc_rFonts)
vc_rFonts.set(qn('w:eastAsia'), '細明體')
vc_rFonts.set(qn('w:ascii'), 'Courier New')
vc_rFonts.set(qn('w:hAnsi'), 'Courier New')
verbatim_char.font.name = 'Courier New'
verbatim_char.font.size = Pt(11)

# ---- References: 參考文獻條目，第二行起內縮 2 個字元（垂懸縮排），依格式規範 ----
try:
    refs_style = doc.styles.add_style('References', WD_STYLE_TYPE.PARAGRAPH)
except ValueError:
    refs_style = doc.styles['References']
refs_style.base_style = normal
refs_pf = refs_style.paragraph_format
refs_pf.left_indent = Pt(24)
refs_pf.first_line_indent = Pt(-24)
refs_pf.space_after = Pt(6)

# ---- TableCaption: 表格標題（置於表格正上方，依慣例），12pt 粗體標楷體置中 ----
try:
    cap_style = doc.styles.add_style('TableCaption', WD_STYLE_TYPE.PARAGRAPH)
except ValueError:
    cap_style = doc.styles['TableCaption']
cap_style.base_style = normal
style_font(cap_style, 12, True, east_asia='標楷體', ascii_font='Times New Roman', color=(0, 0, 0))
cap_pf = cap_style.paragraph_format
cap_pf.alignment = WD_ALIGN_PARAGRAPH.CENTER
cap_pf.space_before = Pt(12)
cap_pf.space_after = Pt(6)
cap_pf.line_spacing_rule = WD_LINE_SPACING.SINGLE

# ---- Figure: 圖片本身所在段落，置中對齊（Normal 為左右對齊，單張圖片置中效果不穩定）----
try:
    fig_style = doc.styles.add_style('Figure', WD_STYLE_TYPE.PARAGRAPH)
except ValueError:
    fig_style = doc.styles['Figure']
fig_style.base_style = normal
fig_pf = fig_style.paragraph_format
fig_pf.alignment = WD_ALIGN_PARAGRAPH.CENTER
fig_pf.space_before = Pt(12)
fig_pf.space_after = Pt(6)

# ---- FigureCaption: 圖片標題（置於圖片正下方，依慣例），12pt 粗體標楷體置中 ----
try:
    figcap_style = doc.styles.add_style('FigureCaption', WD_STYLE_TYPE.PARAGRAPH)
except ValueError:
    figcap_style = doc.styles['FigureCaption']
figcap_style.base_style = normal
style_font(figcap_style, 12, True, east_asia='標楷體', ascii_font='Times New Roman', color=(0, 0, 0))
figcap_pf = figcap_style.paragraph_format
figcap_pf.alignment = WD_ALIGN_PARAGRAPH.CENTER
figcap_pf.space_before = Pt(6)
figcap_pf.space_after = Pt(12)
figcap_pf.line_spacing_rule = WD_LINE_SPACING.SINGLE

# ---- Table style: pandoc emits tables with style id "Table"; define it with visible grid borders ----
# (cell paragraphs already use "Normal" style for font, confirmed separately; this only needs borders)
table_grid = doc.styles['Table Grid']  # has visible borders by default
try:
    tbl_style = doc.styles.add_style('Table', WD_STYLE_TYPE.TABLE)
    tbl_style.base_style = table_grid
except ValueError:
    pass  # style already exists

# ---- Compact list styles (for bullet/numbered lists) ----
for sname in ['List Bullet', 'List Number']:
    try:
        s = doc.styles[sname]
        style_font(s, 12, False, east_asia='標楷體', ascii_font='Times New Roman', color=(0, 0, 0))
        s.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
        s.paragraph_format.space_after = Pt(0)
    except KeyError:
        pass

# ---- Footer: centered page number ----
footer = section.footer
footer_para = footer.paragraphs[0]
footer_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = footer_para.add_run()
fldChar1 = OxmlElement('w:fldChar')
fldChar1.set(qn('w:fldCharType'), 'begin')
instrText = OxmlElement('w:instrText')
instrText.set(qn('xml:space'), 'preserve')
instrText.text = 'PAGE'
fldChar2 = OxmlElement('w:fldChar')
fldChar2.set(qn('w:fldCharType'), 'end')
run._r.append(fldChar1)
run._r.append(instrText)
run._r.append(fldChar2)

import os
doc.save(os.path.join(os.path.dirname(__file__), 'reference.docx'))
print('reference.docx created')
