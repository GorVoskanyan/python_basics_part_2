"""
Напишите основную программу, которая будет запрашивать у пользователя слово и при помощи
рекурсивной функции определять, является ли оно палиндромом.
В результате на экране должно появиться соответствующее сообщение.
"""

def is_palindrome(s: str) -> bool:
    if not s:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])


if is_palindrome('level'):
    print('Palindrome')
else:
    print('Not palindrome')