#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        a = my_list[x-1]
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
        return x 
    except IndexError:
        x = 0
        for item in my_list:
          x += 1
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
        return x 
