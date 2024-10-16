"""
Продолжая тему предыдущего упражнения, в тех же операционных системах на базе Unix обычно есть и утилита
с названием tail, которая отображает последние десять строк содержимого файла, имя которого передается
в качестве аргумента командной строки. Реализуйте программу, которая будет делать то же самое.
Так же, как и в упражнении 149, в случае отсутствия файла, указанного пользователем, или аргумента командной
строки вам нужно вывести соответствующее сообщение.
"""

import sys

if len(sys.argv) == 1:
    sys.exit('Filename must be provided at command line.')
try:
    filename = sys.argv[1]
    with open(filename, 'r', encoding='utf-8') as file:
        first_ten_lines = ''.join(file.readlines()[-10::])
        print(first_ten_lines)
except FileNotFoundError:
    print('Wrong filename...')