#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys

"""Idf/O"""

argm = sys.argv
null = argm.pop(0)

lst = load_from_json_file("add_item.json")
save_to_json_file(argm, lst)
