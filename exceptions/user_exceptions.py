from flask import Flask
from marshmallow import ValidationError


class EmailAlreadyInUseException(ValidationError):
    def __init__(self):
        super().__init__("Email Already in Use")


def user_exceptions(app: Flask):
    @app.errorhandler(EmailAlreadyInUseException)
    def handle_email_already_in_use(error):
        return {'message': error.messages}, 400
