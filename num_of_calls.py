from functools import wraps


def count_num_of_calls(func):
    num_of_calls = 0
    @wraps(func)
    def inner(*args, **kwargs):
        nonlocal num_of_calls
        num_of_calls += 1
        res = func(*args, **kwargs)
        print(f"num_of_calls: {num_of_calls}")
        return res
    return inner


@count_num_of_calls
def add2(x, y):
    for i in range(1000000):
        pass
    return x+y


@count_num_of_calls
def add3(x, y, z): return x+y+z


print(add2(1, 3))
print(add3(1, 3, 1))
print(add2(1, 3))
print(add3(1, 3, 5))
print(add3(1, 3, 6))
