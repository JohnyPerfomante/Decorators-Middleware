# Декоратор збереження метаданих

# Декоратор без functools.wraps
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@simple_decorator
def my_function():
    """This is my function"""
    return "OK"


# Перевірка
print(my_function.__name__)
print(my_function.__doc__)

# Виправлення через functools.wraps
from functools import wraps


def fixed_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@fixed_decorator
def my_function():
    """This is my function"""
    return "OK"


# Перевірка
print(my_function.__name__)
print(my_function.__doc__)

# Без wraps неможливо зрозуміти, яка функція реально викликається, без wraps показує wrapper замість реальної функції.