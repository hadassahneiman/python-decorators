from functools import wraps


def cache_decorator(func):
    cache = {}
    @wraps(func)
    def inner(*args, **kwargs):
        nonlocal cache
        if not cache.get(args[0]):
            res = func(*args, **kwargs)
            cache[args[0]] = res
            return res
        return cache[args[0]]
    return inner


@cache_decorator
def fibonacci(n):
    return fibonacci(n-1) + fibonacci(n-2) if n > 1 else n


print(fibonacci(6))
