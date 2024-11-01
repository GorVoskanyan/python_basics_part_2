from typing import Callable, Any
from functools import wraps

def how_are_you(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        how = input('How are you? ')
        if how == 'ok':
            result = func(*args, **kwargs)
            return result
        return 'try again...'
    return wrapper

@how_are_you
def test(x: int, y: int) -> int:
    return x + y

res = test(3, 4)
print(res)