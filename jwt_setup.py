from flask_jwt_extended import JWTManager

from dals.jwt_dal import TokenDAL
from dals.user_dal import UserDAL

jwt = JWTManager()


@jwt.token_in_blocklist_loader
def check_if_token_revoked(_jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    token_dal = TokenDAL()

    is_blocklisted = token_dal.is_blocklisted(jti)
    return is_blocklisted


@jwt.user_identity_loader
def user_identity_loader(user):
    return str(user.id)


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    user_id = jwt_data['sub']
    user_dal = UserDAL()

    return user_dal.find(user_id=user_id)


@jwt.unauthorized_loader
def unauthorized_callback(reason):
    return {"msg": reason}, 401


@jwt.invalid_token_loader
def invalid_token_callback(reason):
    return {"msg": reason}, 401
