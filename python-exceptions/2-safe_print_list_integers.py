#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        a = my_list[x]
        for i in range(0, x):
            print("{:d}".format(my_list[i]), end="")
        print()
        return x
    except IndexError:
        x = 0
        for item in my_list:
            x += 1
        for i in range(0, x):
            try:
                print("{:d}".format(my_list[i]), end="")
            except ValueError:
                pass
        print()
        return x
    except ValueError:
        a = 2
