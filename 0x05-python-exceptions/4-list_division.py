#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    for i in range(0, list_length):
        try:
            num = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            num = 0
            print("wrong type")
        except ZeroDivisionError:
            num = 0
            print("division by 0")
        except IndexError:
            num = 0
            print("out of range")
        finally:
            my_list.append(num)
    return my_list
