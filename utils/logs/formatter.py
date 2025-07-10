import logging
from logging import LogRecord

from flask import request, has_request_context
from flask_jwt_extended import get_current_user


class LogFormatter(logging.Formatter):
    def format(self, record: LogRecord) -> str:
        if has_request_context():
            try:
                record.user_id = str(get_current_user().id)
            except:
                record.user_id = "Guest"

            record.ip = request.headers.get('X-Forwarded-for', request.remote_addr)
        else:
            record.user_id = "Guest"
            record.ip = 'No-Ip'

        return super().format(record)
