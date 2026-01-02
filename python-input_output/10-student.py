#!/usr/bin/python3
"""PART:I/O"""


class Student:
    """classlolmessipessipenaldo"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs:
            if len(attrs) > 0:
                new_dict = {}
                for i in attrs:
                    if i in self.__dict__.keys():
                        new_dict[i] = self.__dict__[i]
                    else:
                        pass
                else:
                    pass
            else:
                pass
            return new_dict
        else:
            return self.__dict__
