from typing import Callable

PLUGINS: dict[str, Callable] = dict()

def plugin(func: Callable) -> None:
    PLUGINS[func.__name__] = func


@plugin
def test1(): return 1

def test2(): return 2

@plugin
def test3(): return 3

print(PLUGINS)
