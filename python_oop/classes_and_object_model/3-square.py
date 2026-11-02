#!/usr/bin/env python3
"""Módulo que define una clase Square con un método para calcular su área."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0):
        """Inicializa una instancia de Square.

        Args:
            size (int): El tamaño del cuadrado, por defecto 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calcula y devuelve el área actual del cuadrado."""
        return self.__size ** 2
