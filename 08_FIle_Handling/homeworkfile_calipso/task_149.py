"""
В операционных системах на базе Unix обычно присутствует утилита с названием head.
 Она выводит первые десять строк содержимого файла, имя
которого передается в качестве аргумента командной строки.
 Напишите программу на Python, имитирующую поведение этой утилиты. Если
файла, указанного пользователем, не существует, или не задан аргумент
командной строки, необходимо вывести соответствующее сообщение об
ошибке.
"""
import sys

def head(filename):
    lines=10
    try:
        with open(filename, 'r') as file:
            for i in range(lines):
                line=file.readline()
                if not line:
                    break
                print(line)
    except FileNotFoundError:




