import datetime

from typing import Optional
from sqlalchemy import and_

from models.jwt.jwt_type_enum import JWTTypeEnum
from models.jwt.jwt_blocklist import JWTBlocklist
from models.general.db_session_manager import DBSessionManager

from dals.base_dal import BaseDAL


class TokenDAL(BaseDAL):
    def __init__(self):
        self.JWTBlocklistModel = JWTBlocklist
        self.session = DBSessionManager.get_session()

    def create_blocklisted_token(self, jti: str, token_type: JWTTypeEnum, save_to_db: Optional[bool] = True):
        token = self.JWTBlocklistModel(jti=jti, token_type=token_type)

        if save_to_db:
            self.save_to_db(token)
        return token

    def is_blocklisted(self, jti) -> bool:
        token = self.session.query(self.JWTBlocklistModel).filter_by(jti=jti).first()
        return token is not None

    def clean_blocklist(self):
        utcnow = datetime.datetime.now(datetime.UTC)
        self.session.query(self.JWTBlocklistModel).filter(and_(self.JWTBlocklistModel.token_type == JWTTypeEnum.ACCESS,
                                                               self.JWTBlocklistModel.valid_until < utcnow)
                                                          ).delete()
