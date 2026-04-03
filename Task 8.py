# Параметризований декоратор
from functools import wraps


def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)
def say_hi():
    print("Hi")


@repeat(2)
def add(a, b):
    print(a + b)
    return a + b


# Тестування
say_hi()
print("-----")
add(2, 3)

# Додаткова вкладеність потрібна, щоб розділити два етапи: передача параметрів (n), обгортання функції.