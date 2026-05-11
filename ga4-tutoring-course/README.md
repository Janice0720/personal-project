# GA4 家教課程教材專案

本專案為線上家教課程的教材資料庫，針對基礎概念尚不完備的學生，設計一套從環境建置到視覺化報表的 GA4 與 GTM 系統化十二週課程。

## 目錄

- [1. 專案目標](#1-專案目標)
- [2. 學生背景](#2-學生背景)
- [3. 課程總覽](#3-課程總覽)
- [4. 教材結構](#4-教材結構)
- [5. 參考資源](#5-參考資源)

## 1. 專案目標

- **驗證假設**：透過系統化的教材設計，驗證「由底層邏輯出發」的教學方式是否能有效幫助零基礎學生建立數據分析能力
- **方法**：以十二週為期，從 GTM 環境佈署到 Looker Studio 儀表板設計，逐步建構完整的數據分析技能
- **預期成果**：學生能獨立完成「需求定義 → 代碼佈署 → 報表分析」的完整數據分析流程

## 2. 學生背景

| 項目 | 說明 |
|------|------|
| 品牌網站 | [MovieTribe](https://www.movietribe.club/) — 電影主題社群網站 |
| 目前狀態 | 網站尚未安裝 GTM、GA4 基礎設定不完整 |
| 基礎程度 | 不熟悉維度（Dimensions）、指標（Metrics）等核心概念 |
| 學習需求 | 希望了解探索報表（Explorations）與 Looker Studio 視覺化 |

## 3. 課程總覽

十二週課程分為四大階段，每週 60 分鐘線上授課：

```
┌─────────────────────────────────────────────────────┐
│              十二週 GA4 系統化課程                      │
├─────────────┬─────────────┬─────────────┬───────────┤
│  第一階段    │  第二階段    │  第三階段    │ 第四階段   │
│  Week 1-3   │  Week 4-6   │  Week 7-9   │ Week 10-12│
│             │             │             │           │
│ 環境佈署    │ 事件追蹤    │ 深度探索    │ 視覺化    │
│ 與底層邏輯  │ 與參數實務  │ 與行為分析  │ 與綜合應用 │
└─────────────┴─────────────┴─────────────┴───────────┘
```

| 階段 | 週次 | 主題 | 核心目標 |
|------|------|------|----------|
| 第一階段 | Week 1-3 | 環境佈署與底層邏輯 | 完成 GTM/GA4 安裝，理解維度與指標 |
| 第二階段 | Week 4-6 | 事件追蹤與參數實務 | 掌握四大事件類別，完成自訂事件設定 |
| 第三階段 | Week 7-9 | 深度探索與行為分析 | 運用探索報表進行進階行為分析 |
| 第四階段 | Week 10-12 | 視覺化呈現與綜合應用 | 打造 Looker Studio 專業儀表板 |

## 4. 教材結構

```
ga4-tutoring-course/
├── README.md                          # 本文件：專案總覽
├── data/                              # 課程使用的資料與素材
├── materials/                         # 教材主體
│   ├── phase-1/                       # 第一階段：環境佈署與底層邏輯
│   │   ├── week-01-ga4-setup.md       #   Week 1：GA4 環境搭建
│   │   ├── week-02-dimensions-metrics.md #   Week 2：維度與指標
│   │   └── week-03-gtm-fundamentals.md #   Week 3：GTM 基礎
│   ├── phase-2/                       # 第二階段：事件追蹤與參數實務
│   │   ├── week-04-auto-events.md     #   Week 4：自動與加強型事件
│   │   ├── week-05-custom-events.md   #   Week 5：自訂事件實作
│   │   └── week-06-params-conversion.md #   Week 6：參數註冊與轉換
│   ├── phase-3/                       # 第三階段：深度探索與行為分析
│   │   ├── week-07-standard-reports.md #   Week 7：標準報表導讀
│   │   ├── week-08-freeform-segments.md #   Week 8：自由形式與區隔
│   │   └── week-09-funnel-path.md     #   Week 9：漏斗與路徑探索
│   └── phase-4/                       # 第四階段：視覺化呈現與綜合應用
│       ├── week-10-looker-basics.md   #   Week 10：Looker Studio 基礎
│       ├── week-11-dashboard-design.md #   Week 11：進階儀表板設計
│       └── week-12-final-review.md    #   Week 12：總結與專案驗收
└── output/                            # 分析結果與課程產出
```

## 5. 參考資源

### 官方文件
- [GA4 官方說明文件](https://support.google.com/analytics/?hl=zh-Hant)
- [GTM 官方說明文件](https://support.google.com/tagmanager/?hl=zh-Hant)
- [Looker Studio 官方說明文件](https://support.google.com/looker-studio/?hl=zh-Hant)
- [GA4 示範帳戶](https://support.google.com/analytics/answer/6367342?hl=zh-Hant)

### 中文教學資源
- [集客數據行銷 — 2026 GA4 教學大解密](https://inboundmarketing.com.tw/ga4%E6%95%99%E5%AD%B8/)
- [圖靈數位 — 2026 最新版 GA4 完全攻略](https://www.turingdigital.com.tw/blog/ga4p-complete-guide)
- [Haran 的行銷筆記 — GA4 教學合集](https://www.haranhuang.com/google-analytics-4-tutorial-collection.html)
- [MKTGholic 行銷癮 — GTM 三大支柱教學](https://mktgholic.com/google-tag-manager/what-is-gtm-tag-trigger-variables/)
- [STEAM 教育學習網 — GA4 教學系列](https://steam.oxxostudio.tw/category/ga4/content/dimensions-metrics.html)
- [數據行銷讚 — 2026 Looker Studio 入門教學](https://tzuhsiang.com/looker-studio/google-looker-studio-beginners-tutorial/)
- [NICROW — Looker Studio 完整教學](https://nicrow.com/data-analysis/looker-studio-guide/)

### 教學方法論
- **類比式教學**：將抽象技術概念轉化為日常生活場景
- **任務導向教學**：每週設定一個可達成的微小任務（Small Win）
- **即時回饋**：利用即時報表讓學生看到自己操作的結果
