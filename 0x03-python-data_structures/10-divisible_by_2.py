#!/usr/bin/python3
# File: 10-divisible_by_2.py
# Auth: Victorinox2

def divisible_by_2(my_list=[]):
    """finds all multiples of two"""
    multiples = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)
    return (multiples)
