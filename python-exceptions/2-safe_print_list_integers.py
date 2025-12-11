#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    final_sentence = ''
    accumulator = 0
    for i in range(0, x):
        try:
            #print("{:d}".format(my_list[i]), end="")
            final_sentence += "{}".format(my_list[i])
        except (ValueError, TypeError):
            pass
    for i in my_list:
        accumulator += 1
    print(final_sentence)
    return accumulator
