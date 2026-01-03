#!/usr/bin/python3
import pickle


class CustomObject:
    def __init__(self, name, age, is_students):
        self.name = name
        self.age = age
        self.is_student = is_students

    def display(self):
        print("name: {}".format(self.name))
        print("age: {}".format(self.age))
        print("is_student: {}".format(self.is_student))

    def serialize(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)


    @classmethod
    def deserialize(cls, filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
