class Person(object):
    def __init__(self, name, age):
        self.set_name(name)  # private attribute
        self.set_age(age)

    def __str__(self):
        return f"Name: {self.__name} - Age: {self.__age}"

    def get_name(self):     # getter
        return self.__name

    def set_name(self, name):   # setter
        if name.isalpha():
            self.__name = name
        else:
            print('Name must be a alphabetic...')
            self.__name = None

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if 18 < age < 65:
            self.__age = age
        else:
            print('Age must be in range 18, 65...')
            self.__age = None



class Parent(Person):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.children = []

    def __str__(self):
        return super().__str__() + f' - {self.children}'

    def add_children(self, children):
        self.children.append(children)


parent = Parent('Gor', 28)
# print(parent.get_name())
# parent.add_children('Alex')
# print(parent.children)


class Citizen(Parent):
    def __init__(self, name, age, city):
        super().__init__(name, age)
        self.city = city


citizen1 = Citizen('Gor', 28, 'Yerevan')
# citizen1.add_children('Bob')
# print(citizen1.children)
# print(citizen1.salary)

person = Person('Alex', 30)
print(parent)
print(person)