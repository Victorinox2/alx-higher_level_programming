#!/usr/bin/python3

# File: 9-print_last_digit.py
# Auth: Victorinox2

def print_last_digit(number):
    print(abs(number) % 10, end="")
    return(abs(number) % 10)
