from typing import Optional

from abc import ABC

from models.general.db_session_manager import DBSessionManager


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
        except Exception as e:
            print(e) #  actually we should log it somewhere
            self.db_session.rollback()

    def remove_from_db(self, entity, flush: Optional[bool] = False, commit: Optional[bool] = False):
        try:
            self.db_session.delete(entity)
            if flush:
                self.db_session.flush()
            if commit:
                self.db_session.commit()
        except Exception as e:
            print(e) #  same here, we should log it somewhere
            self.db_session.rollback()
