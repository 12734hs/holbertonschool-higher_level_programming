#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    final_sentence = ''
    accumulator_of_sentence = 0
    accumulator_of_list = 0
    for i in range(0, x):
        try:
            #print("{:d}".format(my_list[i]), end="")
            final_sentence += "{}".format(my_list[i])
        except (ValueError, TypeError):
            pass

    for i in my_list:
        accumulator_of_list += 1

    for i in final_sentence:
        accumulator_of_sentence

    if accumulator_of_list > accumulator_of_sentence:
        print(final_sentence)
        return accumulator_of_list
    else:
        print(final_sentence)
        return accumulator
