from functools import wraps


def print_function_information(func):
    @wraps(func)
    def inner(*args, **kwargs):
        arguments = [str(arg) for arg in args]
        kwarguments = [f"{str(key)} = {str(value)}" for key, value in kwargs.items()]
        print(f"Calling: {func.__name__}({', '.join(arguments+kwarguments)})")
        res = func(*args, **kwargs)
        print(f"Return: value_type: {type(res)}, value: {res}")
        return res
    return inner


@print_function_information
def add2(x, y):
    for i in range(1000000):
        pass
    return x+y,x, y


@print_function_information
def add3(x, y, z): return x+y+z


@print_function_information
def add4(): return "hi"


result = add2(1, y=2)
result = add4()
