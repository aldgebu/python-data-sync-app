from werkzeug.datastructures import FileStorage

from utils.file_manager import FileManager
from utils.data_synchronizer import DataSynchronizer

from dals.products_dal import ProductsDAL

from schemas.products.products_schema import ProductsSchema
from schemas.products.products_file_schema import ProductsFileSchema


class ProductsService:
    def __init__(self):
        self.file_manager = FileManager
        self.data_synchronizer = DataSynchronizer()

        self.products_dal = ProductsDAL()

        self.products_schema = ProductsSchema()
        self.products_file_schema = ProductsFileSchema()

    def update(self, file: FileStorage):
        self.products_file_schema.load({'file_name': file.filename})

        products = []
        for row in self.file_manager.get_rows(file):
            products.append(self.products_schema.load(row))

        self.products_dal.update(products=products)
        return {"message": "updated successfully"}

    def sync_products(self):
        unsynced_products = self.products_dal.find(is_synced=False)

        for product in unsynced_products:
            self.data_synchronizer.send_data(self.products_schema.dump(product))
            self.products_dal.make_synchronized(product)
