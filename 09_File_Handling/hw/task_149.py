"""
В операционных системах на базе Unix обычно присутствует утилита с названием head.
Она выводит первые десять строк содержимого файла, имя которого передается в качестве аргумента командной строки.
Напишите программу на Python, имитирующую поведение этой утилиты. Если файла, указанного пользователем,
не существует, или не задан аргумент командной строки, необходимо вывести соответствующее сообщение об ошибке.
"""

import sys

if len(sys.argv) == 1:
    sys.exit('Filename must be provided at command line.')
try:
    filename = sys.argv[1]
    with open(filename, 'r', encoding='utf-8') as file:
        first_ten_lines = ''.join(file.readlines()[:10])
        print(first_ten_lines)
except FileNotFoundError:
    print('Wrong filename...')
    