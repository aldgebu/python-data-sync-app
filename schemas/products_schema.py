from models.products import Products
from schemas.ma import ma


class ProductsSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Products
        load_instance = True
