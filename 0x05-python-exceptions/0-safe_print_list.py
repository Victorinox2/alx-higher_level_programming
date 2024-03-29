#!/usr/bin/python3
# 0-safe_print_list.py
# Victorinox3

def safe_print_list(my_list=[], x=0):
    y = 0
    for z in range(x):
        try:
            print(my_list[z], end="")
            y += 1
        except IndexError:
            break
    print()
    return y
