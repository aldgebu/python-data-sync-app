from functools import wraps

from models.general.db_session_context import DBSessionContext


def db_session_context(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with DBSessionContext():
            return func(*args, **kwargs)
    return wrapper
