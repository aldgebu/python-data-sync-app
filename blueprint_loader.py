from flask import Flask

from blueprints.user_bp import user_bp


def load_blueprints(app: Flask):
    app.register_blueprint(user_bp)
