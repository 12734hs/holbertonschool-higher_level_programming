#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    reversed_list = sorted(my_list, reverse=True)
    for i in reversed_list:
        print("{:d}".format(i))
