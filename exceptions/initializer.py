from flask import Flask

from exceptions.user_exceptions import user_exceptions
from exceptions.general_exceptions import general_exceptions


def initialize_exceptions(app: Flask):
    general_exceptions(app=app)
    user_exceptions(app=app)
