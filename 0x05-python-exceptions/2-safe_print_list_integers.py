#!/usr/bin/python3
# 2-safe_print_list_integers.py
# Victorinox2

def safe_print_list_integers(my_list=[], x=0):
    x = 0
    for z in range(x):
        try:
            print("{:d}".format(my_list[j]), end="")
            x += 1
        except(ValueError, TypeError):
            continue
    print()
    return x
