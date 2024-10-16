"""
Разработайте программу, которая будет показывать слово (или слова),
чаще остальных встречающееся в текстовом файле. Сначала пользователь
должен ввести имя файла для обработки. После этого вы должны открыть
файл и проанализировать его построчно, разделив при этом строки по
словам и исключив из них пробелы и знаки препинания.
Также при подсчете частоты появления слов в файле вам стоит игнорировать регистры.
"""


def remove_characters(s: str) -> list:
    chars = "~!@#$%^&*()_+|}{':?><,./"
    for char in chars:
        s = s.replace(char, '')
    return s.split()


filename = input('Enter filename: ')

with open(filename, 'r', encoding='utf-8') as file:
    s = file.read().lower()
    words = remove_characters(s)
    words_dict = {
        word: words.count(word)
        for word in words
        if len(word) == len(max(words, key=len))
    }

print(words_dict)