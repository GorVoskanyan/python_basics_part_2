"""
В данном упражнении мы напишем программу, выполняющую симуляцию игры в лото с одной картой.
Начните с генерирования списка из всех
возможных номеров для выпадения (от B1 до O75). После этого перемешайте номера в хаотичном порядке,
воспользовавшись функцией shuffle
из модуля random. Вытаскивайте по одному номеру из списка и зачеркивайте номера, пока карточка не окажется
выигравшей. Проведите 1000 симуляций и выведите на экран минимальное, максимальное и среднее количество извлечений номеров,
требующееся для выигрыша. При решении
этой задачи вы можете воспользоваться функциями из упражнений 146
и 147.
"""
from random import shuffle
from time import sleep

from task_146 import card_generator, print_card
from task_147 import check_card


def game_main_loop(card: dict) -> None:
    box = list(range(1, 76))
    shuffle(box)

    print('Welcome Bingo Game!'.center(18, '^'))
    while not check_card(card):
        print_card(card)
        lucky_number = box.pop()
        print(f"{lucky_number}".center(18, '_'))
        sleep(3)
        
        for value in card.values():
            if lucky_number in value:
                value[value.index(lucky_number)] = 0

    print_card(card)
    print('Game Over!'.center(18))


def main():
    card = card_generator()
    game_main_loop(card)


if __name__ == '__main__':
    main()