#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key not in list(a_dictionary.keys()):
        pass
    else:
        a_dictionary.pop(key)
    return a_dictionary
