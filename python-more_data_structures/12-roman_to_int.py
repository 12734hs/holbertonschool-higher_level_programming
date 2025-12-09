#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_letter = {"C": 100, 'L': 50, "X": 10, "V": 5, "I": 1}
    if isinstance(roman_string, str) and not isinstance(roman_string, type(None)):
        accumulator = 0
        for index, roman in enumerate(roman_string):
            now_number = roman_letter[roman_string[index]]
            if index == 0:
                accumulator += roman_letter[roman]
            elif roman_letter[roman_string[index-1]] < now_number:
                accumulator += now_number - 2 * roman_letter[roman_string[index-1]]
            else:
                accumulator += roman_letter[roman]
        return accumulator
    else:
        return 0
