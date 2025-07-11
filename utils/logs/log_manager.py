import logging

from flask import Flask
from logging import Logger
from typing import Optional


class LogManager:
    logger = logging.getLogger()

    @classmethod
    def configure_logging(cls, level: int, logger: Optional[Logger] = None):
        if logger is not None:
            logger.setLevel(level=level)
            return

        logging.getLogger('root').setLevel(level=level)

    @classmethod
    def initialize_app_logger(cls, app_logger: Logger):
        cls.logger = app_logger

    @classmethod
    def get_logger(cls, name: Optional[str] = None) -> Logger:
        if name is not None:
            return logging.getLogger(name)
        return cls.logger

    @classmethod
    def add_handler(cls, handler: logging.Handler):
        cls.logger.addHandler(handler)

    @classmethod
    def clear_logger_handlers(cls, logger: Logger):
        try:
            logger.handlers.clear()
        except:
            pass


    @classmethod
    def remove_all_handlers(cls, app: Flask):
        cls.clear_logger_handlers(app.logger)
        cls.clear_logger_handlers(cls.get_logger('werkzeug'))

        for logger in logging.root.manager.loggerDict.values():
            cls.clear_logger_handlers(logger=logger)
