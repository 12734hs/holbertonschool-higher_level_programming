#!/usr/bin/python3
def fizzbuzz():
    strr = ""
    for i in range(1, 101):
        if i % 15 == 0:
            strr += "FizzBuzz "
        elif i % 5 == 0:
            strr += "Buzz "
        elif i % 3 == 0:
            strr += "Fizz "
        else:
            strr += "{} ".format(i)
    
    print(strr)
