class Person:
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


person = Person('Gor', 28)
# print(person.__name)    # NameMangling      person._Person__name
# print(person._Person__name)

print(person.get_name())
# person.set_name('143151234')
# print(person.get_name())

print(person.get_age())
# person.set_age(33)
# print(person.get_age())