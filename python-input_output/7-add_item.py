#!/usr/bin/python3
"""I/O"""

import sys
load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file

if __name__ == "__main__":
    try:
        lst = load("add_file.json")
    except FileNotFoundError:
        lst = []
    lst.extend(sys.argv[1:])
    save(lst, "add_file.json")
