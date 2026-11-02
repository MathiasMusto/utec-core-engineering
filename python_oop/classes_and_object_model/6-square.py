#!/usr/bin/env python3
"""Módulo Square que define un cuadrado con tamaño y posición."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa una instancia de Square.

        Args:
            size (int): El tamaño del cuadrado.
            position (tuple): Las coordenadas de posición del cuadrado.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Recupera el valor del tamaño (getter)."""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece y valida el valor del tamaño (setter)."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Recupera el valor de la posición (getter)."""
        return self.__position

    @position.setter
    def position(self, value):
        """Establece y valida el valor de la posición (setter)."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calcula y devuelve el área actual del cuadrado."""
        return self.__size ** 2

    def my_print(self):
        """Imprime en stdout el cuadrado usando el carácter '#'."""
        print(self.__str__(), end="")

    def __str__(self):
        """Devuelve la representación en cadena del cuadrado."""
        if self.__size == 0:
            return "\n"

        result = []
        for _ in range(self.__position[1]):
            result.append("")

        for _ in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(result) + "\n"
