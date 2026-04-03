# Проста middleware-обгортка
def middleware(func):
    def wrapper(*args, **kwargs):
        print("Before request")
        result = func(*args, **kwargs)
        print("After request")
        return result
    return wrapper


# Приклад звичайної функції
def handle_request():
    return "OK"


# Обгортка вручну
handle_request = middleware(handle_request)


# Виклик
response = handle_request()
print(f"Response: {response}")

# Це middleware-поведінка, бо Before request - дія до основної функції, After request → дія після основної функції. Фактично перехоплюється виклик і додається додаткова поведінка, не змінюючи саму функцію.