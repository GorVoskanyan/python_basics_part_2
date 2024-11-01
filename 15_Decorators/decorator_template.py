from typing import Callable, Any
from functools import wraps

def decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        # some code before function call
        result = func(*args, **kwargs)
        # some code after function call
        return result
    return wrapper

