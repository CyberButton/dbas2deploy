from apscheduler.schedulers.background import BackgroundScheduler
from django.apps import AppConfig

from dbas2.views import ping


class Dbas2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dbas2'

    def ready(self):
        scheduler = BackgroundScheduler()
        scheduler.add_job(ping, 'interval', minutes=13)
        scheduler.start()
