import atexit
from flask import Flask

from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.schedulers.background import BackgroundScheduler

from config import Config

from services.products_service import ProductsService


def sync_data(app: Flask):
    with app.app_context():
        products_service = ProductsService()
        products_service.sync_products()


def init_scheduler(app: Flask):
    scheduler = BackgroundScheduler()

    scheduler.add_job(func=sync_data, args=[app], trigger=IntervalTrigger(minutes=Config.SYNC_INTERVAL_MINUTES))

    scheduler.start()

    # Define a function to shut down the scheduler
    shutdown_scheduler = lambda: scheduler.shutdown()

    # Register the shutdown function with atexit
    atexit.register(shutdown_scheduler)
