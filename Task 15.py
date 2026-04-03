# Rate limiting
from functools import wraps

def limit_calls(n):
    def decorator(func):
        count = 0  # Лічильник викликів зберігається у замиканні

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal count  # Дозволяє змінювати зовнішню змінну
            if count >= n:
                return "Call limit exceeded"
            count += 1
            return func(*args, **kwargs)

        return wrapper
    return decorator

@limit_calls(3)
def ping():
    return "pong"

# Тестування
print(ping())  # 1-й виклик - pong
print(ping())  # 2-й виклик - pong
print(ping())  # 3-й виклик - pong
print(ping())  # 4-й виклик - Call limit exceeded

# Лічильник count знаходиться у замиканні функції wrapper, кожна обгорнута функція має свій власний count.