# Декоратор як чиста трансформація поведінки
from functools import wraps

def to_uppercase_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper

@to_uppercase_result
def greet(name):
    return f"Hello, {name}"

@to_uppercase_result
def add(a, b):
    return a + b  # Не рядок, результат не змінюється

# Тестування
print(greet("Artem"))   # очікувано: HELLO, ARTEM
print(add(3, 5))        # очікувано: 8