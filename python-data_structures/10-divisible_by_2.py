#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_lst = my_list.copy()
    if not new_lst:
        return []
    else:
        for i in lst:
            if i % 2 == 0:
                new_lst[my_list.index(i)] = True
            else:
                new_lst[my_list.index(i)] = False
    return new_lst
