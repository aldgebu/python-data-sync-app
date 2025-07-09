from functools import wraps


def retry(attempts: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(attempts):
                print(i)
                try:
                    response = func(*args, **kwargs)
                    if response.status_code == 200:
                        break
                except Exception as e:
                    # log exception
                    pass
            else:
                # log exception
                pass
        return wrapper
    return decorator
