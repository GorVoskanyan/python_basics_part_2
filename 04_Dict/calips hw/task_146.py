import os

new_file= open('calipsnew.txt','a', encoding='utf-8')
new_file.write('Կալիպսո\n')
lista=('a','a','bb')
new_file.writelines(lista)


for line in new_file:
    print()

