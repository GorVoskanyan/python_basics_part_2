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

words_list = input('>>> ').split()
result = []

for word in words_list:
    if word[0].lower() in vowels:
        if word[-1] in symbols:
            result.append(word[:-1] + 'way' + word[-1])
        else:
            result.append(word + 'way')
        continue

    for index in range(len(word)):
        if word[index] in vowels:
            if word[-1] not in symbols:
                word = f"{word[index:].capitalize() if word[0].isupper() else word[index:].lower()}{word[:index]}ay"
                result.append(word)
            else:
                word = f"{word[index:-1].capitalize() if word[0].isupper() else word[index:-1]}{word[:index].lower()}ay{word[-1]}"
                result.append(word)
            break

result = ' '.join(result)
print(result)