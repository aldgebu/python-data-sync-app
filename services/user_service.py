from dals.user_dal import UserDAL

from schemas.user_schema import UserSchema

from exceptions.user_exceptions import EmailAlreadyInUseException


class UserService:
    def __init__(self):
        self.user_dal = UserDAL()

        self.user_schema = UserSchema()

    def create(self, data: dict):
        user = self.user_schema.load(data)
        print(user.email)
        print(self.user_dal.find(email=user.email))
        if self.user_dal.find(email=user.email) is not None:
            raise EmailAlreadyInUseException()

        self.user_dal.save_to_db(user, commit=True)
        return {'message': 'user created successfully!',
                'user': self.user_schema.dump(user)}
