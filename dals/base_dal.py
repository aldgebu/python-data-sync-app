from typing import Optional

from abc import ABC

from models.general.db_session_manager import DBSessionManager

from exceptions.general_exceptions import UnKnownProblemException

from utils.logs.log_manager import LogManager


class BaseDAL(ABC):
    def __init__(self):
        self._db_session = None

    @property
    def db_session(self):
        if self._db_session is None:
            self._db_session = DBSessionManager.get_session()

        return self._db_session

    def save_to_db(self,
                   entity,
                   flush: Optional[bool] = False,
                   commit: Optional[bool] = False,
                   merge: Optional[bool] = False):
        try:
            if merge:
                self.db_session.merge(entity)
            else:
                self.db_session.add(entity)

            if flush:
                self.db_session.flush()
            if commit:
                self.db_session.commit()
        except Exception:
            LogManager.get_logger().critical(
            f'Error during {BaseDAL.__name__}.{BaseDAL.save_to_db.__name__} : {entity}, flush={flush}, commit={commit}',
                exc_info=True
            )
            try:
                self.db_session.rollback()
            except Exception:
                LogManager.get_logger().critical(
                    f'Error during {BaseDAL.__name__}.{BaseDAL.save_to_db.__name__} -> rollback : '
                    f'{entity}, flush={flush}, commit={commit}',
                    exc_info=True
                )
            raise UnKnownProblemException()

    def remove_from_db(self, entity, flush: Optional[bool] = False, commit: Optional[bool] = False):
        try:
            self.db_session.delete(entity)
            if flush:
                self.db_session.flush()
            if commit:
                self.db_session.commit()
        except Exception:
            LogManager.get_logger().critical(
                f'Error during {BaseDAL.__name__}.{BaseDAL.remove_from_db.__name__} : '
                f'{entity}, flush={flush}, commit={commit}',
                exc_info=True
            )
            try:
                self.db_session.rollback()
            except Exception:
                LogManager.get_logger().critical(
                    f'Error during {BaseDAL.__name__}.{BaseDAL.remove_from_db.__name__} -> rollback : '
                    f'{entity}, flush={flush}, commit={commit}',
                    exc_info=True
                )
            raise UnKnownProblemException()
