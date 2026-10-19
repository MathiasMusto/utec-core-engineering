#!/usr/bin/env python3
"""Module that contains the uppercase function."""


def uppercase(str):
    """Prints a string in uppercase."""
    for c in str:
        if 97 <= ord(c) <= 122:
            print("{:c}".format(ord(c) - 32), end="")
        else:
            print("{:c}".format(ord(c)), end="")
    print()
