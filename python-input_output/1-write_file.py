#!/usr/bin/python3
"""PART:I/O"""


def write_file(filename="", text=''):
    """fucnt"""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
