"""
В данном упражнении мы будем симулировать 1000 выбрасываний
игральных костей. Начнем с написания функции, выполняющей
случайное выбрасывание двух обычных шестигранных костей. Эта функция не
будет принимать входных параметров, а возвращать должна число,
 выпавшее в сумме на двух костях.
В основной программе реализуйте симуляцию тысячи выбрасываний
костей. Программа должна хранить все результаты с частотой их выпадения.
 После завершения процесса должна быть показана итоговая таблица
с  результатами, похожая на ту, что представлена в табл. 6.1. Выразите
частоту выпадения каждого из чисел в процентах вместе с ожидаемым
результатом согласно теории вероятностей.
"""
import  random
def sum_rock():
    return random.randint(1,6)+ random.randint (1,6)

rock_dict={}
for i in range(1000):
    rock_dict={i: sum_rock()}
    i+=1

print(rock_dict)



