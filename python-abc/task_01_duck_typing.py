#!/usr/bin/python3
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


import math

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (abs(self.radius ** 2))

    def perimeter(self):
        return abs(2 * math.pi * self.radius)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return abs(self.width) * abs(self.height)

    def perimeter(self):
        return 2 * abs(self.width) + abs(self.height)

def shape_info(shape):
    print(shape.area())
    print(shape.perimeter())

rectangle = Rectangle(100, 200)
circle = Circle(100)

shape_info(rectangle)
shape_info(circle)
