from models.products import Products
from schemas.ma import ma


class ProductsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Products
        transient = True
        load_instance = True
