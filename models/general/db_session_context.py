from models.general.db_session_manager import DBSessionManager


class DBSessionContext:
    def __enter__(self):
        DBSessionManager.get_session() # This will create new session during requests

    def __exit__(self, exc_type, exc_val, exc_tb):
        DBSessionManager.commit_session()
        DBSessionManager.close_and_remove_session()
