#!/usr/bin/env python3
"""Module that contains the print_last_digit function."""


def print_last_digit(number):
    """Prints and returns the last digit of a number."""
    if number < 0:
        last_digit = (-number) % 10
    else:
        last_digit = number % 10

    print("{:d}".format(last_digit), end="")
    return last_digit
