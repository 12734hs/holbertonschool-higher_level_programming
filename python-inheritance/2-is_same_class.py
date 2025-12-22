#!/usr/bin/python3
"""This is abput inheritance in oop python"""


def is_same_class(obj, a_class):
    """this is method for check is the object is classes or not"""
    if type(obj) == type(a_class):
        return True
    else:
        return False
