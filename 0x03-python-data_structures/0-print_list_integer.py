#!/usr/bin/python3
# File: 0-print_list_integer.py
# Auth: Victorinox3

def print_list_integer(my_list=[]):
    """prints all the integers of a list."""
    for num in range(len(my_list)):
        print("{:d}".format(my_list[num]))
