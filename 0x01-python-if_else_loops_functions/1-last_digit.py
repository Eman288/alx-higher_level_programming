#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number % 10
if number < 0:
    num = ((number * -1) % 10) * -1
if num > 5:
    print("Last digit of", number, "is", num, "and is greater than 5")
elif num % 10 == 0:
    print("Last digit of", number, "is", num, "and is 0")
else:
    print("Last digit of", number, "is", num, "and is less than 6 and not 0")
