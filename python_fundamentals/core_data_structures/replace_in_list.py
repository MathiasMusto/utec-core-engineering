#!/usr/bin/env python3
"""Module that replaces an element in a list at a specific position."""


def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
