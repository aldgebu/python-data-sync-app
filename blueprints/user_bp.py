from flask import request
from flask.views import MethodView
from flask.blueprints import Blueprint
from flask_jwt_extended import jwt_required, get_jwt

from services.user_service import UserService


user_bp = Blueprint('user', __name__, url_prefix='/user')


class UserRegistrationView(MethodView):
    def __init__(self):
        self.user_service = UserService()

    def post(self):
        data = request.get_json()

        return self.user_service.create(data), 201


class UserAuthView(MethodView):
    def __init__(self):
        self.user_service = UserService()

    def post(self):
        data = request.get_json()

        return self.user_service.login(data=data), 201

    @jwt_required()
    def delete(self):
        jwt = get_jwt()
        data = request.get_json()

        return self.user_service.logout(jwt=jwt, data=data), 200


user_bp.add_url_rule('/auth', view_func=UserAuthView.as_view('user_login'))
user_bp.add_url_rule('/create', view_func=UserRegistrationView.as_view('user_register'))
