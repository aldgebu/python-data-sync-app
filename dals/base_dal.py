from typing import Optional

from abc import ABC

from models.general.db_session_manager import DBSessionManager


class BaseDAL(ABC):
    @classmethod
    def save_to_db(cls, entity, flush: Optional[bool] = False, commit: Optional[bool] = False):
        db_session = DBSessionManager.get_session()

        try:
            db_session.add(entity)
            if flush:
                db_session.flush()
            if commit:
                db_session.commit()
        except Exception as e:
            print(e) #  actually we should log it somewhere
            db_session.rollback()

    @classmethod
    def remove_from_db(cls, entity, flush: Optional[bool] = False, commit: Optional[bool] = False):
        db_session = DBSessionManager.get_session()

        try:
            db_session.delete(entity)
            if flush:
                db_session.flush()
            if commit:
                db_session.commit()
        except Exception as e:
            print(e) #  same here, we should log it somewhere
            db_session.rollback()
