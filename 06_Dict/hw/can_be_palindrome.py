# word = input('Введите строку:')
# word = 'aab'
word = 'aabba'

if len([char for char in word if word.count(char) % 2 != 0]) <= 1:
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')