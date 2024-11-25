"""
Controlador para manejar las operaciones CRUD relacionadas con la tabla Departamento.
"""

import mysql.connector
from mysql.connector import Error
from models.departamento import Departamento
from config.database import db_config


class DepartamentoController:
    """
    Controlador para gestionar departamentos en la base de datos.
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

    def crear_departamento(self, departamento):
        """
        Crea un nuevo departamento en la base de datos.
        Args:
            departamento (Departamento): Objeto Departamento con los datos a insertar.
        """
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    query = "INSERT INTO departamento (nombre, gerente_id) VALUES (%s, %s)"
                    cursor.execute(query, (departamento.nombre, departamento.gerente_id))
                    connection.commit()
        except Error as e:
            print(f"Error al crear departamento: {e}")

    def listar_departamentos(self):
        """
        Obtiene una lista de todos los departamentos.
        Returns:
            list[Departamento]: Lista de objetos Departamento.
        """
        departamentos = []
        try:
            with self.conectar() as connection:
                with connection.cursor(dictionary=True) as cursor:
                    query = "SELECT * FROM departamento"
                    cursor.execute(query)
                    resultados = cursor.fetchall()
                    for row in resultados:
                        departamentos.append(
                            Departamento(
                                departamento_id=row["departamento_id"],
                                nombre=row["nombre"],
                                gerente_id=row["gerente_id"]
                            )
                        )
        except Error as e:
            print(f"Error al listar departamentos: {e}")
        return departamentos

    def buscar_departamento_por_id(self, departamento_id):
        """
        Busca un departamento por su ID.
        Args:
            departamento_id (int): ID del departamento a buscar.
        Returns:
            Departamento | None: Objeto Departamento si se encuentra, None si no.
        """
        try:
            with self.conectar() as connection:
                with connection.cursor(dictionary=True) as cursor:
                    query = "SELECT * FROM departamento WHERE departamento_id = %s"
                    cursor.execute(query, (departamento_id,))
                    row = cursor.fetchone()
                    if row:
                        return Departamento(
                            departamento_id=row["departamento_id"],
                            nombre=row["nombre"],
                            gerente_id=row["gerente_id"]
                        )
        except Error as e:
            print(f"Error al buscar departamento: {e}")
        return None

    def modificar_departamento(self, departamento):
        """
        Actualiza los datos de un departamento existente. Solo se modifican
        los campos proporcionados por el usuario, manteniendo los valores actuales para los demás.
        
        Args:
            departamento (Departamento): Objeto Departamento con los datos a modificar. 
                Los valores en None se conservan.
        """
        try:
            with self.conectar() as connection:
                with connection.cursor(dictionary=True) as cursor:
                    # Obtener los valores actuales del departamento
                    query_select = "SELECT * FROM departamento WHERE departamento_id = %s"
                    cursor.execute(query_select, (departamento.departamento_id,))
                    row = cursor.fetchone()

                    if not row:
                        print(f"El departamento con ID {departamento.departamento_id} no existe.")
                        return

                    # Combinar los datos existentes con los nuevos (los campos en None se conservan)
                    nombre = departamento.nombre or row["nombre"]
                    # pylint: disable=line-too-long
                    gerente_id = departamento.gerente_id if departamento.gerente_id is not None else row["gerente_id"]

                    # Actualizar el departamento
                    query_update = """
                    UPDATE departamento 
                    SET nombre = %s, gerente_id = %s 
                    WHERE departamento_id = %s
                    """
                    cursor.execute(query_update, (nombre, gerente_id, departamento.departamento_id))
                    connection.commit()
                    # pylint: disable=line-too-long
                    print(f"Departamento con ID {departamento.departamento_id} actualizado exitosamente.")
        except Error as e:
            print(f"Error al modificar departamento: {e}")

    def eliminar_departamento(self, departamento_id):
        """
        Elimina un departamento de la base de datos.
        Args:
            departamento_id (int): ID del departamento a eliminar.
        """
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    query = "DELETE FROM departamento WHERE departamento_id = %s"
                    cursor.execute(query, (departamento_id,))
                    connection.commit()
        except Error as e:
            print(f"Error al eliminar departamento: {e}")
