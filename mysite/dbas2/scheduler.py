from apscheduler.schedulers.background import BackgroundScheduler
from dbas2.views import ping


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(ping, 'interval', minutes=13)
    scheduler.start()
