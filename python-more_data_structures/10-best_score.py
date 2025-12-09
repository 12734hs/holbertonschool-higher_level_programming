#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        key = ''
        grades = list(a_dictionary.values())
        max_grade = max(grades)
        for i in a_dictionary.keys():
            if a_dictionary[i] == max_grade:
                key = i
            else:
                pass
        return key
    else:
        return None
