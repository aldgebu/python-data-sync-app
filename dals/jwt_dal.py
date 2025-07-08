import datetime

from typing import Optional
from sqlalchemy import and_

from models.jwt.jwt_type_enum import JWTTypeEnum
from models.jwt.jwt_blocklist import JWTBlocklist
from models.general.db_session_manager import DBSessionManager

from dals.base_dal import BaseDAL


class TokenDAL(BaseDAL):
    def __init__(self):
        self.jwt_blocklist_model = JWTBlocklist
        self.db_session = DBSessionManager.get_session()

    def create_blocklisted_token(self, jti: str, token_type: JWTTypeEnum, save_to_db: Optional[bool] = True):
        token = self.jwt_blocklist_model(jti=jti, token_type=token_type)

        if save_to_db:
            self.save_to_db(token)
        return token

    def is_blocklisted(self, jti) -> bool:
        token = self.db_session.query(self.jwt_blocklist_model).filter_by(jti=jti).first()
        return token is not None

    def clean_blocklist(self):
        utcnow = datetime.datetime.now(datetime.UTC)
        self.db_session.query(self.jwt_blocklist_model).filter(
            and_(self.jwt_blocklist_model.token_type == JWTTypeEnum.ACCESS,
                 self.jwt_blocklist_model.valid_until < utcnow)
            ).delete()
