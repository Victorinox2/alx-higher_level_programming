#!/usr/bin/python3
# File: 9-max_integer.py
# Auth: Victorinox2

def max_integer(my_list=[]):
    """find the biggest integer of a list"""
    if len(my_list) == 0:
        return (None)
    big = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > big:
            big = my_list[i]

    return (big)
