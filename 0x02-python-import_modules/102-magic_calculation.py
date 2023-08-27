#!/usr/bin/python3

# File: 102-magic_calculation.py
# Auth: Victorino2

def magic_calculation(a, b):
    """Match bytecode provided by CS Tech"""
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)
    else:
        return(sub(a, b))
