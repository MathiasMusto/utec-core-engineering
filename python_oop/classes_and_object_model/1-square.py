#!/usr/bin/env python3
"""Módulo que define una clase Square con un tamaño privado."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size):
        """Inicializa una instancia de Square.

        Args:
            size (int): El tamaño del cuadrado.
        """
        self.__size = size
