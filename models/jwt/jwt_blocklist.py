import datetime

from config import Config

from models.general.db import db
from models.jwt.jwt_type_enum import JWTTypeEnum


class JWTBlocklist(db.Model):
    __tablename__ = 'jwt_blocklist'

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(250), nullable=False)
    token_type = db.Column(db.Enum(JWTTypeEnum, name='jwt_type_enum'), nullable=False)
    valid_until = db.Column(db.DateTime,
                            default=datetime.datetime.now(datetime.UTC) + Config.JWT_REFRESH_TOKEN_LIFETIME)

    def __init__(self, jti: str, token_type: JWTTypeEnum):
        self.jti = jti
        self.token_type = token_type
