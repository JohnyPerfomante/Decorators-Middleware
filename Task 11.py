# Middleware для авторизації
def require_auth(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("authenticated", False):
            return "Access denied"
        return func(user, *args, **kwargs)
    return wrapper

# Функція дашборду
@require_auth
def dashboard(user):
    return f"Welcome, {user['name']}"

user_auth = {"name": "Artem", "authenticated": True}
user_noauth = {"name": "Ivan", "authenticated": False}

# Перевірка
print(dashboard(user_auth))     # Welcome, Artem
print(dashboard(user_noauth))   # Access denied