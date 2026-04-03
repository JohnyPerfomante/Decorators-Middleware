# Декоратор логування
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper


@logger
def square(x):
    return x * x


@logger
def add(a, b):
    return a + b


@logger
def greet(name):
    return f"Hello, {name}"


# Перевірка
square(5)
print("-----")

add(3, 7)
print("-----")

greet("Artem")