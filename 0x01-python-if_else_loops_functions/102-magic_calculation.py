#!/usr/bin/python3

# File: 102-magic_calculation.py
# Auth: Victorinox2

def magic_calculation(a, b, c):
    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b-c)
