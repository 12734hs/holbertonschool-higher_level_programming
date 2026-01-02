#!/usr/bin/python3
"""PART:I/O"""

json = {'first_name': "antoni", "last_name": "lionel", "age": 50}


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
            new_dict = {}
            for i in attrs:
                if i in self.__dict__.keys():
                    new_dict[i] = self.__dict__[i]
                else:
                    pass
            return new_dict

    def reload_from_json(self, json):
        for k, v in json.items():
            self.__dict__[k] = v
