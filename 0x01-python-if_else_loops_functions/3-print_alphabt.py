#!/usr/bin/python3

# File: 3-print_alphabt.py
# Auth: Victorinox2

for num in range(97, 123):
    if chr(num) != 'q' and chr(num) != 'e':
        print("{}".format(chr(num)), end="")
