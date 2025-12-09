#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_letter = {"C": 100, 'L': 50, "X": 10, "V": 5, "I": 1}
    if type(roman_string) == str and roman_string is not None:
        accumulator = 0
        for index, roman in enumerate(roman_string):
            if index == 0:
                accumulator += roman_letter[roman]
            elif roman_letter[roman_string[index-1]] < roman_letter[roman_string[index]]:
                accumulator += roman_letter[roman_string[index]] - 2 * roman_letter[roman_string[index-1]]
            else:
                accumulator += roman_letter[roman]
    print(accumulator)
