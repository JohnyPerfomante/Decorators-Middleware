# Middleware для обробки помилок
def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"An error occurred: {e}"
    return wrapper

# Функція для тесту
@handle_errors
def divide(a, b):
    return a / b

# Перевірка
print(divide(10, 2))  # 5.0
print(divide(10, 0))  # An error occurred: division by zero