"""
MyData 個人所得資料 PDF 解析器
支援財政部「年度綜合所得稅各類所得資料清單」格式

pdfplumber 提取到的每筆所得格式為單行：
  [類別] 0 [IDN] [格式代號(可能含浮水印字)] (T)? [給付總額(可能含浮水印字)] [扣繳稅額] [資料來源] [可扣抵稅額]
例：
  營利 0 A220000000 54C T 220 0 88399314 0
  薪資 0 A220000000 部50 677,328 0 42862697 0
  利息 0 A220000000 5AM 1,461 0 27249314 0
"""
import re
import io
from typing import Union


# ── 浮水印字元（財政部臺北國稅局中正分局 的各字）─────────
# 注意：「財」排除在外，避免與「財產交易」撞名
WMARK_CHARS = '政部臺北國稅局中正分'
WMARK       = f'[{WMARK_CHARS}]*'   # 0 到多個浮水印字元

# ── 台灣綜所稅格式代號 → 系統分類 ─────────────────────────
FORMAT_CODE_MAP = {
    '50':  'salary',
    '54':  'dividend',
    '54C': 'dividend',
    '54B': 'dividend',
    '5A':  'interest',
    '5AM': 'interest',
    '5AB': 'interest',
    '51':  'rental',
    '51A': 'rental',
    '9A':  'business',
    '9B':  'business',
}

# 中文類別備用對應（格式代號未命中時使用）
CATEGORY_ZH_MAP = {
    '薪資':   'salary',
    '營利':   'dividend',
    '利息':   'interest',
    '租賃':   'rental',
    '執行業務': 'business',
    '財產交易': 'other',
    '其他':   'other',
    '競技':   'other',
    '稿費':   'business',
}

# ── 格式代號對應函式 ───────────────────────────────────────
def _map_code(raw_code: str, cat_zh: str) -> str:
    """從原始格式代號（可能含浮水印）解析系統分類。"""
    # 移除浮水印字元，保留字母數字
    code = re.sub(f'[{WMARK_CHARS}財]', '', raw_code)
    if code in FORMAT_CODE_MAP:
        return FORMAT_CODE_MAP[code]
    # 前綴推斷
    if re.match(r'^50', code):    return 'salary'
    if re.match(r'^5[34]', code): return 'dividend'
    if re.match(r'^5[AB]', code): return 'interest'
    if re.match(r'^51', code):    return 'rental'
    if re.match(r'^9',  code):    return 'business'
    # fallback：從中文類別
    return CATEGORY_ZH_MAP.get(cat_zh, 'other')


# ── 核心正規式 ─────────────────────────────────────────────
#
# 行樣本：
#   營利 0 A220000000 54C T 220 0 88399314 0
#   薪資 0 A220000000 部50 677,328 0 42862697 0
#   營利 0 A220000000 54C T 局211 0 88399314 0
#
# 群組說明：
#   1  類別（薪資/營利/利息/...）
#   2  格式代號（含浮水印，如 部50、54C）
#   3  給付總額（含浮水印，如 局211、220）
#   4  扣繳稅額

_RECORD_RE = re.compile(
    r'(薪資|營利|利息|租賃|執行業務|財產交易|其他|競技)'  # group 1: 類別
    r'\s+0\s+'                                            # 固定的「0」（證號別）
    r'[A-Z]\d+'                                           # IDN（身分證字號）
    r'\s+' + WMARK +                                      # 浮水印前綴（可選）
    r'([A-Z0-9]{2,5})'                                    # group 2: 格式代號主體
    r'[A-Z]?' + WMARK +                                   # 尾端浮水印（可選）
    r'(?:\s+T)?'                                          # T 旗標（可選）
    r'\s+' + WMARK +                                      # 浮水印前綴（可選）
    r'([\d,]+)'                                           # group 3: 給付總額
    r'\s+(\d+)'                                           # group 4: 扣繳稅額
)


# ── 小工具：PDF → 純文字 ──────────────────────────────────
def _extract_text(file_obj) -> str:
    import pdfplumber
    parts = []
    with pdfplumber.open(file_obj) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                parts.append(t)
    return '\n'.join(parts)


# ── 解析主函式 ────────────────────────────────────────────
def _parse_text(text: str) -> dict:
    """
    從 pdfplumber 提取的字串解析各類所得。
    回傳結構：
      taxpayer_name, tax_year, records, totals, raw_total
    """
    lines = text.split('\n')

    # 取納稅人姓名
    taxpayer_name = ''
    tax_year      = ''
    for line in lines:
        m = re.search(r'所得人姓名：\s*([\u4e00-\u9fff]+)', line)
        if m and not taxpayer_name:
            taxpayer_name = m.group(1)
        m = re.search(r'(\d+)年度綜合所得稅', line)
        if m and not tax_year:
            tax_year = m.group(1) + '年度'

    # 解析每筆所得記錄
    records    = []
    for line in lines:
        m = _RECORD_RE.search(line)
        if not m:
            continue
        cat_zh   = m.group(1)
        raw_code = m.group(2)
        category = _map_code(raw_code, cat_zh)

        # 清除千分位逗點
        amount   = int(m.group(3).replace(',', ''))
        wh_amt   = int(m.group(4))

        if amount <= 0:
            continue

        # 解析扣繳單位名稱（同行或下一行）
        unit_match = re.search(r'扣繳單位名稱：\s*(.+)', line)
        unit = unit_match.group(1).strip() if unit_match else ''

        records.append({
            'category':   category,
            'source':     unit,
            'format':     re.sub(f'[{WMARK_CHARS}財]', '', raw_code),
            'amount':     amount,
            'withholding': wh_amt,
        })

    # 補上扣繳單位名稱（從下一行「扣繳單位名稱：」取得）
    for i, rec in enumerate(records):
        if rec['source']:
            continue
        # 找到此筆金額在 lines 中的位置，往後搜尋
        target = str(rec['amount']).replace(',', '')
        for j, line in enumerate(lines):
            if re.search(rf'\b{target}\b', line.replace(',', '')):
                for k in range(j, min(j + 4, len(lines))):
                    um = re.search(r'扣繳單位名稱：\s*(.+)', lines[k])
                    if um:
                        rec['source'] = um.group(1).strip()
                        break
                break

    # 彙整各類合計
    totals   = {c: 0 for c in ['salary', 'dividend', 'interest',
                                 'rental', 'business', 'other']}
    total_wh = 0
    for r in records:
        totals[r['category']] += r['amount']
        total_wh              += r['withholding']

    total_income = sum(totals.values())

    # 交叉驗證：從 PDF 底部「給付總額(收入)合計」行取合計數字
    raw_total  = 0
    total_found = False
    for i, line in enumerate(lines):
        if '給付總額' in line and '合計' in line:
            # 合計數字可能在同行或接下來幾行
            for chunk in lines[i:i+5]:
                nums = re.findall(r'[\d,]+', chunk)
                for n in nums:
                    v = int(n.replace(',', ''))
                    if v > 1000:   # 避免筆數等小數字
                        raw_total   = v
                        total_found = True
                        break
                if total_found:
                    break
            break

    return {
        'taxpayer_name': taxpayer_name,
        'tax_year':      tax_year,
        'records':       records,
        'totals': {
            **totals,
            'withholding_tax': total_wh,
            'total_income':    total_income,
        },
        'raw_total': raw_total,
    }


# ── 公開 API ──────────────────────────────────────────────
def parse_mydata_pdf(file_obj: Union[str, bytes, io.IOBase]) -> dict:
    """
    解析 MyData 個人所得資料 PDF，回傳結構化資料。

    Returns
    -------
    {
      'taxpayer_name': str,
      'tax_year': str,
      'records': [...],
      'totals': {salary, dividend, interest, rental, business, other,
                 withholding_tax, total_income},
      'raw_total': int,
      'match_ok': bool,   # computed vs PDF 合計一致性
    }
    """
    text   = _extract_text(file_obj)
    result = _parse_text(text)

    computed = result['totals']['total_income']
    raw      = result['raw_total']
    # 允許 ±1 元誤差（千分位捨入）
    result['match_ok'] = (raw == 0 or abs(computed - raw) <= 1)
    return result


# ── CLI 測試 ──────────────────────────────────────────────
if __name__ == '__main__':
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else \
        '/Users/Janice/Desktop/在職碩班文件/個人資料所得_20260502.pdf'

    r = parse_mydata_pdf(path)
    print(f"納稅義務人：{r['taxpayer_name']}  {r['tax_year']}")
    print(f"所得筆數  ：{len(r['records'])} 筆")
    print(f"合計驗證  ：{'✅' if r['match_ok'] else '⚠️ 有差異'}")
    if not r['match_ok']:
        print(f"  計算合計：{r['totals']['total_income']:,}")
        print(f"  PDF 合計：{r['raw_total']:,}")
    print()
    t = r['totals']
    label_map = [('salary','薪資'),('dividend','股利'),('interest','利息'),
                 ('rental','租賃'),('business','執行業務'),('other','其他')]
    for cat, zh in label_map:
        if t[cat]:
            print(f"  {zh:6s}：{t[cat]:>10,} 元")
    print(f"  {'扣繳稅額':6s}：{t['withholding_tax']:>10,} 元")
    print(f"  {'合計':6s}：{t['total_income']:>10,} 元")
    print()
    print("  明細：")
    for rec in r['records']:
        src = rec['source'][:20] if rec['source'] else '—'
        print(f"    [{rec['category']:8s}] {src:<22} {rec['amount']:>10,} 元  扣繳 {rec['withholding']:,}")
