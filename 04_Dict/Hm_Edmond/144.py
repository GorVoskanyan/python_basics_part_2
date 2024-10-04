# ### Понятие анаграмм не ограничивается словами, а может быть расширено
#  до целых предложений. Например, строки «William Shakespeare» и «I am
#  a weakish speller» являются полными анаграммами, если игнорировать
#  пробелы и заглавные буквы.
#  Расширьте свою программу из упражнения 143, добавив возможность
#  проверки на анаграммы целых фраз. При анализе не обращайте внимания
#  на знаки препинания, заглавные буквы и пробелы



def are_anagrams(text_1, text_2):
    text_1 = ''.join([char for char in text_1 if char.isalpha()])
    text_2 = ''.join([char for char in text_2 if char.isalpha()])
    return sorted(text_1.lower()) ==sorted(text_2.lower())


text_1 = input('>>>>:')
text_2 = input('>>>>:')
if are_anagrams(text_1,text_2):
    print('Words are Anagrams')
else:
    print('Not Anagrams')