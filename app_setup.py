from flask import Flask, jsonify

from models.general.db import setup_db
from models.general.db_session_manager import DBSessionManager

from exceptions.initializer import initialize_exceptions


def app_setup(app: Flask):
    with app.app_context():
        setup_db(app)

    initialize_exceptions(app)
