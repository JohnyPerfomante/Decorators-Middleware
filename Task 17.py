# Middleware для валідації даних
from functools import wraps

def validate_name(func):
    @wraps(func)
    def wrapper(data, *args, **kwargs):
        if "name" not in data:
            return "Error: 'name' key is missing"
        if not data["name"]:
            return "Error: 'name' cannot be empty"
        return func(data, *args, **kwargs)
    return wrapper

@validate_name
def create_user(data):
    return f"User {data['name']} created"

valid_data = {"name": "Artem"}
missing_name = {"username": "Ivan"}
empty_name = {"name": ""}

# Виклики
print(create_user(valid_data))      # User Artem created
print(create_user(missing_name))    # Error: 'name' key is missing
print(create_user(empty_name))      # Error: 'name' cannot be empty