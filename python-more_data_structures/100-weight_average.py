#!/usr/bin/python3
def weight_average(my_list=[]):
    result_of_number = 0
    result_of_weight = 0

    if my_list:
        for i in my_list:
            result_of_number += i[0] * i[1]
            result_of_weight += i[1]

        return result_of_number / result_of_weight
    else:
        return 0
