#!/usr/init/env python3
#!/usr/bin/env python3
"""Módulo que define la clase BaseGeometry."""


class BaseGeometry:
    """Representa una geometría base."""

    def area(self):
        """Método que calcula el área (aún no implementado)."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valida que un valor sea un entero positivo mayor que 0.

        Args:
            name (str): El nombre del valor/parámetro.
            value (int): El valor a validar.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
