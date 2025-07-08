from flask import Flask

from exceptions.general_exceptions import general_exceptions


def initialize_exceptions(app: Flask):
    general_exceptions(app=app)
