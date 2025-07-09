from werkzeug.datastructures import FileStorage

from utils.file_manager import FileManager

from dals.products_dal import ProductsDAL

from schemas.products_schema import ProductsSchema


class ProductsService:
    def __init__(self):
        self.file_manager = FileManager
        self.products_dal = ProductsDAL()

        self.products_schema = ProductsSchema()

    def update(self, file: FileStorage):
        products = []
        for row in self.file_manager.get_rows(file):
            products.append(self.products_schema.load(row))

        self.products_dal.update(products=products)
        return {"message": "updated successfully"}
