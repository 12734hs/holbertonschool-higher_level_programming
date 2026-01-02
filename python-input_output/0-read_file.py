#!/usr/bin/python3
"""PART:I/O"""


def readfile(filename=''):
    """funct"""
    with open(filename, 'r') as file:
        file.read()
