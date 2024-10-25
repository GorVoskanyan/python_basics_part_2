import random

class House:
    def __init__(self):
        self.food = 50
        self.money = 0

class Man:
    def __init__(self, name, house):
        self.name = name
        self.satiety = 50
        self.house = house

    def eat(self):
        if self.house.food >= 10:
            self.satiety += 10
            self.house.food -= 10
            print(f"{self.name} ate some food. Satiety: {self.satiety}, Food left: {self.house.food}")
        else:
            print(f"{self.name} wants to eat, but there's not enough food.")
            self.go_shopping()

    def work(self):
        self.satiety -= 10
        self.house.money += 10
        print(f"{self.name} worked. Satiety: {self.satiety}, Money earned: {self.house.money}")

    def play(self):
        self.satiety -= 10
        print(f"{self.name} played. Satiety: {self.satiety}")

    def go_shopping(self):
        if self.house.money >= 20:
            self.house.food += 20
            self.house.money -= 20
            print(f"{self.name} went shopping. Food: {self.house.food}, Money left: {self.house.money}")
        else:
            print(f"{self.name} doesn't have enough money to buy food.")
            self.work()
