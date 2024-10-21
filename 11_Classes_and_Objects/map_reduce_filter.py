# map(callable, iterable)
def square(x): return x ** 2

squares = map(square, [1, 2, 3, 4, 5])
print(squares)