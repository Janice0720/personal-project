# 重新產生第一至三章 Word 檔

依國立臺北商業大學資訊與決策科學研究所論文格式規範（`論文格式參考(1100113新修).doc`）建立：
邊界上下 2.5cm、左 3.5cm、右 2.5cm；本文 12pt 標楷體、1.5 倍行距；
章標題 18pt 置中、節標題（X.Y）18pt 靠左、小節（X.Y.Z）16pt、更深層 14pt，皆為粗體標楷體。

## 使用方式

第一到三章之 markdown 內容修改後，若要重新產生 Word 檔，依序執行：

```bash
cd thesis/exports/build

# 1. 重建格式範本（僅在格式規則需要調整時才需要重跑）
python3 build_reference.py

# 2. 讀取 thesis/chapters/ 底下第一至三章目前內容，組合並正確調整標題階層
python3 preprocess.py

# 3. 轉為 Word 檔（含自動產生之目錄欄位，開啟後於 Word 按 Ctrl+A 再 F9 可更新頁碼）
pandoc combined.md -f markdown+tex_math_dollars -o ../第一至三章初稿.docx \
  --reference-doc=reference.docx --toc --toc-depth=3
```

需要 Python 套件 `python-docx`（`pip3 install python-docx`）與 `pandoc`（`brew install pandoc`）。

## 已知限制（未涵蓋於此檔案）

- 僅包含第一至三章「內文」（標題＋正文），不含封面、書名頁、口試委員審定書、
  中英文摘要、誌謝、參考文獻頁——這些需要指導教授姓名、正式摘要文字等
  尚未底定之資訊，需另行加入。
- 參考文獻清單本身未附於此檔案（各章內文中之作者年份引用已保留，正式
  參考文獻頁待彙整 `thesis/chapters/references-draft.md` 後另行加入，
  並依格式規範採 APA、中文文獻在前、依筆劃排序）。
- 標楷體字型於 Windows／Word 環境（如 DFKai-SB）通常已內建，若在缺乏
  該字型之電腦開啟，文字仍會顯示但可能以替代字型呈現。
