import datetime

from models.general.db import db


class Products(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    is_synced = db.Column(db.Boolean, nullable=False, default=False)
    last_update = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.datetime.now(datetime.UTC),
        onupdate=datetime.datetime.now(datetime.UTC),
    )
