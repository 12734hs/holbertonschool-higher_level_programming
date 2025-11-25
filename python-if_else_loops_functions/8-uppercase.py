#!/usr/bin/python3
def uppercase(str):
    for i in str:
        x = ord(i)
        if 96 < x < 122:
            print("{}".format(chr(x - 32)), end="")
        else:
            print("{}".format(i), end="")
