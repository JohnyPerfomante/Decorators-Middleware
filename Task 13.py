# Комбінування декораторів
import time
from functools import wraps

# Декоратори
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.6f} sec")
        return result
    return wrapper

def positive_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                return "Error: all numeric arguments must be positive"
        for value in kwargs.values():
            if isinstance(value, (int, float)) and value <= 0:
                return "Error: all numeric arguments must be positive"
        return func(*args, **kwargs)
    return wrapper

# Функція з комбінованими декораторами
@logger
@timer
@positive_only
def process_data(x):
    """Подвоює значення x"""
    return x * 2

# Тестування
print(process_data(5))   # Позитивний аргумент
print(process_data(-3))  # Негативний аргумент

# Декоратори накладаються знизу вверх у синтаксисі @:logger - зовнішній, timer - середній, positive_only - внутрішній.

# Як змінюється поведінка: positive_only - перехоплює аргументи - блокує негативні значення, timer - вимірює час виконання оригінальної функції, logger - логування імені функції та результату.

# Результат декорації — комбіноване виконання: спершу перевірка аргументів - вимір часу - логування.