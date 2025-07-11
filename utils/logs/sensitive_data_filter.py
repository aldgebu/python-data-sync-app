import re
import logging

from config import Config


class SensitiveDataFilter(logging.Filter):
    def __init__(self):
        super().__init__()
        self.sensitive_keywords = Config.SENSITIVE_DATA_LIST

    def filter(self, record: logging.LogRecord) -> bool:
        message = record.msg

        for keyword in self.sensitive_keywords:
            pattern = rf"('{keyword}':\s*['\"])(.*?)(['\"])"
            if re.search(pattern, message):
                message = re.sub(pattern, rf"\1*****\3", message)

        record.msg = message
        return True
