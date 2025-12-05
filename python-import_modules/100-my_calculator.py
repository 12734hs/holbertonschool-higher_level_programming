#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
list_of_arguments = sys.argv
list_of_arguments.pop(0)
list_of_operators = ['+', '-', '*', '/']


if len(list_of_arguments) == 3:
    a = int(list_of_arguments[0])
    b = int(list_of_arguments[2])
    operator = list_of_arguments[1]
    
    if operator == '+':
        result = add(a, b)
        print('{} {} {} = {}'.format(a, operator, b, result))
        print(0)
        
    elif operator == '-':
        result = sub(a, b)
        print('{} {} {} = {}'.format(a, operator, b, result))
        print(0)

    elif operator == '*':
        result = mul(a, b)
        print('{} {} {} = {}'.format(a, operator, b, result))
        print(0)

    elif operator == '/':
        result = div(a, b)
        print('{} {} {} = {}'.format(a, operator, b, result))
        print(0)
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        print(1)
else:
    print('Usage: ./100-my_calculator.py <a> <operator> <b>')
    print(1)