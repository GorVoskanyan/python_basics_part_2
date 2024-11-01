import time
from typing import Callable, Any


def squares_sum() -> int:
    return sum(i**2 for i in range(10000))

def cubes_sum(n: int) -> int:
    return sum(i**3 for i in range(n))

def timer(func: Callable, *args, **kwargs) -> Any:
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f'Runtime: {end - start}')
    return result


my_squares_sum = timer(func=squares_sum)
print(my_squares_sum)

my_cubes_sum = timer(cubes_sum, 10000)
print(my_cubes_sum)