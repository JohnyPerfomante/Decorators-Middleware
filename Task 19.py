# Compose для декораторів
from functools import wraps

def decorator_a(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator A: before")
        result = func(*args, **kwargs)
        print("Decorator A: after")
        return result
    return wrapper

def decorator_b(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator B: before")
        result = func(*args, **kwargs)
        print("Decorator B: after")
        return result
    return wrapper

# Функція композиції декораторів
def compose_decorators(d1, d2):
    def composed(func):
        return d1(d2(func))
    return composed

@compose_decorators(decorator_a, decorator_b)
def say_hello():
    print("Hello!")

# Тестування
say_hello()