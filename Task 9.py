# Параметризований логер
from functools import wraps

def log_with_prefix(prefix):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{prefix}] Calling function: {func.__name__}")
            
            result = func(*args, **kwargs)
            
            print(f"[{prefix}] Result: {result}")
            return result
        return wrapper
    return decorator


# Тестові функції з різними префіксами
@log_with_prefix("INFO")
def run_task():
    return "Done"


@log_with_prefix("WARNING")
def divide(a, b):
    return a / b if b != 0 else "Division by zero"


@log_with_prefix("ERROR")
def process(data):
    return data.upper()


# Тестування
run_task()
print("-----")

divide(10, 2)
print("-----")

divide(5, 0)
print("-----")

process("hello")