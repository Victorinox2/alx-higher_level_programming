#!/usr/bin/python3
# File: 2-replace_in_list.py
# Auth: Victorinox2

def replace_in_list(my_list, idx, element):
    """Replace an element of a list at specific position"""
    if idx > 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)
