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

# ---- Page setup: top 2.5cm, bottom 2.5cm, left 3.5cm, right 2.5cm ----
section = doc.sections[0]
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
