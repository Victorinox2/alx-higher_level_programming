#!/usr/bin/python3
# File: 102-complex_delete.py
# Auth: Victorinox2

def complex_delete(a_dictionary, value):
    """Delete key with a specific value in a dictionary"""
    while value in a_dictionary.values():
        for x, y in a_dictionary.items():
            if y == value:
                del a_distance[k]
                break

    return (a_dictionary)
