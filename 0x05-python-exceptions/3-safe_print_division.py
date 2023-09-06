#!/usr/bin/python3
# 3-safe_print_division.py
# Victorinox2

def safe_print_division(a, b):
    try:
        div = a / b
    except ZeroDivisionError:
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div
