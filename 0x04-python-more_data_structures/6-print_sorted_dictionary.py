#!/usr/bin/python3
# File: 6-print_sorted_dictionary.py
# Auth: Victorinox2

def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys"""
    [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]
