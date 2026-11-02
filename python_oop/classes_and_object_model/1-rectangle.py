#!/usr/bin/env python3
"""Módulo que define una clase Rectangle."""


class Rectangle:
    """Representa un rectángulo."""

    def __init__(self, width=0, height=0):
        """Inicializa una instancia de Rectangle.

        Args:
            width (int): El ancho del rectángulo.
            height (int): La altura del rectángulo.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Recupera el valor del ancho (getter)."""
        return self.__width

    @width.setter
    def width(self, value):
        """Establece y valida el valor del ancho (setter)."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Recupera el valor de la altura (getter)."""
        return self.__height

    @height.setter
    def height(self, value):
        """Establece y valida el valor de la altura (setter)."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
