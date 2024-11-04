import time

with open('example.txt', 'w', encoding='utf-8') as file:
    file.write('hello_world!\n')

class Timer:
    def __init__(self):
        print('Start calculate time.')
        self.start = None

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(time.time() - self.start)
        # if exc_type is TypeError:
        #     return True
        return True

with Timer() as t1:
    value1 = 100 * 100 ** 100000
    value1 += ''
    value1 /= 0

with Timer() as t2:
    value2 = 200 * 200 ** 100000

with Timer() as t3:
    value3 = 300 * 300 ** 100000
