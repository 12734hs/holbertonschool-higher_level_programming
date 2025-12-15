#!/usr/bin/python3
"""This class was created for make square guy"""


class Square:
    """This class was created for make square guy"""
    def __init__(self, size=None):
        if size == None:
            pass
        else:
            check = isinstance(size, int)
            check2 = size > 0
            if check == True and check2 == True:
                self.__size = size
            elif check != True and check2 == True:
                raise TypeError("size must be an integer")
            elif check == True and check2 != True:
                raise ValueError ("size must be >= 0")
