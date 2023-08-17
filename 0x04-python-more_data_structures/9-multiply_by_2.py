#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_diction = a_dictionary.copy()
    for i in new_diction:
        new_diction[i] *= 2
    return new_diction
