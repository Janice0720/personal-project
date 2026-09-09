---
name: study-tutor
description: Use only when the user explicitly names study-tutor, says 請用 study-tutor, or says 幫我調用這個 skill / 幫我調用 study-tutor.
disable-model-invocation: true
---

# Study Tutor

把問題變成一本使用者合上檔案後，能用自己的話講出來的課本。對話裡的速覽不是交付物。

讀完本檔後立刻讀 [learner-profile.md](references/learner-profile.md) 與 [textbook-template.md](references/textbook-template.md)。寫檔前必須填滿模板欄位。

## 步驟

1. **對上範圍。** 課內（對得上 `school-notes/` 某門課）或課外。不確定就問一句再寫。
2. **備課。** 課內：先讀該課 `README.md` 與既有筆記。課外：對外搜集可靠來源。指定教科書優先於部落格。
3. **寫課本檔。** 即使用戶說「不用寫檔／對話就好／條列就好／趕時間」，仍要寫檔。對話最多給 5 行速覽，並指出檔案路徑。
4. **教到會。** 嚴格照模板順序：問題 → 人話定義 → 例子 → 理論 → 適用邊界 → 與已知概念的連結 → 3 題自測。公式只出現在人話與例子之後；每個符號先講人話。
5. **深度停在能學會。** 主文停在「合上書能轉述」。使用者說「數學愈完整愈好」時，把證明放進文末「想看推導再讀」，不得佔主文。

## 檔案位置

| 情況 | 路徑 |
|------|------|
| 使用者點了週次 | `school-notes/{課}/weekNN-{主題}.md` |
| 課內概念題 | `school-notes/{課}/explain-{主題}.md` |
| 完全課外 | `school-notes/self-study/explain-{主題}.md` |

課內但超出該週進度：仍放該課資料夾，文首標「課外延伸」。不要改課程 `README.md`。

## 紅旗 — 停下重寫

- 只在聊天視窗教完
- 第一個實質段落就是公式或專有名詞堆疊
- 主文出現 Hoeffding / VC 維度 / Rademacher，但使用者沒有要求證明
- 沒有 3 題自測，或自測是讓人默寫不等式
- 沒有來源

| 藉口 | 實際 |
|------|------|
| 用戶說不用寫檔、趕時間 | 點名這個 skill = 要留下課本 |
| 條列就好 | 對話可條列；檔案仍要寫成課本 |
| 數學愈完整愈好 | 先教到會，推導進文末選讀 |
| 這題很簡單不用自測 | 自測是必填欄 |

## 不要做

不要做間隔複習系統、Obsidian 儀表板、學習計畫。不要代寫作業或考試答案當正文。
