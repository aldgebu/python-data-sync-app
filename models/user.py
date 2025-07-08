from models.general.db import db
from models.customs.bcrypt_type import BcryptType


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(128), nullable=False)

    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(BcryptType(), nullable=False)
