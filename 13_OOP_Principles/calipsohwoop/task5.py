
import random

class Cell:
    def __init__(self,number,sign):
        self.number=number
        self.sign=sign
        self.busy=False

    def change_state(self,sign):
        if not self.busy:
            self.sign=sign
            self.busy=True


class Player:
    def __init__(self,name,sign):
        self.name=name
        self.sign=sign
        self.win=0

    def make_move(self,board):
        while True:






