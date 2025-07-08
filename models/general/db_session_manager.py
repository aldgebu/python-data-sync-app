from models.general.db import db

from exceptions.general_exceptions import UnKnownProblemException


class DBSessionManager:
    session = None

    @classmethod
    def create_session(cls):
        try:
            cls.session = db.session
        except Exception as e:
            # log exception
            raise UnKnownProblemException()

    @classmethod
    def get_session(cls):
        if cls.session is None:
            cls.create_session()

        return cls.session
