#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total = 0
    arg = len(sys.argv)
    for i in range(arg-1):
        total += int(sys.argv[i + 1])
    print(total)
