#!/usr/bin/python3
"""Hello dude"""


def inherits_from(obj, a_class):
    """Heloo man"""
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
