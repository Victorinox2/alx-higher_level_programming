#!/usr/bin/python
# 2-args.py
# Victorinox2

if __name__ == "__main__":
    """print the number of list of an argument"""
    import sys
    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("print{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
