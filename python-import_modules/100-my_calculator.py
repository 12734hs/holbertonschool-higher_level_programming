#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
list_of_arguments = argv
list_of_arguments.pop(0)
list_of_operators = ['+', '-', '*', '/']


def print_result():
    if len(list_of_arguments) == 3:
        a = int(list_of_arguments[0])
        b = int(list_of_arguments[2])
        operator = list_of_arguments[1]

        if operator == '+':
            result = add(a, b)
            print('{} {} {} = {}'.format(a, operator, b, result))

        elif operator == '-':
            result = sub(a, b)
            print('{} {} {} = {}'.format(a, operator, b, result))

        elif operator == '*':
            result = mul(a, b)
            print('{} {} {} = {}'.format(a, operator, b, result))

        elif operator == '/':
            result = div(a, b)
            print('{} {} {} = {}'.format(a, operator, b, result))

        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
    else:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)


if __name__ == "__main__":
    print_result()
