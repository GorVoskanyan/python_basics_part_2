class RandomNumber:
    def __init__(self, limit):
        self.__limit = limit
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__counter < self.__limit:
            self.__counter += 1
            return __import__('random').randint(-100, 100)
        else:
            raise StopIteration


random_iterator = RandomNumber(limit=3)
# print(random_iterator.__next__())
# print(random_iterator.__next__())
# print(random_iterator.__next__())
# print(random_iterator.__next__())

for random_number in random_iterator:
    print(random_number)