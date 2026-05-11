#!/bin/bash
# 市場輿情分析儀表板啟動腳本
# 用法：bash run.sh
cd "$(dirname "$0")"
streamlit run app.py
