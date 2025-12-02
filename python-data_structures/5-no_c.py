#!/usr/bin/python3

def no_c(my_string):
    lst_letters = list(my_string)
    for i in my_string:
        if i == 'c' or i == "C":
            lst_letters.pop(index(i))

    return ''.join(lst_letters)
