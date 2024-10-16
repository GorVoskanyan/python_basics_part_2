import sys

# sys.setrecursionlimit(5000)

def factorial(n):
    if n == 1:
        return 1
    else:
        result = factorial(n - 1)
        return n * result

# result = factorial(5)
# print(result)


def unpack_list(l: list):
    if not l:
        return 0
    if isinstance(l[0], int):
        return l[0] + unpack_list(l[1:])
    elif isinstance(l[0], list):
        return unpack_list(l[0])

# l = [1, 1, [1, [1, [1, 1, 1, [1, [1, [1, [1, [1,[1,[1]]]]]]]]]]]
# result = unpack_list(l)
# print(result)   # -> [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# from functools import cache
# @cache

cache = dict()

def fibonacci(n):
    # return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)
    if n <= 1:
        return n
    if n not in cache:
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return cache[n]

fibo_5 = fibonacci(50)
print(fibo_5)