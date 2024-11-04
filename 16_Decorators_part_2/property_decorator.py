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

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if name.isaplpha():
            self.__name = name
        raise Exception('Name error.')

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int) -> None:
        if 18 < age < 65:
            self.__age = age
        else:
            raise Exception('Age must be in range 18-65')


person = Person(name='ALex', age=30)
print(person.name)
print(person.age)
person.age = 95
print(person.age)

