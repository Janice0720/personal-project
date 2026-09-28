"""Insert a formatted cover page at the very start of the exported docx
(before pandoc's TOC block), matching 國立臺北商業大學資訊與決策科學研究所 format spec.

Run this AFTER the pandoc conversion step (see README.md), since it edits the
already-generated docx in place.
"""
import os
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.enum.text import WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUTPUT_FILENAME = "黃子甄_論文計畫書(第一至三章初稿).docx"
DOCX_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", OUTPUT_FILENAME))

# ---- 封面資訊：如有異動請直接修改以下欄位後重新執行本腳本 ----
SCHOOL = "國立臺北商業大學"
INSTITUTE = "資訊與決策科學研究所"
DEGREE_LABEL = "碩士學位論文"
TITLE_ZH = "應用投資人分群與個人化推薦模型於數位券商基金投資服務之研究"
TITLE_EN = "A Study on Applying Investor Segmentation and Personalized Recommendation Models to Digital Brokerage Fund Investment Services"
STUDENT = "研究生：黃子甄　撰"
ADVISOR = "指導教授：王亦凡　博士"
GRAD_DATE = "中華民國一一六年六月"  # 115 學年度第二學期（116 年 6 月）預計畢業


def set_run_font(run, size, bold, east_asia='標楷體', ascii_font='Times New Roman'):
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.name = ascii_font
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = OxmlElement('w:rFonts')
        rPr.append(rFonts)
    rFonts.set(qn('w:eastAsia'), east_asia)
    rFonts.set(qn('w:ascii'), ascii_font)
    rFonts.set(qn('w:hAnsi'), ascii_font)


def make_para(doc, text, size, bold, east_asia='標楷體', ascii_font='Times New Roman',
              space_before=0, space_after=0, line_spacing_pt=None, page_break=False):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf = p.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    if line_spacing_pt:
        pf.line_spacing = Pt(line_spacing_pt)
    run = p.add_run(text if text else "")
    set_run_font(run, size, bold, east_asia, ascii_font)
    if page_break:
        run.add_break(WD_BREAK.PAGE)
    return p


# ---- 表格欄寬修正：pandoc 表格預設等寬三分（tblLayout=fixed 但欄寬相同），
# 遇到「說明」等長文字欄位時會被壓縮到過窄，導致逐字換行、列高暴增（3.3.2 GA4
# 66 欄位表尤其明顯）。依各表實際欄位性質，將較長之說明類欄位加寬、短標籤欄位
# 收窄。可用寬度 = 頁寬 21cm − 左 3.5cm − 右 2.5cm = 15cm（A4，見上方頁面設定）。
USABLE_WIDTH_TWIPS = Cm(15).twips
TABLE_COL_RATIOS = {
    0: [0.15, 0.28, 0.30, 0.27],  # 表2-1 缺口/說明/最貼近之既有研究/與本研究之具體差異
    1: [0.15, 0.25, 0.60],        # 表3-1 分類/欄位/說明
    2: [0.15, 0.20, 0.12, 0.53],  # 表3-2 分類/欄位/尺度類型/說明
    3: [0.15, 0.25, 0.60],        # 表3-3 尺度類型/特徵範例/說明
    4: [0.15, 0.42, 0.43],        # 表3-4 模型/產出邏輯/所需資料
    5: [0.25, 0.75],              # 表3-5 欄位/說明
}


def fix_table_widths(doc):
    for idx, table in enumerate(doc.tables):
        ratios = TABLE_COL_RATIOS.get(idx)
        if not ratios:
            continue
        widths_twips = [int(USABLE_WIDTH_TWIPS * r) for r in ratios]

        tbl = table._tbl
        tblPr = tbl.tblPr
        tblLayout = tblPr.find(qn('w:tblLayout'))
        if tblLayout is None:
            tblLayout = OxmlElement('w:tblLayout')
            tblPr.append(tblLayout)
        tblLayout.set(qn('w:type'), 'fixed')

        tblGrid = tbl.find(qn('w:tblGrid'))
        cols = tblGrid.findall(qn('w:gridCol'))
        for col, w in zip(cols, widths_twips):
            col.set(qn('w:w'), str(w))

        for row in table.rows:
            for cell, w in zip(row.cells, widths_twips):
                cell.width = Cm(w / 566.9291339)  # twips -> cm


# ---- 表目錄：格式規範要求「目錄」之後、正文之前須有「表目錄」（見申請作業文件）。
# 逐一為 TableCaption 段落加上書籤，並於目錄後建立表目錄頁，以 PAGEREF 欄位
# 產生頁碼（與既有頁尾頁碼欄位同樣，開啟後 Ctrl+A 再 F9 更新）。----
def add_table_of_tables(doc):
    body = doc.element.body

    captions = [p for p in doc.paragraphs if p.style.name == 'TableCaption']
    if not captions:
        return

    bookmark_names = []
    for i, p in enumerate(captions):
        name = f'TableCap{i + 1}'
        bookmark_names.append(name)
        el = p._p
        bmk_start = OxmlElement('w:bookmarkStart')
        bmk_start.set(qn('w:id'), str(i + 1))
        bmk_start.set(qn('w:name'), name)
        bmk_end = OxmlElement('w:bookmarkEnd')
        bmk_end.set(qn('w:id'), str(i + 1))
        el.insert(0, bmk_start)
        el.append(bmk_end)

    chapter1_para = None
    for p in doc.paragraphs:
        if p.style.name == 'Heading 1' and p.text == '第一章　緒論':
            chapter1_para = p
            break
    if chapter1_para is None:
        return
    insert_ref = chapter1_para._p

    lot_paras = []

    brk_p = doc.add_paragraph()
    brk_p.add_run().add_break(WD_BREAK.PAGE)
    lot_paras.append(brk_p)

    title_p = doc.add_paragraph()
    title_p.style = doc.styles['Heading 1']
    title_run = title_p.add_run('表目錄')
    set_run_font(title_run, 18, True)
    lot_paras.append(title_p)

    for name, cap in zip(bookmark_names, captions):
        entry_p = doc.add_paragraph()
        entry_p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        pf = entry_p.paragraph_format
        pf.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
        pf.tab_stops.add_tab_stop(Cm(15), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)

        run1 = entry_p.add_run(cap.text)
        set_run_font(run1, 12, False)
        entry_p.add_run('\t')

        run_fld = entry_p.add_run()
        set_run_font(run_fld, 12, False)
        fldChar1 = OxmlElement('w:fldChar')
        fldChar1.set(qn('w:fldCharType'), 'begin')
        instrText = OxmlElement('w:instrText')
        instrText.set(qn('xml:space'), 'preserve')
        instrText.text = f'PAGEREF {name} \\h'
        fldChar2 = OxmlElement('w:fldChar')
        fldChar2.set(qn('w:fldCharType'), 'end')
        run_fld._r.append(fldChar1)
        run_fld._r.append(instrText)
        run_fld._r.append(fldChar2)

        lot_paras.append(entry_p)

    for p in lot_paras:
        el = p._p
        body.remove(el)
        insert_ref.addprevious(el)


def main():
    doc = Document(DOCX_PATH)
    body = doc.element.body
    first_child = body[0]  # pandoc puts the TOC content-control (or first para) here

    cover_paras = []
    cover_paras.append(make_para(doc, SCHOOL, 24, True, space_before=40))
    cover_paras.append(make_para(doc, INSTITUTE, 24, True))
    cover_paras.append(make_para(doc, DEGREE_LABEL, 24, True))
    for _ in range(5):
        cover_paras.append(make_para(doc, "", 18, False))
    cover_paras.append(make_para(doc, TITLE_ZH, 24, True, line_spacing_pt=32))
    cover_paras.append(make_para(doc, "", 12, False))
    cover_paras.append(make_para(doc, TITLE_EN, 20, False, line_spacing_pt=26))
    for _ in range(5):
        cover_paras.append(make_para(doc, "", 18, False))
    cover_paras.append(make_para(doc, STUDENT, 18, True))
    for _ in range(4):
        cover_paras.append(make_para(doc, "", 18, False))
    cover_paras.append(make_para(doc, ADVISOR, 18, True))
    for _ in range(4):
        cover_paras.append(make_para(doc, "", 18, False))
    cover_paras.append(make_para(doc, GRAD_DATE, 18, True))
    page_break_para = doc.add_paragraph()
    page_break_para.add_run().add_break(WD_BREAK.PAGE)
    cover_paras.append(page_break_para)

    # Each paragraph above was appended at the very end of the body; move them,
    # in the same order, to sit immediately before the original first element
    # (pandoc's TOC block), so the final order is: cover -> TOC -> chapter 1.
    insert_ref = first_child
    for p in cover_paras:
        el = p._p
        body.remove(el)
        insert_ref.addprevious(el)

    fix_table_widths(doc)
    add_table_of_tables(doc)

    # Heading 1's style-level pageBreakBefore is not reliably rendered as a
    # visible page break by all viewers; insert explicit page breaks before
    # every chapter-level heading to guarantee each chapter starts on a new page.
    CHAPTER_TITLES = {"第一章　緒論", "第二章　文獻探討", "第三章　研究方法", "參考文獻"}
    for p in doc.paragraphs:
        if p.style.name == "Heading 1" and p.text in CHAPTER_TITLES:
            brk_p = OxmlElement('w:p')
            brk_r = OxmlElement('w:r')
            brk = OxmlElement('w:br')
            brk.set(qn('w:type'), 'page')
            brk_r.append(brk)
            brk_p.append(brk_r)
            p._p.addprevious(brk_p)

    doc.save(DOCX_PATH)
    print("cover page inserted before TOC ->", DOCX_PATH)


if __name__ == "__main__":
    main()
