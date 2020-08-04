from time import perf_counter
import functools


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        end = perf_counter()
        print(f"time taken in secs: {end-start:.4f}")
    return wrapper


@timer
def sum(a, b):
    print(a+b)


sum(5, 88)