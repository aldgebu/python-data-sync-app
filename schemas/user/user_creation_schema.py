import re
from marshmallow import validates, ValidationError

from schemas.ma import ma

from models.user import UserModel


class UserCreationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        dump_only = ('id',)
        load_only = ('password',)

    @validates('password')
    def password_validator(self, password, **kwargs):
        if re.match(".*[a-z]", password) is None:
            raise ValidationError('Should contain at least one lower character')
        if re.match(".*[0-9]", password) is None:
            raise ValidationError('Should contain at least one number')
        if len(password) < 8:
            raise ValidationError('Should be at least 8 characters')

        if re.fullmatch("[a-zA-Z0-9!@#$%^&*_.,?]*", password) is None:
            raise ValidationError("Password contains invalid characters")
