#!/usr/bin/env python3
"""Módulo que define una clase Square con un método para imprimir su gráfico."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0):
        """Inicializa una instancia de Square.

        Args:
            size (int): El tamaño del cuadrado, por defecto 0.
        """
        self.size = size

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

    def area(self):
        """Calcula y devuelve el área actual del cuadrado."""
        return self.__size ** 2

    def my_print(self):
        """Imprime en stdout el cuadrado usando el carácter '#'."""
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__size):
            print("#" * self.__size)
