# Декоратор для *args і **kwargs
def debug_args(func):
    def wrapper(*args, **kwargs):
        print(f"Function: {func.__name__}")

        print(f"Positional args: {args}")

        print(f"Keyword args: {kwargs}")

        result = func(*args, **kwargs)

        print(f"Result: {result}")
        print("-----")
        return result
    return wrapper


# Функція без аргументів
@debug_args
def say_hello():
    return "Hello!"


# Функція з позиційними аргументами
@debug_args
def add(a, b):
    return a + b


# Функція з іменованими аргументами
@debug_args
def greet(name, prefix="Hello"):
    return f"{prefix}, {name}"


# Тести
say_hello()

add(3, 5)

greet("Artem")

greet("Ivan", prefix="Hi")