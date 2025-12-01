#!/usr/bin/python3
import sys

lst = sys.argv
lst.pop(0)

def func():
    if len(lst) != 0:
        if len(lst) != 1:
            print("{} arguments:".format(len(lst)))
            for i in range(0, len(lst)):
                print("{}: {}".format(i + 1, lst[i]))
        else:
            print("{} argument:".format(len(lst)))
            print("{}: {}".format(len(lst), lst[0]))
    else:
        print("0 arguments.")

if __name__ == "__main__":
    func()
