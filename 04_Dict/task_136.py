
"""
Напишите функцию с названием reverseLookup, которая будет осуществлять поиск всех ключей в
словаре по заданному значению. Функция
должна принимать в качестве параметров словарь и значение для поиска
и возвращать список ключей (он может быть пустым) из этого словаря,
соответствующих переданному значению.
В основной программе продемонстрируйте работу функции путем создания словаря и поиска в нем всех ключей
по заданному значению. Убедитесь, что функция работает корректно при наличии нескольких ключей
для искомого значения, одного ключа и  их отсутствии. Ваша программа должна запускаться только в том случае,
если она не импортирована в виде модуля в другой файл.
"""

def reverse_lookup(d, v):
    res = []
    for key, value in d.items():
        if v == value:
            res.append(key)

    return res


if __name__ == '__main__':
    v = True
    d = {'name': 'Calipso', 'is_student': True, 'is_programmer': True}
    r = reverse_lookup(d, v)
    print(r)
