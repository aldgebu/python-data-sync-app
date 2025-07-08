from typing import Optional

from models.user import UserModel
from models.general.db_session_manager import DBSessionManager

from dals.base_dal import BaseDAL


class UserDAL(BaseDAL):
    def __init__(self):
        self.user_model = UserModel
        self.db_session = DBSessionManager.get_session()

    def find(self, email: Optional[str] = None, get_all: Optional[bool] = False):
        query = self.db_session.query(self.user_model)

        if email:
            query = query.filter_by(email=email)

        if get_all:
            return query.all()
        return query.first()
