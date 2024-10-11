# try except
# try:
#     file = open('text.txt', 'r+', encoding='utf-8')
#     file.write('Hello World!\n')
# except FileNotFoundError:
#     print('File is now created!')
#     file = open('text.txt', 'x', encoding='utf-8')
# else:
#     file = open('text.txt', 'r', encoding='utf-8')
#     print(file.read())
# finally:
#     print('Finally block always work')
#     file.close()



# a = 1
# b = 'a'

# try:
#     print(a / b)
# except ZeroDivisionError:
#     print('B must be a non zero.')
# except TypeError:
#     print('B must be a integer.')
#
# print('ok')



# while True:
#     try:
#         n = int(input('Enter integer: '))
#         break
#     except ValueError as msg:
#         print('Try again...')
#         print(msg)
#
# print(n)
# print(type(n))


# class MyException(Exception):
#     pass
#
# try:
#     raise MyException('My first exception')
# except MyException:
#     print('Ok')
