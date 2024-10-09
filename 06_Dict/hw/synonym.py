# Введите количество пар слов: 3
# Первая пара: Привет — Здравствуйте
# Вторая пара: Печально — Грустно
# Третья пара: Весело — Радостно
# Введите слово: интересно
# Такого слова в словаре нет.
# Введите слово: здравствуйте
# Синоним: Привет

words_count = int(input('Введите количество пар слов: '))
dictionary = dict()

for i in range(1, words_count + 1):
    word1, word2 = input(f'{i} пара: ').split(' - ')
    dictionary[word1] = word2

word = input('Введите слово: ')
while word != '':
    for key, value in dictionary.items():
        if word == key:
            print(f"Синоним: {value}")
            break
        elif word == value:
            print(f"Синоним: {key}")
            break
    else:
        print('Такого слова в словаре нет.')
    word = input('Введите слово: ')