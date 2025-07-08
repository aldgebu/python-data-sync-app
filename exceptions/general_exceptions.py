from flask import Flask
from marshmallow import ValidationError
from werkzeug.exceptions import InternalServerError


class UnKnownProblemException(InternalServerError):
    def __init__(self):
        super().__init__("Unknown Problem")


class RefreshTokenException(ValidationError):
    def __init__(self):
        super().__init__("Refresh Token expired")


def general_exceptions(app: Flask):
    # we should log somewhere that this error happened but for demo project it would be enough I think
    @app.errorhandler(InternalServerError)
    def handle_internal_server_error(error):
        return {"message": "Internal server error"}, 500

    @app.errorhandler(UnKnownProblemException)
    def handle_un_know_problem(error):
        return {"message": error.description}, 500

    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        return {"message": error.messages}, 400

    @app.errorhandler(RefreshTokenException)
    def handle_refresh_token_exception(error):
        return {"message": error.messages}, 400
