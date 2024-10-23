import random

class House:
    def __init__(self):
        self.food = 50
        self.money = 0

class Human:
    def __init__(self, name):
        self.name = name
        self.hunger_level = 50
        self.house = House()

    def eat(self):
        if self.house.food > 0:
            self.hunger_level += 20
            self.house.food -= 10
            print(f"{self.name} is eating")
        else:
            print(f"{self.name} cant eating")

    def work(self):
        self.house.money += 10
        print(f"{self.name} working and he have   {self.house.money} ")

    def go_to_magazine(self):
        if self.house.money >= 20:
            self.house.food += 20
            self.house.money -= 20
            print(f"{self.name} by a food")
        else:
            print(f"{self.name} cant by a food")

    def play(self):
        print(f"{self.name} is playing")

    def daily_routine(self):
        if self.hunger_level < 20:
            self.eat()
        elif self.house.food < 10:
            self.go_to_magazine()
        elif self.house.money < 50:
            self.work()
        else:
            step = random.randint(1, 6)
            if step == 1:
                self.work()
            elif step == 2:
                self.eat()
            else:
                self.play()

    def year(self):
        for day in range(365):
            if self.hunger_level <= 0:
                print(f"{self.name} Game over!!")
                return
            self.daily_routine()
        print(f"{self.name} live")


human1 = Human("Jiro")
human2 = Human("Edmond")


human1.year()
human2.year()
