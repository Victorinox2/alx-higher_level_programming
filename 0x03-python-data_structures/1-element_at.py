#!/usr/bin/python3
# File: 1-element_at.py
# Auth: Victorinox2

def element_at(my_list, idx):
    """Retrieve an element from list"""
    if idx < 0 or idx > (len(my_list) -1):
        return None
    return (my_list[idx])
