#!/usr/bin/python3
def islower(letter):
    ord_c = ord(letter)
    if 97 < ord_c < 122:
        return True
    else:
        return False
