#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    final_dict = a_dictionary.copy()
    for k, v in a_dictionary.items():
        final_dict[k] = v * 2
    return final_dict
