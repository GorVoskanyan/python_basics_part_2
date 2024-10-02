"""
Расширьте свое решение упражнения 122, чтобы ваш анализатор корректно
обрабатывал символы в верхнем регистре и знаки препинания, такие
как запятая, точка, а также восклицательный и  вопросительный знаки.
Если в оригинале слово начинается с заглавной буквы, то в переводе на
«поросячью латынь» оно также должно начинаться с  заглавной буквы,
тогда как буквы, перенесенные в конец слов, должны стать строчными.
Например, слово Computer должно быть преобразовано в Omputercay. Если
в конце слова стоит знак препинания, он там же и должен остаться после
выполнения перевода. То есть слово в конце предложения Science!
необходимо трансформировать в Iencescay!.
"""

vowels = 'aeiuo'
symbols = '.,!?'

is_upper = False
word = input('>>> ')
if word[0].isupper():
    is_upper = True

symbol = '' if word[-1] not in symbols else word[-1]    # ternary operator
word = word.lower()

changed_word = ''

if word[0] not in vowels:
    for i in range(len(word)):
        if word[i] in vowels:
            if symbol:
                changed_word += word[i:-1] + word[:i] + 'ay'
            else:
                changed_word += word[i:] + word[:i] + 'ay'
            break
    changed_word += symbol
else:
    if symbol:
        changed_word += word[:-1] + 'way' + symbol
    else:
        changed_word += word + 'way'

if is_upper:
    changed_word = changed_word.capitalize()

print(changed_word)

