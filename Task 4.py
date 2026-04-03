# Декоратор вимірювання часу
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()  # Час до виклику

        result = func(*args, **kwargs)

        end = time.time()    # Час після виклику
        execution_time = end - start

        print(f"Execution time of {func.__name__}: {execution_time:.6f} seconds")
        return result
    return wrapper


@timer
def slow_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Тести
slow_sum(10_000)
slow_sum(100_000)
slow_sum(1_000_000)