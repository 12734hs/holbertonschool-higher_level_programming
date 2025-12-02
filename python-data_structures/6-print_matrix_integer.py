#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for lists in matrix:
        for i in lists:
            print('{:d}'.format(i), end='')
        print('')
