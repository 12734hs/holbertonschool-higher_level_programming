#!usr/bin/python3

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (self.radius * self.radius) * 3.14

    def perimeter(self):
        return 2 * (3.14 * self.radius)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape):
    print(shape.area())
    print(shape.perimeter())

shape_info(Rectangle(5, 5))
shape_info(Circle(5))
