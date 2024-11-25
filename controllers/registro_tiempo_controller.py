"""
Controlador para manejar las operaciones CRUD relacionadas con la tabla RegistroDeTiempo.
"""

import mysql.connector
from mysql.connector import Error
from models.registro_tiempo import RegistroDeTiempo
from config.database import db_config


class RegistroDeTiempoController:
    """
    Controlador para gestionar registros de tiempo en la base de datos.
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

    def crear_registro(self, registro):
        """
        Crea un nuevo registro de tiempo en la base de datos.
        Args:
            registro (RegistroDeTiempo): Objeto RegistroDeTiempo con los datos a insertar.
        """
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    # pylint: disable=line-too-long
                    query = ("INSERT INTO registro_de_tiempo (fecha, horas_trabajadas, descripcion, empleado_id) "
                             "VALUES (%s, %s, %s, %s)")
                    cursor.execute(query, (registro.fecha, registro.horas_trabajadas, registro.descripcion, registro.empleado_id))
                    connection.commit()
        except Error as e:
            print(f"Error al crear registro de tiempo: {e}")

    def listar_registros(self):
        """
        Obtiene una lista de todos los registros de tiempo.
        Returns:
            list[RegistroDeTiempo]: Lista de objetos RegistroDeTiempo.
        """
        registros = []
        try:
            with self.conectar() as connection:
                with connection.cursor(dictionary=True) as cursor:
                    query = "SELECT * FROM registro_de_tiempo"
                    cursor.execute(query)
                    resultados = cursor.fetchall()
                    for row in resultados:
                        registros.append(
                            RegistroDeTiempo(
                                registro_id=row["registro_id"],
                                fecha=row["fecha"],
                                horas_trabajadas=row["horas_trabajadas"],
                                descripcion=row["descripcion"],
                                empleado_id=row["empleado_id"]
                            )
                        )
        except Error as e:
            print(f"Error al listar registros de tiempo: {e}")
        return registros

    def buscar_registro_por_id(self, registro_id):
        """
        Busca un registro de tiempo por su ID.
        Args:
            registro_id (int): ID del registro a buscar.
        Returns:
            RegistroDeTiempo | None: Objeto RegistroDeTiempo si se encuentra, None si no.
        """
        try:
            with self.conectar() as connection:
                with connection.cursor(dictionary=True) as cursor:
                    query = "SELECT * FROM registro_de_tiempo WHERE registro_id = %s"
                    cursor.execute(query, (registro_id,))
                    row = cursor.fetchone()
                    if row:
                        return RegistroDeTiempo(
                            registro_id=row["registro_id"],
                            fecha=row["fecha"],
                            horas_trabajadas=row["horas_trabajadas"],
                            descripcion=row["descripcion"],
                            empleado_id=row["empleado_id"]
                        )
        except Error as e:
            print(f"Error al buscar registro de tiempo: {e}")
        return None

    def modificar_registro(self, registro):
        """
        Actualiza los datos de un registro de tiempo existente. Solo se modifican
        los campos proporcionados por el usuario, manteniendo los valores actuales para los demás.

        Args:
            registro (RegistroDeTiempo): Objeto RegistroDeTiempo con los datos a modificar.
        """
        try:
            with self.conectar() as connection:
                with connection.cursor(dictionary=True) as cursor:
                    # Obtener los valores actuales del registro
                    query_select = "SELECT * FROM registro_de_tiempo WHERE registro_id = %s"
                    cursor.execute(query_select, (registro.registro_id,))
                    row = cursor.fetchone()

                    if not row:
                        print(f"El registro con ID {registro.registro_id} no existe.")
                        return
                    # pylint: disable=line-too-long
                    # Combinar los datos existentes con los nuevos (los campos en None se conservan)
                    fecha = registro.fecha or row["fecha"]
                    horas_trabajadas = registro.horas_trabajadas if registro.horas_trabajadas is not None else row["horas_trabajadas"]
                    descripcion = registro.descripcion or row["descripcion"]
                    empleado_id = registro.empleado_id if registro.empleado_id is not None else row["empleado_id"]

                    # Actualizar el registro
                    query_update = """
                    UPDATE registro_de_tiempo 
                    SET fecha = %s, horas_trabajadas = %s, descripcion = %s, empleado_id = %s 
                    WHERE registro_id = %s
                    """
                    cursor.execute(query_update, (fecha, horas_trabajadas, descripcion, empleado_id, registro.registro_id))
                    connection.commit()
                    print(f"Registro de tiempo con ID {registro.registro_id} actualizado exitosamente.")
        except Error as e:
            print(f"Error al modificar registro de tiempo: {e}")

    def eliminar_registro(self, registro_id):
        """
        Elimina un registro de tiempo de la base de datos.
        Args:
            registro_id (int): ID del registro a eliminar.
        """
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    query = "DELETE FROM registro_de_tiempo WHERE registro_id = %s"
                    cursor.execute(query, (registro_id,))
                    connection.commit()
                    print(f"Registro de tiempo con ID {registro_id} eliminado exitosamente.")
        except Error as e:
            print(f"Error al eliminar registro de tiempo: {e}")
