from flask import request
from flask.views import MethodView
from flask.blueprints import Blueprint

from services.user_service import UserService


user_bp = Blueprint('user', __name__, url_prefix='/user')


class UserRegistrationView(MethodView):
    def __init__(self):
        self.user_service = UserService()

    def post(self):
        data = request.get_json()

        return self.user_service.create(data), 200


user_bp.add_url_rule('/create', view_func=UserRegistrationView.as_view('user_register'))
