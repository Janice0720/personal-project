"""
生成 5 份模擬 MyData 個人所得資料 PDF
每份對應一種財務人物類型，格式與 pdf_parser.py 的正規式相容

執行：cd side-projects/personal-fincheck
      /opt/anaconda3/bin/python scripts/generate_sample_pdfs.py
產出：data/sample_pdfs/*.pdf
"""

import os
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4

# ── 字型設定 ─────────────────────────────────────────────────
FONT_PATH = '/Library/Fonts/Arial Unicode.ttf'
FONT_NAME = 'ArialUnicode'
pdfmetrics.registerFont(TTFont(FONT_NAME, FONT_PATH))

OUTPUT_DIR = 'data/sample_pdfs'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── 5 種財務人物設計 ──────────────────────────────────────────
# 每筆格式：(中文類別, 格式代號, IDN, 金額, 扣繳稅額, 扣繳單位)
PERSONAS = [
    {
        'filename': '01_薪資投資型_張小明.pdf',
        'name':     '張小明',
        'idn':      'A123456001',
        'year':     '112',
        'persona':  '薪資投資型',
        'note':     '薪資 ~39%｜股利 ~58%｜利息 ~3%',
        'records': [
            ('薪資', '50',  'A123456001', 600_000,  18_000, '台灣積體電路製造股份有限公司'),
            ('營利', '54C', 'A123456001', 900_000,       0, '元大台灣50 ETF'),
            ('利息', '5A',  'A123456001',  50_000,   5_000, '台灣銀行'),
        ],
    },
    {
        'filename': '02_自雇型_李小芳.pdf',
        'name':     '李小芳',
        'idn':      'A223456002',
        'year':     '112',
        'persona':  '自雇型',
        'note':     '薪資 ~31%｜執行業務 ~15%｜股利 ~54%',
        'records': [
            ('薪資',    '50',  'A223456002', 400_000,  12_000, '某設計公司'),
            ('執行業務', '9A',  'A223456002', 200_000,  20_000, '顧問服務業'),
            ('營利',    '54C', 'A223456002', 700_000,       0, '富邦金控'),
        ],
    },
    {
        'filename': '03_股利集中型_王大華.pdf',
        'name':     '王大華',
        'idn':      'A323456003',
        'year':     '112',
        'persona':  '股利集中型',
        'note':     '薪資 ~11%｜股利 ~85%｜利息 ~4%',
        'records': [
            ('薪資', '50',  'A323456003',   280_000,   8_400, '兼職顧問費'),
            ('營利', '54C', 'A323456003', 2_100_000,       0, '鴻海精密工業'),
            ('營利', '54C', 'A323456003',      5_000,       0, '台積電股利'),
            ('利息', '5A',  'A323456003',   100_000,  10_000, '第一銀行'),
        ],
    },
    {
        'filename': '04_保守固定型_陳美惠.pdf',
        'name':     '陳美惠',
        'idn':      'A423456004',
        'year':     '112',
        'persona':  '保守固定型',
        'note':     '薪資 ~19%｜股利 ~51%｜利息 ~29%',
        'records': [
            ('薪資', '50',  'A423456004', 150_000,   4_500, '政府機關'),
            ('營利', '54C', 'A423456004', 400_000,       0, '高股息ETF'),
            ('利息', '5A',  'A423456004', 160_000,  16_000, '合庫銀行定存'),
            ('利息', '5AM', 'A423456004',  70_000,   7_000, '郵局儲蓄存款'),
        ],
    },
    {
        'filename': '05_多元資產型_林志成.pdf',
        'name':     '林志成',
        'idn':      'A523456005',
        'year':     '112',
        'persona':  '多元資產型',
        'note':     '薪資 ~22%｜股利 ~50%｜租賃 ~15%｜利息 ~13%',
        'records': [
            ('薪資', '50',  'A523456005', 350_000,  10_500, '兼職薪資'),
            ('營利', '54C', 'A523456005', 800_000,       0, '元大高股息ETF'),
            ('租賃', '51',  'A523456005', 240_000,  24_000, '不動產租賃'),
            ('利息', '5A',  'A523456005', 210_000,  21_000, '中國信託銀行'),
        ],
    },
]


def fmt(n: int) -> str:
    """數字加千分位逗點"""
    return f'{n:,}'


def make_pdf(p: dict):
    path = os.path.join(OUTPUT_DIR, p['filename'])
    c = canvas.Canvas(path, pagesize=A4)
    W, H = A4

    def text(x, y, s, size=11):
        c.setFont(FONT_NAME, size)
        c.drawString(x, y, s)

    y = H - 60

    # ── 標題區 ───────────────────────────────────────────────
    text(W/2 - 160, y, f'財政部財政資訊中心', size=12)
    y -= 22
    text(W/2 - 200, y, f'{p["year"]}年度綜合所得稅各類所得資料清單', size=14)
    y -= 30
    c.line(50, y, W - 50, y)
    y -= 20

    text(50, y, f'所得人姓名：{p["name"]}')
    text(300, y, f'身分證統一編號：{p["idn"]}')
    y -= 20
    text(50, y, f'申請日期：{p["year"]}年12月01日')
    text(300, y, f'財務人物類型（示範）：{p["persona"]}')
    y -= 20
    text(50, y, f'所得結構備註：{p["note"]}')
    y -= 20
    c.line(50, y, W - 50, y)
    y -= 25

    # ── 欄位標題 ──────────────────────────────────────────────
    c.setFont(FONT_NAME, 10)
    c.drawString(50,  y, '類別')
    c.drawString(110, y, '證號別')
    c.drawString(155, y, '統一編號')
    c.drawString(265, y, '格式代號')
    c.drawString(335, y, '給付總額(元)')
    c.drawString(450, y, '扣繳稅額(元)')
    y -= 5
    c.line(50, y, W - 50, y)
    y -= 18

    # ── 所得記錄（格式與 pdf_parser.py 正規式相符）────────────
    total_income = 0
    total_wh     = 0
    for (cat, code, idn, amt, wh, unit) in p['records']:
        # 機器可讀行（parser 讀取這行）
        record_line = f'{cat} 0 {idn} {code} {fmt(amt)} {wh}'
        c.setFont(FONT_NAME, 10)
        c.drawString(50, y, record_line)
        y -= 15
        # 人類可讀行（扣繳單位說明）
        c.setFont(FONT_NAME, 9)
        c.setFillColorRGB(0.3, 0.3, 0.3)
        c.drawString(70, y, f'扣繳單位名稱：{unit}')
        c.setFillColorRGB(0, 0, 0)
        y -= 18
        total_income += amt
        total_wh     += wh

    # ── 合計行 ────────────────────────────────────────────────
    c.line(50, y, W - 50, y)
    y -= 18
    c.setFont(FONT_NAME, 11)
    c.drawString(50, y, f'給付總額(收入)合計：{fmt(total_income)}')
    c.drawString(330, y, f'扣繳稅額合計：{fmt(total_wh)}')

    # ── 頁尾說明 ──────────────────────────────────────────────
    y -= 40
    c.setFont(FONT_NAME, 9)
    c.setFillColorRGB(0.5, 0.5, 0.5)
    c.drawString(50, y, '※ 本資料為 FinCheck 系統示範用模擬資料，非真實納稅資料。')
    c.drawString(50, y - 15, '※ 格式參照財政部財政資訊中心「MyData 個人所得清單」。')

    c.save()
    print(f'✅ {path}  （總所得 {fmt(total_income)} 元，扣繳 {fmt(total_wh)} 元）')


if __name__ == '__main__':
    print(f'=== 生成 5 份模擬 MyData PDF ===\n')
    for p in PERSONAS:
        make_pdf(p)
    print(f'\n全部輸出至：{OUTPUT_DIR}/')
