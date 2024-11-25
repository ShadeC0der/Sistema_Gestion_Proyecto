"""
Módulo que define la clase Empleado.

La clase Empleado representa un empleado de una organización.
Incluye propiedades y validaciones para sus atributos principales.
"""

from datetime import date

 # pylint: disable=too-many-instance-attributes
class Empleado:
    """
    Clase que representa a un empleado.

    Atributos:
        empleado_id (int): Identificador único del empleado.
        rut (str): Identificación única del empleado (ejemplo: '12345678-9').
        nombre (str): Nombre completo del empleado.
        direccion (str): Dirección del empleado.
        telefono (str): Teléfono del empleado.
        email (str): Correo electrónico del empleado.
        fecha_inicio (datetime.date): Fecha de inicio en la empresa.
        salario (float): Salario del empleado.
        departamento_id (int): ID del departamento asociado.
    """

    # pylint: disable=too-many-arguments
    def __init__(self, empleado_id=None, rut="", nombre="", direccion="", telefono="",
                 email="", fecha_inicio=None, salario=0.0, departamento_id=None):
        """
        Inicializa una nueva instancia de la clase Empleado.

        Args:
            empleado_id (int, opcional): Identificador único del empleado. Default es None.
            rut (str, opcional): Identificación única del empleado (ejemplo: '12345678-9').
            nombre (str, opcional): Nombre completo del empleado. Default es "".
            direccion (str, opcional): Dirección del empleado. Default es "".
            telefono (str, opcional): Teléfono del empleado. Default es "".
            email (str, opcional): Correo electrónico del empleado. Default es "".
            fecha_inicio (datetime.date, opcional): Fecha de inicio en la empresa. Default es None.
            salario (float, opcional): Salario del empleado. Default es 0.0.
            departamento_id (int, opcional): ID del departamento asociado. Default es None.
        """
        self.empleado_id = empleado_id
        self.rut = rut
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.fecha_inicio = fecha_inicio
        self.salario = salario
        self.departamento_id = departamento_id

    @property
    def empleado_id(self):
        """Obtiene o establece el ID único del empleado."""
        return self._empleado_id

    @empleado_id.setter
    def empleado_id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("El empleado_id debe ser un entero.")
        self._empleado_id = value

    @property
    def rut(self):
        """Obtiene o establece el RUT del empleado."""
        return self._rut

    @rut.setter
    def rut(self, value):
        if not value:
            raise ValueError("El rut no puede estar vacío.")
        self._rut = value

    @property
    def nombre(self):
        """Obtiene o establece el nombre del empleado."""
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not value.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = value

    @property
    def salario(self):
        """Obtiene o establece el salario del empleado."""
        return self._salario

    @salario.setter
    def salario(self, value):
        if value < 0:
            raise ValueError("El salario no puede ser negativo.")
        self._salario = value

    @property
    def fecha_inicio(self):
        """Obtiene o establece la fecha de inicio del empleado."""
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
            str: Representación de la instancia de Empleado.
        """
        return (f"Empleado(empleado_id={self.empleado_id},rut='{self.rut}',nombre='{self.nombre}', "
                f"salario={self.salario}, departamento_id={self.departamento_id})")
