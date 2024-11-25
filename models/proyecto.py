"""
Módulo que define la clase Proyecto.

La clase Proyecto representa un proyecto dentro de una organización.
Incluye propiedades y validaciones para sus atributos principales.
"""

from datetime import date

 # pylint: disable=too-many-instance-attributes
class Proyecto:
    """
    Clase que representa un proyecto.

    Atributos:
        proyecto_id (int): Identificador único del proyecto.
        nombre (str): Nombre del proyecto.
        descripcion (str): Descripción detallada del proyecto.
        fecha_inicio (datetime.date): Fecha de inicio del proyecto.
    """

    def __init__(self, proyecto_id=None, nombre="", descripcion="", fecha_inicio=None):
        """
        Inicializa una nueva instancia de la clase Proyecto.

        Args:
            proyecto_id (int, opcional): Identificador único del proyecto. Default es None.
            nombre (str, opcional): Nombre del proyecto. Default es "".
            descripcion (str, opcional): Descripción del proyecto. Default es "".
            fecha_inicio (datetime.date, opcional): Fecha de inicio del proyecto. Default es None.
        """
        self.proyecto_id = proyecto_id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio

    @property
    def proyecto_id(self):
        """Obtiene o establece el ID único del proyecto."""
        return self._proyecto_id

    @proyecto_id.setter
    def proyecto_id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("El proyecto_id debe ser un entero.")
        self._proyecto_id = value

    @property
    def nombre(self):
        """Obtiene o establece el nombre del proyecto."""
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not value.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = value

    @property
    def descripcion(self):
        """Obtiene o establece la descripción del proyecto."""
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value.strip() if value else ""

    @property
    def fecha_inicio(self):
        """Obtiene o establece la fecha de inicio del proyecto."""
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, value):
        if value is not None and not isinstance(value, date):
            raise ValueError("La fecha de inicio debe ser una instancia de datetime.date.")
        self._fecha_inicio = value

    def __repr__(self):
        """
        Representa la instancia de la clase como una cadena.

        Returns:
            str: Representación de la instancia de Proyecto.
        """
        return (f"Proyecto(proyecto_id={self.proyecto_id}, nombre='{self.nombre}', "
                f"descripcion='{self.descripcion}', fecha_inicio={self.fecha_inicio})")
