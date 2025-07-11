from models.general.db import db

from exceptions.general_exceptions import UnKnownProblemException

from utils.logs.log_manager import LogManager


class DBSessionManager:
    session = None

    @classmethod
    def create_session(cls):
        try:
            cls.session = db.session
        except Exception:
            LogManager.get_logger().critical(msg='Error during db session creation', exc_info=True)
            raise UnKnownProblemException()

    @classmethod
    def get_session(cls):
        if cls.session is None:
            cls.create_session()

        return cls.session

    @classmethod
    def commit_session(cls) -> bool:
        if not cls.session:
            return True

        try:
            cls.session.commit()
        except Exception:
            LogManager.get_logger().critical(msg='Error during db session commit', exc_info=True)
            cls.session.rollback()
            return False

        return True

    @classmethod
    def close_and_remove_session(cls):
        try:
            cls.session.close()
        except Exception:
            LogManager.get_logger().error(
                msg='Error during closing session',
                exc_info=True
            )

        cls.session = None
