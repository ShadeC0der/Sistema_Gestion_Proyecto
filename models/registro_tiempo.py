"""
Módulo que define la clase RegistroDeTiempo.

La clase RegistroDeTiempo representa un registro de las horas trabajadas
por un empleado en un proyecto.
Incluye propiedades y validaciones para sus atributos principales.
"""

from datetime import date


class RegistroDeTiempo:
    """
    Clase que representa un registro de tiempo.

    Atributos:
        registro_id (int): Identificador único del registro.
        fecha (datetime.date): Fecha del registro.
        horas_trabajadas (float): Número de horas trabajadas.
        descripcion (str): Descripción del registro.
        empleado_id (int): Identificador del empleado asociado al registro.
    """

    def __init__(self, registro_id=None, fecha=None, horas_trabajadas=0.0, 
                 descripcion="", empleado_id=None):
        """
        Inicializa una nueva instancia de la clase RegistroDeTiempo.

        Args:
            registro_id (int, opcional): Identificador único del registro. Default es None.
            fecha (datetime.date, opcional): Fecha del registro. Default es None.
            horas_trabajadas (float, opcional): Número de horas trabajadas. Default es 0.0.
            descripcion (str, opcional): Descripción del registro. Default es "".
            empleado_id (int, opcional): Identificador del empleado asociado. Default es None.
        """
        self.registro_id = registro_id
        self.fecha = fecha
        self.horas_trabajadas = horas_trabajadas
        self.descripcion = descripcion
        self.empleado_id = empleado_id

    @property
    def registro_id(self):
        """Obtiene o establece el ID único del registro."""
        return self._registro_id

    @registro_id.setter
    def registro_id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("El registro_id debe ser un entero.")
        self._registro_id = value

    @property
    def fecha(self):
        """Obtiene o establece la fecha del registro."""
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        if value is not None and not isinstance(value, date):
            raise ValueError("La fecha debe ser una instancia de datetime.date.")
        self._fecha = value

    @property
    def horas_trabajadas(self):
        """Obtiene o establece las horas trabajadas."""
        return self._horas_trabajadas

    @horas_trabajadas.setter
    def horas_trabajadas(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Las horas trabajadas deben ser un número positivo.")
        self._horas_trabajadas = value

    @property
    def descripcion(self):
        """Obtiene o establece la descripción del registro."""
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value.strip() if value else ""

    @property
    def empleado_id(self):
        """Obtiene o establece el ID del empleado asociado."""
        return self._empleado_id

    @empleado_id.setter
    def empleado_id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("El empleado_id debe ser un entero.")
        self._empleado_id = value

    def __repr__(self):
        """
        Representa la instancia de la clase como una cadena.

        Returns:
            str: Representación de la instancia de RegistroDeTiempo.
        """
        return (f"RegistroDeTiempo(registro_id={self.registro_id}, fecha={self.fecha}, "
                f"horas_trabajadas={self.horas_trabajadas}, descripcion='{self.descripcion}', "
                f"empleado_id={self.empleado_id})")
