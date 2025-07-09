from flask import Flask

from blueprints.user_bp import user_bp
from blueprints.swagger_bp import SWAGGER_URL, swagger_bp


def load_blueprints(app: Flask):
    app.register_blueprint(user_bp)
    app.register_blueprint(swagger_bp, url_prefix=SWAGGER_URL)
