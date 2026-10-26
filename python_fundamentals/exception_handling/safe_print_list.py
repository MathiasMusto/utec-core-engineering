#!/usr/bin/env python3


def safe_print_list(my_list=[], x=0):
    i = 0
    nb_print = 0
    while i < x:
        try:
            print(my_list[i], end="")
            nb_print += 1
        except IndexError:
            break
        i += 1
    print()
    return nb_print
