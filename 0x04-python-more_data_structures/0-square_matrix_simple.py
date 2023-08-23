#!/usr/bin/python3
# File: 0-square_matrix_simple.py
# Auth: Victorinox2

def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix"""
    return ([list(map(lamda x: x * x, row)) for row in matrix])
