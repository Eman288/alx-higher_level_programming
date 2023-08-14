#!/usr/bin/python3
def no_c(my_string):
    strd = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            strd += i
    return strd
