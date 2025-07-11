from functools import wraps

from utils.logs.log_manager import LogManager


def retry(attempts: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, attempts + 1):
                try:
                    LogManager.get_logger().debug(f'Attempt #{i} for function "{func.__name__}"')
                    response = func(*args, **kwargs)
                    if response.status_code == 200:
                        LogManager.get_logger().info(f'Successful attempt #{i} for function "{func.__name__}"')
                        break
                    else:
                        LogManager.get_logger().warning(
                            f'Attempt #{i} for function "{func.__name__}" failed with status code: {response.status_code}'
                        )
                except Exception as e:
                    LogManager.get_logger().error(
                        f'Exception during attempt #{i} for function "{func.__name__}": {e}',
                        exc_info=True
                    )
            else:
                LogManager.get_logger().error(f'All {attempts} attempts failed for function "{func.__name__}"')
        return wrapper
    return decorator
