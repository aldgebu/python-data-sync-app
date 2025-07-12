from flask import request
from flask.views import MethodView
from flask.blueprints import Blueprint
from flask_jwt_extended import jwt_required

from services.products_service import ProductsService

from utils.decorators.for_methods.db_session_context import db_session_context


products_bp = Blueprint('products', __name__, url_prefix='/products')


class UploadProductsView(MethodView):
    def __init__(self):
        self.products_service = ProductsService()

    @db_session_context
    @jwt_required()
    def post(self):
        file = request.files['file']

        return self.products_service.update(file=file), 200


products_bp.add_url_rule('/upload', view_func=UploadProductsView.as_view('upload_products_view'))
