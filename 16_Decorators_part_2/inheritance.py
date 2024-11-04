from typing import List

class Person(object):
    """Base class for all persons.

    Args:
        name (str): name of person
        age (int): age of person

    Attributes:
        __name (str): name of person, must be string
        __age (int): age of people, raise exception if not in range 18-65
        """

    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        if name.isaplpha():
            self.__name = name
        raise Exception('Name error.')

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int) -> None:
        if 18 < age < 65:
            self.__age = age
        else:
            raise Exception('Age must be in range 18-65')

    def info(self):
        print('I am person.')

class Parent(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__kids = ['Alex', 'Bob']

    def get_kids(self) -> List[str]:
        return self.__kids

    def info(self):
        print('I am parent.')


class Employee(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__salary = 20000.00

    def get_salary(self) -> float:
        return self.__salary

    def info(self):
        print('I am employee.')


class Citizen(Parent, Employee):

    def info(self):
        print('I am citizen.')



citizen = Citizen(name='John', age=30)
# print(citizen.get_name())
# print(citizen.get_age())

# print(citizen.get_kids())
# print(citizen.get_salary())

# citizen.info()

print(citizen.__class__.__mro__)    # method resolution order
print(Citizen.__mro__)