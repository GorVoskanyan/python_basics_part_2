from abc import ABC, abstractmethod

class Figure(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return (self.width + self.length) * 2

    def calculate_area(self):
        return self.width * self.length


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def calculate_area(self):
        p = (self.a + self.b + self.c) / 2
        return p * ((p - self.a) * (p - self.b) * (p - self.c))


rectangle = Rectangle(3, 4)
triangle = Triangle(3, 4, 5)
print(rectangle.perimeter())
print(triangle.perimeter())

print(rectangle.calculate_area())
print(triangle.calculate_area())
