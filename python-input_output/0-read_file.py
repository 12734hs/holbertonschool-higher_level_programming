#!/usr/bin/python3
"""PART:I/O"""


def read_file(filename=''):
    """funct"""
    with open(filename, 'r') as file:
        file.read()
