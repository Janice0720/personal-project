# 安裝指引：Whisper 語音轉文字環境

## 1. 安裝 ffmpeg（必要）

```bash
brew install ffmpeg
```

## 2. 安裝 OpenAI Whisper

```bash
pip install openai-whisper
```

> 若使用 conda：
> ```bash
> conda install -c conda-forge ffmpeg
> pip install openai-whisper
> ```

## 3. 確認安裝

```bash
whisper --version
ffmpeg -version
```

## 4. 模型選擇建議

| 模型   | 檔案大小 | 速度 | 準確度 | 適用情境           |
|--------|--------|------|--------|-------------------|
| tiny   | 39 MB  | 最快 | 最低   | 快速測試           |
| base   | 74 MB  | 快   | 低     | 快速測試           |
| small  | 244 MB | 中   | 中     | 個人筆記，速度優先  |
| medium | 769 MB | 慢   | 高     | **一般上課錄音**（建議）|
| large  | 1.5 GB | 最慢 | 最高   | 雜訊多或專業術語多  |

## 5. 首次執行注意

首次執行時，Whisper 會自動下載模型至 `~/.cache/whisper/`，  
medium 模型約 769MB，請確保網路連線正常。
