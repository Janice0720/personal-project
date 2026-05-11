"""Task 5 驗證：測試評分模組"""
import sys, os
sys.path.append(os.path.dirname(__file__))
from scoring import score_diversification, score_tax_efficiency, get_fincheck_scores, generate_recommendations
import numpy as np

MAX_ENTROPY = np.log2(6)

# 測試 1：純股利所得，entropy 極低
entropy_pure_dividend = -(1.0 * np.log2(1.0) + 5 * 1e-10 * np.log2(1e-10))
s1 = score_diversification(0.01)
assert s1 < 5, f"純集中所得應 < 5 分，得到 {s1}"
print(f"✅ 測試1 純集中：多元化評分 = {s1}")

# 測試 2：完全均等所得，entropy 最高
s2 = score_diversification(MAX_ENTROPY)
assert s2 == 100, f"完全均等應為 100，得到 {s2}"
print(f"✅ 測試2 完全均等：多元化評分 = {s2}")

# 測試 3：稅率低於基準 → 高分
s3 = score_tax_efficiency(user_tax_rate=0.04, benchmark_tax_rate=0.08)
assert s3 > 50, f"稅率低於基準應 > 50 分，得到 {s3}"
print(f"✅ 測試3 低稅率：稅務效率評分 = {s3}")

# 測試 4：稅率高於基準 → 低分
s4 = score_tax_efficiency(user_tax_rate=0.15, benchmark_tax_rate=0.08)
assert s4 < 50, f"稅率高於基準應 < 50 分，得到 {s4}"
print(f"✅ 測試4 高稅率：稅務效率評分 = {s4}")

# 測試 5：整合健檢評分
result = get_fincheck_scores(shannon_entropy=1.5, user_tax_rate=0.10, total_income=1_200_000)
print(f"✅ 測試5 整合評分：{result}")

# 測試 6：建議產出
tips = generate_recommendations('薪資投資型', 60, 55)
assert len(tips) == 3, "應產出 3 條建議"
print(f"✅ 測試6 建議文字：")
for i, t in enumerate(tips, 1):
    print(f"   {i}. {t}")

print("\n✅ 所有評分模組測試通過")

# 測試：自雇型人物建議包含退休規劃相關文字
tips_ziyong = generate_recommendations('自雇型', diversification_score=50, tax_efficiency_score=60)
assert any('退休' in t or '勞退' in t for t in tips_ziyong), "自雇型建議應包含退休相關文字"
print("自雇型建議測試通過：", tips_ziyong[-1])

# 測試：PERSONA_DESCRIPTIONS 包含全部 5 種人物
from scoring import PERSONA_DESCRIPTIONS
assert len(PERSONA_DESCRIPTIONS) == 5, f"應有 5 種人物描述，實際有 {len(PERSONA_DESCRIPTIONS)} 種"
assert '自雇型' in PERSONA_DESCRIPTIONS, "PERSONA_DESCRIPTIONS 缺少自雇型"
print("人物描述數量驗證通過：", list(PERSONA_DESCRIPTIONS.keys()))
