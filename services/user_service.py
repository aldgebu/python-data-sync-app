from flask_jwt_extended import create_access_token, create_refresh_token, decode_token

from models.jwt.jwt_type_enum import JWTTypeEnum

from dals.jwt_dal import TokenDAL
from dals.user_dal import UserDAL

from schemas.user.user_login_schema import UserLoginSchema
from schemas.user.user_creation_schema import UserCreationSchema

from exceptions.general_exceptions import RefreshTokenException
from exceptions.user_exceptions import EmailAlreadyInUseException, SuchUserNotFoundException


class UserService:
    def __init__(self):
        self.user_dal = UserDAL()
        self.token_dal = TokenDAL()

        self.user_login_schema = UserLoginSchema()
        self.user_creation_schema = UserCreationSchema()

    def create(self, data: dict):
        user = self.user_creation_schema.load(data)
        if self.user_dal.find(email=user.email) is not None:
            raise EmailAlreadyInUseException()

        self.user_dal.save_to_db(user, flush=True)
        return {'message': 'user created successfully!',
                'user': self.user_creation_schema.dump(user)}

    def login(self, data: dict):
        email, password = self.user_login_schema.load(data)

        user = self.user_dal.find(email=email)
        if user is None or not self.user_dal.verify_password(user_obj=user, password=password):
            raise SuchUserNotFoundException()

        return {
            "access_token": create_access_token(identity=user, fresh=True),
            "refresh_token": create_refresh_token(identity=user)
        }

    def logout(self, jwt: dict, data: dict):
        try:
            decoded_token = decode_token(data.get('refresh_token'))
            jti = decoded_token['jti']
            if self.token_dal.is_blocklisted(jti=jti):
                raise Exception
            refresh_token = self.token_dal.create_blocklisted_token(jti=jti, token_type=JWTTypeEnum.REFRESH)
        except:
            raise RefreshTokenException()

        jti = jwt['jti']
        access_token = self.token_dal.create_blocklisted_token(jti=jti, token_type=JWTTypeEnum.ACCESS)
        self.token_dal.save_to_db(access_token, flush=True)
        self.token_dal.save_to_db(refresh_token, flush=True) # Update access token
        return {"message": "Logout successfully!"}
