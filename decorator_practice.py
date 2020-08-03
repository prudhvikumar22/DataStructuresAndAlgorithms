import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("time taken in secs: ", end-start)
    return wrapper


@timer
def sum(a,b):
    print(a+b)


sum(5,88)