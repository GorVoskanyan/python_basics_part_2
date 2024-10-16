"""
Напишите программу, которая будет считывать содержимое файла, добавлять к считанным строкам
порядковый номер и сохранять их в таком виде в новом файле. Имя исходного файла необходимо запросить
у пользователя, так же, как и имя целевого файла. Каждая строка в созданном
файле должна начинаться с ее номера, двоеточия и пробела, после чего должен идти текст строки из исходного файла.
"""

input_filename = input('Enter filename: ')
output_filename = input('Enter output filename: ')

with open(input_filename, 'r', encoding='utf-8') as input_file, \
    open(output_filename, 'a', encoding='utf-8') as output_file:
    lines = input_file.readlines()
    for i, line in enumerate(lines, 1):
        output_file.write(f"{i}: {lines[i]}")

