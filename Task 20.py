# Functional Request Processing Engine
import time
from functools import wraps

# Middleware 1: Logger
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"LOG: Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"LOG: Result = {result}")
        return result
    return wrapper

# Middleware 2: require_auth
def require_auth(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("authenticated", False):
            return "Access denied"
        return func(user, *args, **kwargs)
    return wrapper

# Middleware 3: validate_positive
def validate_positive(func):
    @wraps(func)
    def wrapper(user, value, *args, **kwargs):
        if value < 0:
            return "Error: value must be positive"
        return func(user, value, *args, **kwargs)
    return wrapper

# Middleware 4: handle_errors
def handle_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"An error occurred: {e}"
    return wrapper

# Middleware 5: timer
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start:.6f} seconds")
        return result
    return wrapper

# Базова функція обробки запиту
def handle_request(user, value):
    if value == 999:  # Для демонстрації помилки
        raise ValueError("Simulated exception")
    return f"Processed value: {value}"

# Middleware-ланцюжок. Порядок: handle_errors - timer - require_auth - validate_positive - logger
handle_request = handle_errors(timer(require_auth(validate_positive(logger(handle_request)))))

# Тестові сценарії
user_auth = {"name": "Artem", "authenticated": True}
user_noauth = {"name": "Ivan", "authenticated": False}

print("Сценарій 1: Авторизоване, позитивне значення")
print(handle_request(user_auth, 42))

print("\nСценарій 2: Неавторизований користувач")
print(handle_request(user_noauth, 42))

print("\nСценарій 3: Від'ємне значення")
print(handle_request(user_auth, -5))

print("\nСценарій 4: Помилка всередині функції")
print(handle_request(user_auth, 999))