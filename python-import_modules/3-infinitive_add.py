#!/usr/bin/python3
import sys

lst = sys.argv
lst.pop(0)

accumulator = 0

for i in lst:
    accumulator += int(i)

if __name__ == "__main__":
    print(accumulator)
