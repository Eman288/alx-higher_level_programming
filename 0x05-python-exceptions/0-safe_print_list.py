def safe_print_list(my_list=[], x=0):
    l = 0
    try:
        while (x):
            print(my_list[l], end="")
            l += 1
            x-=1
    except IndexError:
        l = l
    finally:
        print('')
        return l
