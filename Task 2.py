# Ручне обгортання функції
def greet(name):
    return f"Hello, {name}"


def wrapper(func):
    def inner(name):
        print("Before function call")
        result = func(name)
        print("After function call")
        return result
    return inner


# Ручне обгортання
wrapped_greet = wrapper(greet)

# Виклик нової функції
result = wrapped_greet("John")
print(result)

# Wrapper приймає іншу функцію (func), створює нову функцію (inner), додає додаткову поведінку, повертає цю нову функцію.

# Поведінка оригінальної функції: оригінальна логіка не змінюється, але навколо неї додається додатковий контекст виконання.