from functools import wraps
from typing import Callable


def call_count(func: Callable) -> Callable:
    count = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        res = func(*args, **kwargs)
        count += 1
        print(count)
        return res
    return wrapper


@call_count
def test(): return 1


test()
test()
test()
