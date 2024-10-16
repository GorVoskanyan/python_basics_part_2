"""
В данном упражнении вы должны написать программу, которая будет
находить самое длинное слово в файле. В качестве результата программа
должна выводить на экран длину самого длинного слова и все слова такой
длины. Для простоты принимайте за значимые буквы любые непробельные символы, включая цифры и знаки препинания.
"""

import sys

filename = sys.argv[1]

with open(filename, 'r', encoding='utf-8') as file:
    words = file.read().split()
    max_length = len(max(words, key=len))
    # result = [word for word in words if len(word) == max_length]
    result = []
    for word in words:
        if len(word) == max_length:
            result.append(word)
print(max_length)
print(result)
