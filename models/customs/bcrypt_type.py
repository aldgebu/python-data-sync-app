import bcrypt
from sqlalchemy import TypeDecorator, VARCHAR


class BcryptType(TypeDecorator):
    impl = VARCHAR

    def process_bind_param(self, value, dialect):
        if value is None:
            return value

        return bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def process_result_value(self, value, dialect):
        return value
