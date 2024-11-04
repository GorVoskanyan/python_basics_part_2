from abc import ABC, abstractmethod

class Figure(ABC):
    """Abstract base class."""
    def __init__(self, x, y, size_1, size_2):
        self._x = x
        self.y = y
        self.size_1 = size_1
        self.size_2 = size_2

    @abstractmethod
    def move(self, new_x , new_y):
        self.x = new_x
        self.y = new_y

    def resize(self, new_size_1, new_size_2):
        self.size_1 = new_size_1
        self.size_2 = new_size_2


class ResizebleMixin:
    def resize(self, size_1, size_2):
        self.size_1 = size_1
        self.size_2 = size_2


class Rectangle(Figure, ResizebleMixin):
    def __init__(self, x, y, size1, size2):
        super().__init__(x, y, size1, size2)


class Square(Figure, ResizebleMixin):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)


rect1 = Rectangle(10, 20, 5, 6)
rect2 = Rectangle(20, 10, 3, 7)
square = Square(5, 6, 10)

for figure in [rect1, rect2, square]:
    new_size1 = figure.size_1 * 2
    new_size2 = figure.size_2 * 2
    figure.resize(new_size1, new_size2)


# print(square.size_1)
# print(square.size_2)

figure = Figure(1,1,1,1)
