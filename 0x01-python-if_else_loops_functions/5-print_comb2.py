#!/usr/bin/python3
i = 0
while i < 100:
    if i == 99:
        print("{}".format(i))
        i += 1
    else:
        print("{:02}".format(i), end=", ")
        i += 1
