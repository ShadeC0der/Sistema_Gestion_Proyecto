"""
Módulo que define la clase Departamento.

La clase Departamento representa un departamento dentro de una organización.
Incluye propiedades y validaciones para sus atributos principales.
"""


class Departamento:
    """
    Clase que representa un departamento.

    Atributos:
        departamento_id (int): Identificador único del departamento.
        nombre (str): Nombre del departamento.
        gerente_id (int): ID del gerente asociado al departamento.
    """

    def __init__(self, departamento_id=None, nombre="", gerente_id=None):
        """
        Inicializa una nueva instancia de la clase Departamento.

        Args:
            departamento_id (int, opcional): Identificador único del departamento. Default es None.
            nombre (str, opcional): Nombre del departamento. Default es "".
            gerente_id (int, opcional): ID del gerente asociado. Default es None.
        """
        self.departamento_id = departamento_id
        self.nombre = nombre
        self.gerente_id = gerente_id

    @property
    def departamento_id(self):
        """Obtiene o establece el ID único del departamento."""
        return self._departamento_id

    @departamento_id.setter
    def departamento_id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("El departamento_id debe ser un entero.")
        self._departamento_id = value

    @property
    def nombre(self):
        """Obtiene o establece el nombre del departamento."""
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not value.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = value

    @property
    def gerente_id(self):
        """Obtiene o establece el ID del gerente asociado."""
        return self._gerente_id

    @gerente_id.setter
    def gerente_id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("El gerente_id debe ser un entero.")
        self._gerente_id = value

    def __repr__(self):
        """
        Representa la instancia de la clase como una cadena.

        Returns:
            str: Representación de la instancia de Departamento.
        """
        return (f"Departamento(departamento_id={self.departamento_id}, "
                f"nombre='{self.nombre}', gerente_id={self.gerente_id})")
