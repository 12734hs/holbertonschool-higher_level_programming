#!/usr/bin/python3
"""Hello guys, how is weather today"""


class Square:
    """It is a class, as you can see it"""

    def __init__(self, size=0, position=(0,0)):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

        if len(position) == 2:
            isint1 = isinstance(position[0], int)
            isint2 = isinstance(position[1], int)
            if isint1 and isint2 and position[0] >= 0 and position[1] >= 0:
                self.__position = position
            else:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) == 2:
            isint1 = isinstance(value[0], int)
            isint2 = isinstance(value[1], int)
            if isint1 and isint2 and value[0] >= 0 and value[1] >= 0:
                self.__position = value
            else:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(1, self.__position[1] + 1):
                print()
            for i in range(1, self.__size + 1):
                for k in range(0, self.__position[0]):
                    print(' ', end='')
                print(self.__size * "#")
