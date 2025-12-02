#!/usr/bin/python3

def multiple_returns(sentence):
    tuple_of_sentence = tuple(sentence)
    if len(tuple_of_sentence) < 1:
        return 0, None
    else:
        return len(tuple_of_sentence), tuple_of_sentence[0]
