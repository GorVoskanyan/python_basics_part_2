"""
Целое число n называется совершенным, если сумма всех его собственных
делителей равна самому числу n. Например, 28 – это совершенное число,
поскольку его собственными делителями являются 1, 2, 4, 7 и 14, а 1 + 2
+ 4 + 7 + 14 = 28.
Напишите функцию для определения того, является ли заданное число
совершенным. Функция будет принимать на вход единственный параметр и возвращать True,
если он представляет собой совершенное число,
и  False – если нет. Разработайте небольшую программу, которая будет
использовать функцию для идентификации и  вывода на экран всех совершенных чисел в диапазоне от 1 до 10 000.
При решении этой задачи
импортируйте функцию, написанную в упражнении 115.
"""

from task_115 import dividers


def is_perfect(n: int) -> bool:
    dividers_sum = sum(dividers(n))
    if dividers_sum == n:
        return True
    return False


def main():
    for num in range(1, 10001):
        if is_perfect(n=num):
            print(num, 'is perfect number.')


if __name__ == '__main__':
    main()