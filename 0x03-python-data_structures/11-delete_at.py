#!/usr/bin/python3
# File: 11-delete_at.py
# Auth: Victorinox2

def delete_at(my_list=[], idx=0):
    """delete an item at a specific position"""
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)
