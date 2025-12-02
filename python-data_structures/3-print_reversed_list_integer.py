#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    reversed_list = my_list.sort(reverse=True)
    for i in reversed_list:
        print(i)
