"""
Собственным делителем числа называется всякий его делитель, отличный
от самого числа. Напишите функцию, которая будет возвращать список
всех собственных делителей заданного числа. Само это число должно
передаваться в  функцию в  виде единственного аргумента. Результатом
функции будет перечень собственных делителей числа, собранных в список.
Основная программа должна демонстрировать работу функции,
запрашивая у пользователя число и выводя на экран список его собственных
делителей. Программа должна запускаться только в том случае, если она
не импортирована в виде модуля в другой файл.
"""

def dividers(n: int) -> list:
    result = []
    for div in range(1, n):
        if n % div == 0:
            result.append(div)

    return result


def main():
    n = int(input('Enter number: '))
    r = dividers(n=n)
    print(r)


if __name__ == '__main__':
    main()