#!/usr/bin/python3
"""PART:I/O"""


class Student:
    """classlolmessipessipenaldo"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}

