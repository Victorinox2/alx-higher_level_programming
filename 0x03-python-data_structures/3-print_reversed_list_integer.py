#!/usr/bin/python3
# File: 3-print_reversed_list_integer.py
# Auth: Victorinox2

def print_reversed_list_integer(my_list=[]):
    """print all integers of list in reverse."""
    if isinstance(my_list, list):
        my_list.reverse()
        for x in my_list:
            print("{:d}".format(x))
