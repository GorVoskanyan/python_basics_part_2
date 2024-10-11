import sys

def fibo(n: int) -> list:
    res = []
    a, b = 0, 1
    while a < n:
        res.append(a)
        a, b = b, a+b

    return res

try:
    n = int(sys.argv[1])
    res = fibo(n)
    print(res)
except IndexError:
    print('Arguments must be provided as command line argumenst')