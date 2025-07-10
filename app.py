import logging

from flask import Flask
from flask_migrate import Migrate

from jwt_setup import jwt
from app_setup import app_setup
from config import Config, ConfigManager

from scheduler.scheduler import init_scheduler

from models.general.db import db

from schemas.ma import ma

from blueprint_loader import load_blueprints

from utils.logs.log_manager import LogManager
from utils.logs.HandlerManager import HandlerManager


migrate = Migrate()


def init_extensions(flask_app: Flask):
    ma.init_app(flask_app)
    migrate.init_app(flask_app, db)
    db.init_app(flask_app)
    jwt.init_app(flask_app)

    init_scheduler(app=flask_app)


def create_app() -> Flask:
    flask_app = Flask(__name__)
    flask_app.config.from_object(ConfigManager.get_config())

    HandlerManager.initialize_file_handler(level=logging.INFO) # First Make file to write logs
    LogManager.remove_all_handlers(app=flask_app) # Remove all default handlers
    LogManager.initialize_app_logger(app_logger=flask_app.logger) # make app logger main logger
    LogManager.configure_logging(level=logging.DEBUG, logger=LogManager.get_logger()) # setting logging level

    init_extensions(flask_app=flask_app)
    app_setup(app=flask_app)
    load_blueprints(app=flask_app)

    return flask_app


if __name__ == '__main__':
    app = create_app()
    app.run(host=Config.APP_HOST, port=Config.APP_PORT_DOCKER)
