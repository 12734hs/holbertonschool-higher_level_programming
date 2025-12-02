#!/usr/bin/python3

def no_c(my_string):
    lst_letters = list(my_string)
    for i in my_string:
        if i == 'c' or i == "C":
            index_of_lst = lst_lettters.index(i)
            lst_letters.pop(index_of_lst))

    return ''.join(lst_letters)
