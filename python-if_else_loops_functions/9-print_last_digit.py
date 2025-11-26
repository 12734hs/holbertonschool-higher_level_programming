#!/usr/bin/python3
def print_last_digit(number):
    if number!= 0:
        result = int(str(number)[-1])
        print("{}".format(result), end='')
        return result
    else:
        print("0")
        return number
