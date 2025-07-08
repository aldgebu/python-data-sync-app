from schemas.ma import ma
from marshmallow import fields, post_load


class UserLoginSchema(ma.Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)

    @post_load
    def post_load_processing(self, data, **kwargs):
        return data['email'], data['password']
