#!/usr/bin/python3
def uppercase(str):
    strr = ''
    for i in str:
        x = ord(i)
        if 96 < x < 122:
            strr += chr(x - 32)
        else:
            strr += i
    print("{}".format(strr))
