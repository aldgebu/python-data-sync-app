import logging

from config import Config
from utils.logs.formatter import LogFormatter
from utils.logs.log_manager import LogManager
from utils.logs.sensitive_data_filter import SensitiveDataFilter


class HandlerManager:
    @classmethod
    def initialize_handler(cls,
                           handler: logging.Handler,
                           formatter: logging.Formatter,
                           log_filter: logging.Filter,
                           level: int,
                           remove_others: bool):
        handler.setLevel(level)
        handler.addFilter(log_filter)
        handler.setFormatter(formatter)

        if remove_others:
            LogManager.clear_logger_handlers(LogManager.get_logger())
        LogManager.add_handler(handler)

    @classmethod
    def initialize_file_handler(cls, level: int, remove_others: bool = True):
        file_handler = logging.FileHandler(Config.LOG_FILE_NAME)
        formatter = LogFormatter(fmt=Config.LOG_FORMAT) # TODO: check if work without getting format
        log_filter = SensitiveDataFilter()

        cls.initialize_handler(handler=file_handler, formatter=formatter,
                               log_filter=log_filter, level=level, remove_others=remove_others)
