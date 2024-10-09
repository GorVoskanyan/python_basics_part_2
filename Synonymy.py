# Введите количество пар слов: 3
# Первая пара: Привет — Здравствуйте
# Вторая пара: Печально — Грустно
# Третья пара: Весело — Радостно
# Введите слово: интересно
# Такого слова в словаре нет.
# Введите слово: здравствуйте
# Синоним: Привет

n = int(input('Mutqagreq bareri qanaky: '))

synonyms = {}

for i in range(n):
    zuyger = input(f'{i} mutqagreq zuygy').split('-')
    synonyms[zuyger[1].lower()] = zuyger[0]

bar = input("mutqagreq bary: ").lower()

if bar in synonyms:
    print(f'homanish: {synonyms[bar]}')
else:
    print('aydpisi bar chka bararanum')


