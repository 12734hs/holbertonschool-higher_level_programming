#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) > 1 and len(tuple_a) > 1:
        new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return new_tuple
    elif len(tuple_b) == 1 and len(tuple_a) > 1:
        new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1])
        return new_tuple
    elif len(tuple_b) < 1 and len(tuple_a) > 1:
        return tuple_a
    elif len(tuple_a) > 1 and len(tuple_b) > 1:
        new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return new_tuple
    elif len(tuple_a) == 1 and len(tuple_b) > 1:
        new_tuple = (tuple_a[0] + tuple_b[0], tuple_b[1])
        return new_tuple
    elif len(tuple_a) < 1 and len(tuple_b) > 1:
        return tuple_b
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
        new_tuple = (tuple_a[0] + tuple_b[0], 0)
        return new_tuple
    else:
        return (0, 0)
