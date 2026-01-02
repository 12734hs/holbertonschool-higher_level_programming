#!/usr/bin/python3
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file
import sys
"""I/O"""

argm = sys.argv
null = argm.pop(0)

lst = load_from_json_file("add_item.json")
save_to_json_file(argm, lst)
