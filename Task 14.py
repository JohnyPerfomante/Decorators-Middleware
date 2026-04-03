# Побудова middleware-ланцюжка вручну
from functools import wraps

# Middleware 1: Логування запиту
def log_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("LOG: Before request")
        result = func(*args, **kwargs)
        print("LOG: After request")
        return result
    return wrapper

# Middleware 2: Авторизація
def authorize(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("authenticated", False):
            return "Access denied"
        return func(user, *args, **kwargs)
    return wrapper

# Middleware 3: Обробка помилок
def handle_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"An error occurred: {e}"
    return wrapper

# Основна функція
def handle_request(user):
    if user.get("name") == "ErrorUser":
        raise ValueError("Something went wrong")
    return f"Request handled for {user['name']}"

# Побудова ланцюжка вручну
handle_request = log_request(authorize(handle_errors(handle_request)))

user_auth = {"name": "Artem", "authenticated": True}
user_noauth = {"name": "Ivan", "authenticated": False}
user_error = {"name": "ErrorUser", "authenticated": True}

# Виклики
print(handle_request(user_auth))     # Має пройти весь ланцюжок
print("-----")
print(handle_request(user_noauth))   # Заблоковано authorize
print("-----")
print(handle_request(user_error))    # Зловить handle_errors