#!/usr/bin/python3
# File: 100-weight_average.py
# Auth: Victorinox2

def weight_average(my_list=[]):
    """Return the weighted average of all integers in a list of tuples"""
    if not my_list:
        return 0
    num = 0
    den = 0

    for tup in my_list:
        num += tup[0] * tup[1]
        den += tup[1]

    return (num / den)
