#!/usr/bin/env python3
"""Module that contains a function to print a list of integers."""


def print_list_integer(my_list=[]):
    """Prints all integers of a list."""
    for i in my_list:
        print("{:d}".format(i))
