import bcrypt

from typing import Optional

from models.user import UserModel
from models.general.db_session_manager import DBSessionManager

from dals.base_dal import BaseDAL


class UserDAL(BaseDAL):
    def __init__(self):
        self.user_model = UserModel
        super().__init__()

    def find(self, user_id: Optional[int] = None, email: Optional[str] = None, get_all: Optional[bool] = False):
        query = self.db_session.query(self.user_model)

        if user_id:
            query = query.filter_by(id=user_id)
        if email:
            query = query.filter_by(email=email)

        if get_all:
            return query.all()
        return query.first()

    @classmethod
    def verify_password(cls, user_obj: UserModel, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), user_obj.password.encode('utf-8'))
