#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit_str = list(str(number))
last_digit_int = int(last_digit_str[-1])
if number < 0:
    print(f"Last digit of {number} is {-last_digit_int} is less than 6 and not 0")
elif last_digit_int == 0:
    print(f"Last digit of {number} is {last_digit_int} and is 0")
elif 0 < last_digit_int < 6:
    print(f"Last digit of {number} is {last_digit_int} is less than 6 and not 0")
elif last_digit_int > 5:
    print(f"Last digit of {number} is {last_digit_int} and is greater than 5")
