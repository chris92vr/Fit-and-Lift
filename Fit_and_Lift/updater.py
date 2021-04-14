from apscheduler.schedulers.background import BackgroundScheduler
from .deleted_expired_subscriptions import cleanup_expired_subscriptions


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(cleanup_expired_subscriptions, 'interval', seconds=10)
    scheduler.start()