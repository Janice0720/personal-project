import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from config import SCHEDULE_HOUR, SCHEDULE_MINUTE

logger = logging.getLogger(__name__)


def run_daily_analysis():
    """排程執行函式：收集資料 → 分析 → 寫入快取。"""
    from collector import collect_all
    from analyzer import run_analysis, save_cache

    logger.info("=== 每日市場分析開始 ===")
    try:
        raw_data = collect_all()
        result = run_analysis(raw_data)
        save_cache(result)
        logger.info(f"=== 分析完成，關鍵字：{result['top_keywords']} ===")
    except Exception as e:
        logger.error(f"每日分析失敗：{e}")


def create_scheduler() -> BackgroundScheduler:
    """建立並設定排程器，回傳尚未啟動的 scheduler 實例。"""
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        run_daily_analysis,
        trigger=CronTrigger(hour=SCHEDULE_HOUR, minute=SCHEDULE_MINUTE),
        id="daily_analysis",
        name="每日市場分析",
        replace_existing=True,
    )
    return scheduler
