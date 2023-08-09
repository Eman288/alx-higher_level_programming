#!/usr/bin/python3
i = 122
c = i
for j in range(26):
    c = i
    if i % 2 != 0:
        c -= 32
    print("{}".format(chr(c)), end="")
    i -= 1
