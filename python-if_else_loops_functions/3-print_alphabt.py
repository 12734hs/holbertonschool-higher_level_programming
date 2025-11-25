#!/usr/bin/python3
strm = ''
for i in range(97, 123):
    if chr(i) == "q" or chr(i) == "e":
        continue
    strm += chr(i)

print("{0}".format(strm), end="")
