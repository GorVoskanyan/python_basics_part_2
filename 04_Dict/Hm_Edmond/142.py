# ###Напишите программу, определяющую и выводящую на экран количество
# уникальных символов во введенной пользователем строке.
# Например,в строке Hello, World! содержится десять уникальных символов, а в строке
# zzz – один. Используйте словарь или набор для решения этой задачи.
# ###



text = input('>>>>:' )
simvols = {}
for sim in text:
    simvols[sim] = True
print('=>', len(simvols))