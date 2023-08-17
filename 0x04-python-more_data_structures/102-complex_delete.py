#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a = list(a_dictionary)
    for i in a:
        if a_dictionary[i] == value:
            del a_dictionary[i]
    return a_dictionary
