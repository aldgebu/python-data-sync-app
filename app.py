from flask import Flask
from flask_migrate import Migrate

from jwt_setup import jwt
from app_setup import app_setup
from config import Config, ConfigManager

from scheduler.scheduler import init_scheduler

from models.general.db import db

from schemas.ma import ma

from blueprint_loader import load_blueprints


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

    init_extensions(flask_app=flask_app)
    app_setup(app=flask_app)
    load_blueprints(app=flask_app)

    return flask_app


if __name__ == '__main__':
    app = create_app()
    app.run(host=Config.APP_HOST, port=Config.APP_PORT_DOCKER)
