#!/usr/bin/python3
# File: 101-square_matrix_map.py
# Auth: Victorinox2

def square_matrix_map(matrix=[]):
    return (list(map(lambda x: list(map(lambda y: y**2, x))
