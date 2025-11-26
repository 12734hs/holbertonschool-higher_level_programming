#!/usr/bin/python3
def remove_char_at(string, n):
    if len(string) >= n > 0:
        lss = list(string)
        lss.pop(n)
        return ''.join(lss)
    else:
        return string
