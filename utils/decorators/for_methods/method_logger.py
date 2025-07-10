from functools import wraps

from utils.logs.log_manager import LogManager


def method_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        LogManager.get_logger().info(
            f"Method called: {func.__module__}.{func.__qualname__}, args: {args}, kwargs: {kwargs}"
        )

        return func(*args, **kwargs)
    return wrapper
