#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv) - 1))
    else:
        if len(sys.argv) == 2:
            print("{} argument:".format(len(sys.argv) - 1))
        else:
            print("{} arguments:".format(len(sys.argv) - 1))
        for i in range(len(sys.argv) - 1):
            print("{}: {}".format(i + 1, sys.argv[i + 1]), end="\n")
