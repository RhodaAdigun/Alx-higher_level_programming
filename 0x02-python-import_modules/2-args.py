#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    arg = len(sys.argv)
    if arg == 1:
        print("0 arguments.")
    elif arg == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(arg - 1))
        while i < arg:
            print("{:d}: {}".format(i, sys.argv[i]))
            i += 1
