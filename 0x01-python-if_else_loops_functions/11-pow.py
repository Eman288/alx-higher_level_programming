#!/usr/bin/python3
def pow(a, b):
    c = 1
    if b >= 0:
        for i in range(b):
            c *= a
    else:
        b *= -1
        for i in range(b):
            c /= a
    return c
