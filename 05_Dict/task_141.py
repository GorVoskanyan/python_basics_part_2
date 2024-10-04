"""
Несмотря на то что популярность оплаты по чекам за последние годы
серьезно снизилась, некоторые компании до сих пор используют этот способ для
ведения взаиморасчетов с сотрудниками и поставщиками.
Сумма на чеках обычно указывается дважды: один раз цифрами, второй – прописью на английском языке.
Повторение суммы двумя разными формами
записи призвано не позволить недобросовестным сотрудникам или поставщикам изменять
сумму на чеках перед их обналичиванием.
В данном упражнении вам необходимо написать функцию, принимающую в качестве входного
параметра число от 0 до 999 и возвращающую
строку прописью. Например, если значение параметра будет равно 142,
функция должна вернуть следующую строку: «one hundred forty two».
Используйте один или несколько словарей вместо условных конструкций
if/elif/else для выработки решения этой задачи. Напишите основную
программу, в которой пользователь будет вводить числовое значение, а на
экран будет выводиться соответствующая сумма прописью.
"""

points = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

ten_to_twenty = {
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}

tens = {
    10: 'ten',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninty'
}


def converter(number: int) -> str:
    if number == 0:
        return 'zero'

    if number in points:
        return points[number]

    if 10 <= number <= 99:
        if number in ten_to_twenty:
            return ten_to_twenty[number]
        elif number % 10:
            return tens[number // 10 * 10] + ' ' + points[number % 10]
        else:
            return tens[number]
    elif 100 <= number <= 999:
        if not number % 100:
            return points[number // 100] + ' hundred'
        elif number % 100 in tens:
            return points[number // 100] + ' hundred ' + tens[number % 100]
        elif number % 100 in ten_to_twenty:
            return points[number // 100] + ' hundred ' + ten_to_twenty[number % 100]
        else:
            point = points[number % 10] if number % 10 else ''
            if number % 100 // 10:
                return points[number // 100] + ' hundred ' + tens[number % 100 // 10 * 10] + ' ' + point
            else:
                return points[number // 100] + ' hundred ' + point


converted = converter(0)
print(converted)