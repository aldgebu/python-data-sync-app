from werkzeug.datastructures import FileStorage

from dals.products_dal import ProductDAL
from utils.file_manager import FileManager


class ProductsService:
    def __init__(self):
        self.file_manager = FileManager
        self.products_dal = ProductDAL()

    def update(self, file: FileStorage):
        products = []
        for row in self.file_manager.get_rows(file):
            print(row)

        return {"message": "updated successfully"}
