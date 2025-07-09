from typing import List, Optional

from models.products import Products
from models.general.db_session_manager import DBSessionManager

from dals.base_dal import BaseDAL


class ProductsDAL(BaseDAL):
    def __init__(self):
        self.db_session = DBSessionManager.get_session()

    def update(self, products: List[Products]):
        for product in products:
            self.save_to_db(product, merge=True)

    def find(self, is_synced: Optional[bool] = None) -> List[Products]:
        query = self.db_session.query(Products)

        if is_synced is not None:
            query = query.filter_by(is_synced=is_synced)

        return query.all()

    def make_synchronized(self, products: List[Products]):
        for product in products:
            product.is_synced = True
            self.save_to_db(product)

        DBSessionManager.commit_session()
