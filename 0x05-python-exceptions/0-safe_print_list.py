#!/usr/bin/python3
# 0-safe_print_list.py
# Victorinox3

 ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
