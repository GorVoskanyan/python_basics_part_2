class Fibonacci:
    def __init__(self, number):
        self.__number = number
        self.__counter = 0
        self.__cur_value = 0
        self.__next_value = 1

    def __iter__(self):
        self.__counter = 0
        self.__cur_value = 0
        self.__next_value = 1
        return self

    def __next__(self):
        if self.__counter < self.__number:
            self.__counter += 1
            self.__cur_value, self.__next_value = self.__next_value, self.__cur_value + self.__next_value
            return self.__cur_value
        else:
            raise StopIteration


fibo = Fibonacci(number=3)

print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))

# for fib in fibo:
#     print(fib, end='|')
#
# for fib in fibo:
#     print(fib, end='|')