"""
программе вам необходимо запросить у пользователя строку.
После этого программа должна преобразовать его в соответствующую
последовательность точек и тире, вставляя пробелы между отдельными
символами. Символы, не представленные в таблице, можно игнорировать
"""
symbol_dict={'A': '.–', 'B': '–...', 'C': '–.–.',
             'D': '–..', 'E': '.', 'F': '..–.',
             'G': '––.', 'H': '….', 'I': '..',
             'J': '.–––', 'K': '–.–', 'L': '.–..',
             'M': '––', 'N': '–.', 'O': '–––',
             'P': '.––.', 'Q': '––.–', 'R': '.–.',
             'S': '...', 'T': '–', 'U': '..–', 'V': '...–',
             'W': '.––', 'X': '–..–', 'Y': '–.––',
             'Z': '––..', '1': '.––––','2': '..–––',
             '3': '...––','4': '….–', '5': '…..',
             '6': '–….', '7': '––...',
             '8': '–––..','9': '––––.',
             '0': '–––––' }

user_word= input('>>> :')
word_item=[]
result=[]
for i in range(len(user_word)):
    word_item.append(user_word[i])
print(word_item)


for e in symbol_dict:
    result.append(symbol_dict[e])
print(result)
