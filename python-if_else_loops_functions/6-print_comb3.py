#!/usr/bin/python3
for i in range(100):
    for x in range(i+1, 10):
        if int(str("{}{}".format(i, x))) != 89:
            print('{}{}'.format(i, x), end=", ")
        else:
            print('89', end='')
