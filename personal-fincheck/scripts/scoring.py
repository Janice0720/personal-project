"""
評分模組：所得多元化評分、稅務效率評分、規則引擎建議
"""
import numpy as np

# Shannon Entropy 最大值（6 類所得完全均等）= log2(6)
MAX_ENTROPY = np.log2(6)

# 各所得群組的基準扣繳稅率。
# 依財政部「111 年度綜合所得稅申報核定統計專冊」中各分位的
# 應納稅額佔所得總額比率推算，資料檔位於：
#   data/raw/111_綜所稅各類所得5分位統計.csv
# 對應群組定義見 classify_income_group()。
BENCHMARK_TAX_RATES = {
    'low':      0.05,
    'mid_low':  0.08,
    'mid':      0.11,
    'mid_high': 0.14,
    'high':     0.17,
}

# 各人物類型的文字描述
PERSONA_DESCRIPTIONS = {
    '股利集中型': '你的所得高度依賴股利收入（平均佔 72%），投資組合集中。',
    '薪資投資型': '薪資與股利各佔約三到五成，是兼顧工作與投資的均衡型態。',
    '保守固定型': '利息收入比例偏高，偏好穩定固定收益型資產（定存/債券）。',
    '多元資產型': '股利、租賃、利息三類所得並重，是最多元分散的資產配置型。',
    '自雇型':    '執行業務所得佔約 14.5%，兼具股利收入，屬於自雇或兼業型的複合所得結構。',
}


def score_diversification(shannon_entropy: float) -> int:
    """所得多元化評分（0～100），Shannon Entropy 越高 → 評分越高"""
    score = (shannon_entropy / MAX_ENTROPY) * 100
    return int(np.clip(score, 0, 100))


def score_tax_efficiency(user_tax_rate: float, benchmark_tax_rate: float) -> int:
    """
    稅務效率評分（0～100）。
    低於基準稅率 → 高分；高於基準稅率 → 低分。
    """
    if benchmark_tax_rate == 0:
        return 50
    diff = benchmark_tax_rate - user_tax_rate
    score = 50 + (diff / benchmark_tax_rate) * 50
    return int(np.clip(score, 0, 100))


def classify_income_group(total_income: float) -> str:
    """依總所得判斷所屬分位群組。

    切點設計說明
    ------------
    本函數的分群切點以「fincheck 目標用戶族群」為設計基準，
    而非全體綜所稅申報戶的等分位邊界。目標用戶為具有多元投資
    所得（股利、利息、租賃等）的中高所得族群。

    參考資料：財政部財政資訊中心「111 年度綜合所得稅申報核定
    統計專冊」，資料檔位於 data/raw/111_綜所稅各類所得5分位統計.csv。

    全體申報戶分佈背景（111 年度，約 663 萬戶）：
      - 全國平均薪資收入：91.60 萬元
      - 5 等分位平均薪資收入：197.74 / 140.22 / 119.33 / 103.17 / 74.41 萬元
        （由高至低：第1分位 P80–100 → 第5分位 P0–20）

    切點與全體分佈的對應關係（估算）：
      < 100 萬  → 約 P0–P40（全體中低收入，但已為本工具用戶的入門門檻）
      100–130 萬 → 約 P40–P60
      130–160 萬 → 約 P60–P80
      160–200 萬 → 約 P80–P90
      ≥  200 萬  → 約 P90 以上

    注意：若需嚴格對齊全體等分位邊界，請改用官方 5 等分位數據
    重新校準切點。
    """
    if total_income < 1_000_000:
        return 'low'
    elif total_income < 1_300_000:
        return 'mid_low'
    elif total_income < 1_600_000:
        return 'mid'
    elif total_income < 2_000_000:
        return 'mid_high'
    else:
        return 'high'


def get_fincheck_scores(shannon_entropy: float,
                        user_tax_rate: float,
                        total_income: float) -> dict:
    """整合健檢評分，回傳各維度分數字典"""
    group = classify_income_group(total_income)
    bench = BENCHMARK_TAX_RATES[group]
    return {
        'income_group': group,
        'diversification_score': score_diversification(shannon_entropy),
        'tax_efficiency_score': score_tax_efficiency(user_tax_rate, bench),
        'benchmark_tax_rate': bench,
        'user_tax_rate': user_tax_rate,
    }


def generate_recommendations(persona: str,
                              diversification_score: int,
                              tax_efficiency_score: int) -> list:
    """根據人物類型與評分，回傳 3 條個人化理財建議"""
    tips = []

    # 所得多元化建議
    if diversification_score < 35:
        tips.append("所得來源高度集中，建議逐步布局不同資產類別（如债券 ETF、REITs）以分散風險。")
    elif diversification_score < 65:
        tips.append("所得多元化程度中等，可考慮增加穩定固定收益資產（如投資等級債券），降低整體波動。")
    else:
        tips.append("所得來源相當多元，財務結構穩健，建議定期檢視各資產比例是否符合當前人生階段規劃。")

    # 稅務效率建議
    if tax_efficiency_score < 45:
        tips.append("稅務負擔率高於同所得層平均，建議檢視可申報的合法扣除額（如捐贈、醫療費用、房貸利息），或諮詢理財顧問。")
    elif tax_efficiency_score < 70:
        tips.append("稅務效率尚可，可留意每年 5 月申報期的退稅機會，善用各類所得的扣除優惠。")
    else:
        tips.append("稅務效率良好，持續保持現有規劃，並可考慮善用股利所得的分離課稅（28%）與合併計稅的利弊比較。")

    # 人物類型專屬建議
    persona_tips = {
        '股利集中型': "股利佔比偏高，建議評估個股集中度，若超過 3 成在單一標的，可分散至寬基 ETF 降低個股風險。",
        '薪資投資型': "薪資與股利均衡是良好基礎，建議優先建立 6 個月緊急預備金後，再提高投資配置比例。",
        '保守固定型': "利息所得偏高代表持有較多定存或債券，在升息循環結束後，可評估是否部分轉向股息型資產以提升長期報酬。",
        '多元資產型': "資產配置最為分散，理財觀念成熟，建議定期再平衡（Rebalancing），維持各類資產在目標比例範圍內。",
        '自雇型':    "執行業務所得為浮動性收入，建議強化退休準備（如勞退自提 6%），並考慮保障型保險填補社會保險缺口。",
    }
    tips.append(persona_tips.get(persona, "建議定期進行財務健檢，根據人生階段調整資產配置策略。"))

    return tips
