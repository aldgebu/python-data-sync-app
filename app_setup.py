from flask import Flask

from models.general.db import setup_db


from exceptions.initializer import initialize_exceptions


def app_setup(app: Flask):
    with app.app_context():
        setup_db(app)

    initialize_exceptions(app)
