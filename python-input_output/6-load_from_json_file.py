#!/usr/bin/python3
"""PART:I/O"""

import json


def load_from_json_file(filename):
    """funct"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
