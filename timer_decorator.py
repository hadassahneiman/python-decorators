from time import time
from functools import wraps


def timer_decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        print(f"Done in: {time() - start} seconds.")
        return res
    return inner


@timer_decorator
def add2(x, y):
    for i in range(1000000):
        pass
    return x+y


@timer_decorator
def add3(x, y, z): return x+y+z


@timer_decorator
def add4(): return "hi"


result = add2(1,2)
print(result)
result = add4()
print(result)
