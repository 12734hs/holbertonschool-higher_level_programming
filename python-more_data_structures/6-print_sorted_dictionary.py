#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    lst_of_keys = list(a_dictionary.keys())
    lst_of_keys.sort()
    for i in range(0, len(lst_of_keys)):
        print('{}: {}'.format(lst_of_keys[i], a_dictionary[lst_of_keys[i]]))
