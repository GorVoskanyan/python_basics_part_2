class Cat:

    TOTAL_SOUNDS = 0

    def __init__(self, name):
        self.name = name
        self.legs = 4
        self.has_a_tail = True

    # @staticmethod
    # def sound():
    #     print('Meow!')

    @classmethod
    def sound(cls):
        cls.TOTAL_SOUNDS += 1
        print(cls.TOTAL_SOUNDS)
        print('Meow!')


cat = Cat('Murzik')
Cat.sound()
Cat.sound()
Cat.sound()
# print(cat.TOTAL_SOUNDS)