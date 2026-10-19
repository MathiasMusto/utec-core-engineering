#!/usr/bin/env python3
"""Module that contains the uppercase function."""


def uppercase(str):
    """Prints a string in uppercase."""
    print("".join(chr(ord(c) - 32) if 97 <= ord(c) <= 122 else c for c in str))
