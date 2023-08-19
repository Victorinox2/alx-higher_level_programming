#!/usr/bin/python3
# File: 6-print_matrix_integer.py
# Auth: Victorinox2

def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers"""
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            print("{:}".format(matrix[x][y], end=""))
            if y! = (len(matrix[x]) - 1):
                print(" ", end="")
        print("")
