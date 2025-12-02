#!/usr/bin/python3

def max_integer(my_list=[]):
    start = my_list[0]
    if len(my_list) < 1:
        return None
    else:
        for i in my_list:
            if i > start:
                start = i
    return start
