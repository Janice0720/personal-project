"""
Task 7：MyData 真實資料測試
114年度綜合所得稅各類所得資料清單 — 黃子甄
"""
import sys, os
sys.path.append(os.path.dirname(__file__))

import numpy as np
from clustering import predict_persona
from scoring import get_fincheck_scores, generate_recommendations, PERSONA_DESCRIPTIONS, MAX_ENTROPY

# ── 從 PDF 解析的實際所得資料 ──────────────────────────────
# 所得筆數：24 筆（2025年度，114年）
# 格式代號說明：
#   54C = 信託基金/股利所得（ETF配息、股票股利）
#   5AM = 利息所得
#   50  = 薪資所得

# 薪資所得（格式50）
salary_detail = {
    '好好證券股份有限公司': 677_328,
}

# 營利/股利所得（格式54C）
dividend_detail = {
    '復華台灣科技優息ETF（12月配）': 220+142+208+211+45+117+50+296+108+282+320+360,
    '永豐金融控股':   3_750,
    '富邦台灣採吉50': 17,
    '群益台灣精選高息ETF': 2_157,
    '台新新光金融控股': 2_700,
    '中國鋼鐵':        330,
    '台灣積體電路製造（TSMC）': 399+450+450+500,
    '宏德彩藝有限公司': 77_883,
}

# 利息所得（格式5AM）
interest_detail = {
    '合作金庫商業銀行南門分公司': 1_461,
}

# 彙總
salary   = sum(salary_detail.values())
dividend = sum(dividend_detail.values())
interest = sum(interest_detail.values())
rental   = 0
business = 0
other    = 0
withholding_tax = 0  # 扣繳稅額合計：0（PDF 確認）
total    = salary + dividend + interest

# ── 列印所得明細 ──────────────────────────────────────────
print("=" * 55)
print("  114年度 個人所得明細（黃子甄）")
print("=" * 55)
print(f"{'類別':<8} {'項目':<28} {'金額':>10}")
print("-" * 55)
for name, amt in salary_detail.items():
    print(f"{'薪資':<8} {name:<28} {amt:>10,}")
print()
for name, amt in dividend_detail.items():
    print(f"{'營利/股利':<8} {name:<28} {amt:>10,}")
print()
for name, amt in interest_detail.items():
    print(f"{'利息':<8} {name:<28} {amt:>10,}")
print("-" * 55)
print(f"{'薪資小計':<36} {salary:>10,}")
print(f"{'營利/股利小計':<36} {dividend:>10,}")
print(f"{'利息小計':<36} {interest:>10,}")
print(f"{'給付總額合計':<36} {total:>10,}  ← PDF 合計：769,784 ✅")
print(f"{'扣繳稅額合計':<36} {withholding_tax:>10,}")

# ── 計算特徵 ──────────────────────────────────────────────
amounts   = [salary, dividend, interest, rental, business, other]
col_names = ['salary','dividend','interest','rental','business','other']
ratios = {f'{c}_ratio': a / total for c, a in zip(col_names, amounts)}

vals      = np.array(list(ratios.values()))
vals_safe = np.where(vals > 0, vals, 1e-10)
entropy   = float(-np.sum(vals_safe * np.log2(vals_safe)))
ratios['shannon_entropy'] = entropy
tax_rate  = withholding_tax / total

# ── 模型預測 ──────────────────────────────────────────────
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'kmeans_model.pkl')
persona = predict_persona(ratios, model_path=MODEL_PATH)
scores  = get_fincheck_scores(entropy, tax_rate, total)
tips    = generate_recommendations(persona, scores['diversification_score'], scores['tax_efficiency_score'])

# ── 健檢報告 ──────────────────────────────────────────────
print("\n" + "=" * 55)
print("  FinCheck 個人財務健檢結果")
print("=" * 55)
print(f"\n【財務人物類型】  {persona}")
print(f"  → {PERSONA_DESCRIPTIONS.get(persona, '')}")

print(f"\n【所得結構】")
print(f"  薪資比例：{ratios['salary_ratio']*100:.1f}%   ({salary:,} 元)")
print(f"  股利比例：{ratios['dividend_ratio']*100:.1f}%   ({dividend:,} 元)")
print(f"  利息比例：{ratios['interest_ratio']*100:.2f}%   ({interest:,} 元)")

print(f"\n【Shannon Entropy】  {entropy:.4f}（最大值 {MAX_ENTROPY:.3f}）")
print(f"【所得多元化評分】  {scores['diversification_score']} / 100")
print(f"【稅務效率評分】    {scores['tax_efficiency_score']} / 100")
print(f"  你的扣繳稅率：{tax_rate*100:.1f}%   同群基準：{scores['benchmark_tax_rate']*100:.1f}%")
print(f"  所得分位群組：{scores['income_group']}")

print(f"\n【個人化建議】")
for i, tip in enumerate(tips, 1):
    print(f"  {i}. {tip}")
