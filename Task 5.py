# Декоратор перевірки аргументу
def positive_only(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                return "Error: all numeric arguments must be positive"

        for value in kwargs.values():
            if isinstance(value, (int, float)) and value <= 0:
                return "Error: all numeric arguments must be positive"

        return func(*args, **kwargs)
    return wrapper


@positive_only
def multiply(a, b):
    return a * b


@positive_only
def power(base, exp):
    return base ** exp


# Тести
print(multiply(2, 3))      # OK
print(multiply(-2, 3))     # Error
print(power(2, 3))         # OK
print(power(2, -1))        # Error

# Декоратор додає валідацію вхідних даних, функція більше не виконується, якщо аргументи не відповідають умовам.