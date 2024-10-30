def fibonacci(number):
    a, b = 0, 1
    for _ in range(number):
        if a > 5:
            return
        yield a
        a, b = b, a+b

fibo_10 = fibonacci(number=30)
# print(fibo_10)

# print(next(fibo_10))
# print(next(fibo_10))
# print(next(fibo_10))
# print(next(fibo_10))
# print(next(fibo_10))
# print(next(fibo_10))
# print(next(fibo_10))

# for fib in fibo_10:
#     print(fib, end='|')


# generator expressions
data = (num for num in range(10) if not num % 2)
print(data)
print(4 in data)

