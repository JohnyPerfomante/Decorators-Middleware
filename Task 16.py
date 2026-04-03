# Кешування результатів
from functools import wraps

def simple_cache(func):
    cache = {}  # Для зберігання результатів

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result  # Збереження результату
        return result

    return wrapper

@simple_cache
def square(x):
    print("Calculating...")
    return x * x

# Тестування
print(square(5))  # Перший виклик - "Calculating..." + 25
print(square(5))  # Другий виклик - 25, "Calculating..." не друкується
print(square(6))  # Перший виклик для 6 - "Calculating..." + 36
print(square(6))  # Другий виклик для 6 - 36, без друку