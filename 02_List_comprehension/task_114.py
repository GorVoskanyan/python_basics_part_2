"""
Напишите программу, запрашивающую у пользователя целые числа, пока
он не оставит строку ввода пустой. После окончания ввода на экран должны быть выведены сначала все отрицательные
числа, которые были введены, затем нулевые и только после этого положительные. Внутри каждой
группы числа должны отображаться в той последовательности, в которой
были введены пользователем. Например, если он ввел следующие числа:
3, -4, 1, 0, -1, 0 и -2, вывод должен оказаться таким: -4, -1, -2, 0, 0, 3 и 1.
Каждое значение должно отображаться на новой строке.
"""

negatives = []
zeros = []
positives = []


while num := input('Enter num: '):
    num = int(num)
    if num < 0:
        negatives.append(num)
    elif num == 0:
        zeros.append(num)
    else:
        positives.append(num)

# for num in negatives:
#     print(num, end=', ')
# for num in zeros:
#     print(num, end=', ')
# for num in positives:
#     print(num, end=', ')

result = negatives + zeros + positives

for num in result:
    print(num, end=', ')