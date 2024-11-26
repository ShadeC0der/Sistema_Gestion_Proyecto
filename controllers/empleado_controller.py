"""
Controlador para manejar las operaciones CRUD relacionadas con la tabla Empleado.
"""

import mysql.connector
from mysql.connector import Error
from models.empleado import Empleado
from config.database import db_config


class EmpleadoController:
    """
    Controlador para gestionar empleados en la base de datos.
    """

    def __init__(self):
        self.db_config = db_config

    def conectar(self):
        """
        Establece una conexión con la base de datos.
        Returns:
            mysql.connector.connection.MySQLConnection: Conexión activa.
        """
        return mysql.connector.connect(**self.db_config)

    def crear_empleado(self, empleado):
        """
        Crea un nuevo empleado en la base de datos.
        Args:
            empleado (Empleado): Objeto Empleado con los datos a insertar.
        """
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    query = """
                        INSERT INTO empleado 
                        (rut, nombre, direccion, telefono, email, fecha_inicio, salario, departamento_id) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(query, (
                        empleado.rut, empleado.nombre, empleado.direccion,
                        empleado.telefono, empleado.email, empleado.fecha_inicio,
                        empleado.salario, empleado.departamento_id
                    ))
                    connection.commit()
                    print("Empleado creado exitosamente.")
        except Error as e:
            if "FOREIGN KEY" in str(e):
                print(f"Error: El departamento con ID {empleado.departamento_id} no existe.")
            else:
                print(f"Error al crear empleado: {e}")

    def listar_empleados(self):
        """
        Obtiene una lista de todos los empleados.
        Returns:
            list[Empleado]: Lista de objetos Empleado.
        """
        empleados = []
        try:
            with self.conectar() as connection:
                with connection.cursor(dictionary=True) as cursor:
                    query = "SELECT * FROM empleado"
                    cursor.execute(query)
                    resultados = cursor.fetchall()
                    for row in resultados:
                        empleados.append(
                            Empleado(
                                empleado_id=row["empleado_id"],
                                rut=row["rut"],
                                nombre=row["nombre"],
                                direccion=row["direccion"],
                                telefono=row["telefono"],
                                email=row["email"],
                                fecha_inicio=row["fecha_inicio"],
                                salario=row["salario"],
                                departamento_id=row["departamento_id"]
                            )
                        )
        except Error as e:
            print(f"Error al listar empleados: {e}")
        return empleados

    def buscar_empleado_por_rut(self, rut):
        """
        Busca un empleado por su RUT.
        Args:
            rut (str): RUT del empleado a buscar.
        Returns:
            Empleado | None: Objeto Empleado si se encuentra, None si no.
        """
        try:
            with self.conectar() as connection:
                with connection.cursor(dictionary=True) as cursor:
                    query = "SELECT * FROM empleado WHERE rut = %s"
                    cursor.execute(query, (rut,))
                    row = cursor.fetchone()
                    if row:
                        return Empleado(
                            empleado_id=row["empleado_id"],
                            rut=row["rut"],
                            nombre=row["nombre"],
                            direccion=row["direccion"],
                            telefono=row["telefono"],
                            email=row["email"],
                            fecha_inicio=row["fecha_inicio"],
                            salario=row["salario"],
                            departamento_id=row["departamento_id"]
                        )
        except Error as e:
            print(f"Error al buscar empleado: {e}")
        return None

    def modificar_empleado(self, empleado):
        """
        Actualiza los datos de un empleado existente. Solo se modifican
        los campos proporcionados por el usuario, manteniendo los valores actuales para los demás.

        Args:
            empleado (Empleado): Objeto Empleado con los datos a modificar.
        """
        try:
            with self.conectar() as connection:
                with connection.cursor(dictionary=True) as cursor:
                    query_select = "SELECT * FROM empleado WHERE rut = %s"
                    cursor.execute(query_select, (empleado.rut,))
                    row = cursor.fetchone()

                    if not row:
                        print(f"El empleado con RUT {empleado.rut} no existe.")
                        return

                    nombre = empleado.nombre or row["nombre"]
                    direccion = empleado.direccion or row["direccion"]
                    telefono = empleado.telefono or row["telefono"]
                    email = empleado.email or row["email"]
                    fecha_inicio = empleado.fecha_inicio or row["fecha_inicio"]
                    salario = empleado.salario if empleado.salario is not None else row["salario"]
                    departamento_id = empleado.departamento_id if empleado.departamento_id is not None else row["departamento_id"]

                    query_update = """
                    UPDATE empleado 
                    SET nombre = %s, direccion = %s, telefono = %s, email = %s, 
                        fecha_inicio = %s, salario = %s, departamento_id = %s 
                    WHERE rut = %s
                    """
                    cursor.execute(query_update, (nombre, direccion, telefono, email, fecha_inicio,
                                                  salario, departamento_id, empleado.rut))
                    connection.commit()
                    print(f"Empleado con RUT {empleado.rut} actualizado exitosamente.")
        except Error as e:
            print(f"Error al modificar empleado: {e}")

    def eliminar_empleado(self, rut):
        """
        Elimina un empleado de la base de datos.
        Args:
            rut (str): RUT del empleado a eliminar.
        """
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    query = "DELETE FROM empleado WHERE rut = %s"
                    cursor.execute(query, (rut,))
                    connection.commit()
                    print(f"Empleado con RUT {rut} eliminado exitosamente.")
        except Error as e:
            print(f"Error al eliminar empleado: {e}")
