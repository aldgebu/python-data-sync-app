from typing import List

from models.products import Products
from models.general.db_session_manager import DBSessionManager

from dals.base_dal import BaseDAL


class ProductDAL(BaseDAL):
    def __init__(self):
        self.db_session = DBSessionManager.get_session()

    def update(self, products: List[Products]):
        for product in products:
            self.save_to_db(product, merge=True)

        DBSessionManager.commit_session() # Better and faster to commit everything together
