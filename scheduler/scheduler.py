import atexit
from flask import Flask

from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.schedulers.background import BackgroundScheduler

from config import Config

def sync_data(app: Flask):
    pass


def init_scheduler(app: Flask):
    scheduler = BackgroundScheduler()

    scheduler.add_job(func=sync_data, args=[app], trigger=IntervalTrigger(seconds=Config.SYNC_INTERVAL_MINUTES))

    scheduler.start()

    # Define a function to shut down the scheduler
    shutdown_scheduler = lambda: scheduler.shutdown()

    # Register the shutdown function with atexit
    atexit.register(shutdown_scheduler)
