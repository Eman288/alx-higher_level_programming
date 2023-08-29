#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    try:
        while (x):
            print(my_list[num], end="")
            num += 1
            x -= 1
    except IndexError:
        num = num + 0
    finally:
        print('')
        return num
