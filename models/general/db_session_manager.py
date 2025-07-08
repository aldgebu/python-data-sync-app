from models.general.db import db


class DBSessionManager:
    session = None

    @classmethod
    def create_session(cls):
        try:
            cls.session = db.session
        except Exception as e:
            # log exception
            pass

    @classmethod
    def get_session(cls):
        if cls.session is None:
            cls.create_session()

        return cls.session
