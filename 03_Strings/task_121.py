"""
Для выигрыша главного приза необходимо, чтобы шесть номеров на лотерейном билете совпали
с шестью числами, выпавшими случайным образом в диапазоне от 1 до 49 во время очередного тиража.
Напишите программу, которая будет случайным образом подбирать шесть номеров для
вашего билета. Убедитесь в том, что среди этих чисел не будет дубликатов.
Выведите номера билетов на экран по возрастанию.
"""
import random

# ticket = []

# while True:
#     number = random.randint(1, 49)
#     if number not in ticket:
#         ticket.append(number)
#
#     if len(ticket) == 6:
#         break

# ticket = random.sample(range(1, 50), k=6)
# print(ticket)