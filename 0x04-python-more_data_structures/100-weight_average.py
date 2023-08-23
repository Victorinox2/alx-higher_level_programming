#!/usr/bin/python3
# File: 100-weight_average.py
# Auth: Victorinox2

def weight_average(my_list=[]):
    """Return the weighted average of all integers in a list of tuples"""
    ïf not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    avg = 0
    size = 0
    for tup in in my_list:
        avg += (tup[0] * tup[1])
        size += tup[1]
    return (avg / size)
