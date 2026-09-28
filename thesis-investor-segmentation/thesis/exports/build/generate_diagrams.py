"""Generate real diagram images (PNG) to replace the ASCII box-drawing
architecture diagram (3.1) and research-process flowchart (3.2), which were
previously plain monospace text blocks. Requires matplotlib.

Run this BEFORE preprocess.py (see README.md) — preprocess.py references
the output PNGs by relative path.
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.font_manager import FontProperties

FONT_PATH = "/System/Library/Fonts/STHeiti Medium.ttc"
FONT = FontProperties(fname=FONT_PATH)
OUTDIR = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(OUTDIR, exist_ok=True)


def box(ax, x, y, w, h, lines, facecolor="#EAF2FB", edgecolor="#2C5F8A", fontsize=11, title_bold=True):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.06",
                                 linewidth=1.4, edgecolor=edgecolor, facecolor=facecolor))
    n = len(lines)
    for i, line in enumerate(lines):
        ty = y + h - (i + 0.6) * (h / n)
        weight = 'bold' if (title_bold and i == 0) else 'normal'
        fp = FontProperties(fname=FONT_PATH, weight=weight)
        ax.text(x + w / 2, ty, line, ha='center', va='center', fontproperties=fp, fontsize=fontsize)


def arrow(ax, x, y0, y1, label=None, label_fontsize=9):
    ax.add_patch(FancyArrowPatch((x, y0), (x, y1), arrowstyle='-|>', mutation_scale=16,
                                  linewidth=1.4, color="#2C5F8A"))
    if label:
        ax.text(x + 0.15, (y0 + y1) / 2, label, ha='left', va='center',
                 fontproperties=FONT, fontsize=label_fontsize, color="#444444")


def fig_architecture():
    fig, ax = plt.subplots(figsize=(7.5, 9))
    ax.set_xlim(0, 7.5)
    ax.set_ylim(0, 9)
    ax.axis('off')

    layers = [
        ("第一層：資料蒐集（3.3 節）",
         ["‧ 使用者網站行為資料（GA4／BigQuery）",
          "‧ 基金交易資料（內部交易資料庫）",
          "‧ 用戶屬性資料"]),
        ("第二層：特徵工程／資料前處理（3.4 節）",
         ["‧ 識別碼歸戶、缺值處理", "‧ RFM／行為特徵計算、標準化"]),
        ("第三層：投資人分群（3.5 節）",
         ["‧ K-prototypes 分群（K-means 僅作方法論對照）"]),
        ("第四層：個人化推薦模型（3.6 節）",
         ["‧ 熱門推薦（baseline）", "‧ 內容導向推薦（基於基金屬性相似度）",
          "‧ 協同過濾推薦（ALS）", "‧ 分群輔助協同過濾（結合分群結果，候選集篩選）"]),
        ("第五層：模型評估（3.7 節）",
         ["‧ Precision@K、Recall@K、MAP 等指標比較",
          "‧ 分析分群輔助模型相較基準模型之效益"]),
    ]
    interfaces = [
        "介面：原始事件列與欄位資料\n（user_id／user_pseudo_id 尚未串接）",
        "介面：訓練期使用者 × 特徵矩陣\n（僅以訓練期資料計算，防範資料洩漏）",
        "介面：分群標籤（每位使用者一個群體代號，訓練期資料）",
        "介面：依訓練期資料產出之 Top-K 推薦清單（供測試期評估）",
    ]

    box_w, gap = 6.5, 0.55
    box_h = [1.5, 1.15, 0.95, 1.55, 1.3]
    x0 = (7.5 - box_w) / 2
    y = 9.0
    centers_x = x0 + box_w / 2
    for i, (title, items) in enumerate(layers):
        h = box_h[i]
        y -= h
        box(ax, x0, y, box_w, h, [title] + items, fontsize=10.5)
        if i < len(interfaces):
            y -= gap
            ax.add_patch(FancyArrowPatch((centers_x, y + gap), (centers_x, y),
                                          arrowstyle='-|>', mutation_scale=16,
                                          linewidth=1.4, color="#2C5F8A"))
            ax.text(centers_x + 0.35, y + gap / 2, interfaces[i], ha='left', va='center',
                     fontproperties=FONT, fontsize=8.5, color="#555555")

    plt.tight_layout()
    out = os.path.join(OUTDIR, "fig_3_1_architecture.png")
    plt.savefig(out, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print("wrote", out)


def fig_process():
    fig, ax = plt.subplots(figsize=(8.5, 10.5))
    ax.set_xlim(0, 8.5)
    ax.set_ylim(0, 10.5)
    ax.axis('off')

    main_x, main_w = 0.8, 5.0
    side_x, side_w = 6.2, 2.0

    steps = [
        ("步驟 1：資料蒐集與整合規劃", "3.3 節", None),
        ("步驟 2：資料前處理與特徵工程", "3.4 節",
         "含識別碼歸戶、缺值處理、RFM／行為特徵計算、標準化\n依訓練期／測試期切分\n檢核點 A：歸戶率、缺值比例是否落於合理範圍？\n不通過 → 回頭調整步驟一取得範圍或步驟二處理規則"),
        ("步驟 3：投資人分群（回應 RQ1）", "3.5 節",
         "檢核點 B：分群品質指標（Silhouette 等）是否可接受？\n不通過 → 回頭調整步驟二特徵組合或標準化方式，重新分群"),
        ("步驟 4：個人化推薦模型建置", "3.6 節",
         "以訓練期資料訓練四種模型\n檢核點 C：分群輔助 CF 候選池是否過度稀疏？\n不通過 → 回頭調整步驟三分群數或候選集篩選門檻"),
        ("步驟 5：模型評估與比較", "3.7 節",
         "以測試期資料評估，回應 RQ2、RQ3\n檢核點 D：四模型指標是否均能計算（如 Recall 分母非零）？\n不通過 → 回頭檢視 3.7.1 節三層條件於步驟二之落實情況"),
        ("步驟 6：結果整合與應用建議", "呼應第四、五章", None),
    ]

    n = len(steps)
    top, bottom = 10.2, 0.3
    step_h = (top - bottom) / n * 0.62
    step_gap = (top - bottom) / n
    ys = [top - (i + 1) * step_gap + (step_gap - step_h) / 2 for i in range(n)]

    for i, (title, sec, note) in enumerate(steps):
        y = ys[i]
        box(ax, main_x, y, main_w, step_h, [f"{title}　── {sec}"], fontsize=10.5, facecolor="#EAF2FB")
        if note:
            fp_note = FontProperties(fname=FONT_PATH, weight='normal')
            ax.text(main_x + main_w + 0.15, y + step_h / 2, note, ha='left', va='center',
                     fontproperties=fp_note, fontsize=7.8, color="#555555", linespacing=1.6)
        if i < n - 1:
            cx = main_x + main_w / 2
            ax.add_patch(FancyArrowPatch((cx, y), (cx, ys[i + 1] + step_h),
                                          arrowstyle='-|>', mutation_scale=15,
                                          linewidth=1.3, color="#2C5F8A"))

    # 側支：測試期資料保留，不進入步驟 3–4（從步驟 2 底部分岔，於步驟 5 頂部匯流）
    y2_bottom = ys[1]
    y3_top = ys[2] + step_h
    y4_bottom = ys[3]
    y5_top = ys[4] + step_h
    cx_main = main_x + main_w / 2
    side_cx = side_x + side_w / 2
    box(ax, side_x, (y4_bottom + y3_top) / 2 - 0.55, side_w, 1.1,
        ["測試期資料保留", "（不進入步驟 3–4）"], fontsize=8.5, facecolor="#FBF3E4",
        edgecolor="#B8860B", title_bold=False)
    ax.add_patch(FancyArrowPatch((cx_main, y2_bottom), (side_cx, (y4_bottom + y3_top) / 2 + 0.55),
                                  arrowstyle='-|>', mutation_scale=13, linewidth=1.1,
                                  color="#B8860B", connectionstyle="arc3,rad=0.15"))
    ax.add_patch(FancyArrowPatch((side_cx, (y4_bottom + y3_top) / 2 - 0.55), (cx_main, y5_top),
                                  arrowstyle='-|>', mutation_scale=13, linewidth=1.1,
                                  color="#B8860B", connectionstyle="arc3,rad=0.15"))

    plt.tight_layout()
    out = os.path.join(OUTDIR, "fig_3_2_process_flow.png")
    plt.savefig(out, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print("wrote", out)


if __name__ == "__main__":
    fig_architecture()
    fig_process()
