#!/usr/bin/env python3
"""Módulo que define la clase Rectangle heredando de BaseGeometry."""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectángulo que hereda de BaseGeometry."""

    def __init__(self, width, height):
        """Inicializa una instancia de Rectangle.

        Args:
            width (int): El ancho del rectángulo.
            height (int): La altura del rectángulo.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
