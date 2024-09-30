# #Для выигрыша главного приза необходимо, чтобы шесть номеров на ло-
# терейном билете совпали с шестью числами, выпавшими случайным об-
# разом в диапазоне от 1 до 49 во время очередного тиража. Напишите про-
# грамму, которая будет случайным образом подбирать шесть номеров для
# вашего билета. Убедитесь в том, что среди этих чисел не будет дубликатов.
# Выведите номера билетов на экран по возрастанию

import random
from random import randrange

min=1
max=49
numbers =[]
len_num=6


for i in range(len_num):
    elem=randrange(min,max+1,1)
    while elem in numbers:
        elem=randrange(min,max+1,1)
    numbers.append(elem)
numbers.sort()
print(numbers)