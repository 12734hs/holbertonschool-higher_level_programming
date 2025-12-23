#!/usr/bin/python3
"""Hi"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class"""
    def __init__(self):
        super().__init__()


    def area(self):
        return self.__width * self.__height
