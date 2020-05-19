from time import sleep
from functools import wraps


def slow_down(func):
    @wraps(func)
    def inner(*args, **kwargs):
        sleep(1)
        return func(*args, **kwargs)
    return inner
