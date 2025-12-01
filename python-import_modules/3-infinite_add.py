#!/usr/bin/python3
import sys

lst = sys.argv
lst.pop(0)

acumulator = 0

for i in lst:
    acumulator += int(i)

if __name__ == "__main__":
    print(acumulator)
