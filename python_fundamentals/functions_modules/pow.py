#!/usr/bin/env python3
"""Module that contains the pow function."""


def pow(a, b):
    """Computes a to the power of b without using ** operator."""
    if b == 0:
        return 1
    
    result = 1
    abs_b = -b if b < 0 else b

    for _ in range(abs_b):
        result *= a

    if b < 0:
        return 1 / result
    
    return result
