import time
from typing import Callable, Any
from functools import wraps

def timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Runtime: {end - start}')
        return result
    return wrapper

@timer
def squares_sum() -> int:
    return sum(i**2 for i in range(10000))

@timer
def cubes_sum(n: int) -> int:
    """Return sum of cubes 1-n."""
    return sum(i**3 for i in range(n))


my_squares_sum = squares_sum()
print(my_squares_sum)

my_cubes_sum = cubes_sum(n=10000)
print(cubes_sum.__name__)
print(cubes_sum.__doc__)
