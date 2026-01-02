#!/usr/bin/python3
"""PART:I/O"""


def append_write(filename="", text=''):
    """fucnt"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
