"""
Controlador para manejar las operaciones CRUD relacionadas con la tabla Proyecto.
"""

import mysql.connector
from mysql.connector import Error
from models.proyecto import Proyecto
from config.database import db_config


class ProyectoController:
    """
    Controlador para gestionar proyectos en la base de datos.
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

    def crear_proyecto(self, proyecto):
        """
        Crea un nuevo proyecto en la base de datos.
        Args:
            proyecto (Proyecto): Objeto Proyecto con los datos a insertar.
        """
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    # pylint: disable=line-too-long
                    query = "INSERT INTO proyecto (nombre, descripcion, fecha_inicio) VALUES (%s, %s, %s)"
                    cursor.execute(query, (proyecto.nombre, proyecto.descripcion, proyecto.fecha_inicio))
                    connection.commit()
        except Error as e:
            print(f"Error al crear proyecto: {e}")

    def listar_proyectos(self):
        """
        Obtiene una lista de todos los proyectos.
        Returns:
            list[Proyecto]: Lista de objetos Proyecto.
        """
        proyectos = []
        try:
            with self.conectar() as connection:
                with connection.cursor(dictionary=True) as cursor:
                    query = "SELECT * FROM proyecto"
                    cursor.execute(query)
                    resultados = cursor.fetchall()
                    for row in resultados:
                        proyectos.append(
                            Proyecto(
                                proyecto_id=row["proyecto_id"],
                                nombre=row["nombre"],
                                descripcion=row["descripcion"],
                                fecha_inicio=row["fecha_inicio"]
                            )
                        )
        except Error as e:
            print(f"Error al listar proyectos: {e}")
        return proyectos

    def buscar_proyecto_por_id(self, proyecto_id):
        """
        Busca un proyecto por su ID.
        Args:
            proyecto_id (int): ID del proyecto a buscar.
        Returns:
            Proyecto | None: Objeto Proyecto si se encuentra, None si no.
        """
        try:
            with self.conectar() as connection:
                with connection.cursor(dictionary=True) as cursor:
                    query = "SELECT * FROM proyecto WHERE proyecto_id = %s"
                    cursor.execute(query, (proyecto_id,))
                    row = cursor.fetchone()
                    if row:
                        return Proyecto(
                            proyecto_id=row["proyecto_id"],
                            nombre=row["nombre"],
                            descripcion=row["descripcion"],
                            fecha_inicio=row["fecha_inicio"]
                        )
        except Error as e:
            print(f"Error al buscar proyecto: {e}")
        return None

    def modificar_proyecto(self, proyecto):
        """
        Actualiza los datos de un proyecto existente. Solo se modifican
        los campos proporcionados por el usuario, manteniendo los valores actuales para los demás.

        Args:
            proyecto (Proyecto): Objeto Proyecto con los datos a modificar.
        """
        try:
            with self.conectar() as connection:
                with connection.cursor(dictionary=True) as cursor:
                    # Obtener los valores actuales del proyecto
                    query_select = "SELECT * FROM proyecto WHERE proyecto_id = %s"
                    cursor.execute(query_select, (proyecto.proyecto_id,))
                    row = cursor.fetchone()

                    if not row:
                        print(f"El proyecto con ID {proyecto.proyecto_id} no existe.")
                        return

                    # Combinar los datos existentes con los nuevos (los campos en None se conservan)
                    nombre = proyecto.nombre or row["nombre"]
                    descripcion = proyecto.descripcion or row["descripcion"]
                    fecha_inicio = proyecto.fecha_inicio or row["fecha_inicio"]

                    # Actualizar el proyecto
                    query_update = """
                    UPDATE proyecto 
                    SET nombre = %s, descripcion = %s, fecha_inicio = %s 
                    WHERE proyecto_id = %s
                    """
                    # pylint: disable=line-too-long
                    cursor.execute(query_update, (nombre, descripcion, fecha_inicio, proyecto.proyecto_id))
                    connection.commit()
                    print(f"Proyecto con ID {proyecto.proyecto_id} actualizado exitosamente.")
        except Error as e:
            print(f"Error al modificar proyecto: {e}")

    def eliminar_proyecto(self, proyecto_id):
        """
        Elimina un proyecto de la base de datos.
        Args:
            proyecto_id (int): ID del proyecto a eliminar.
        """
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    query = "DELETE FROM proyecto WHERE proyecto_id = %s"
                    cursor.execute(query, (proyecto_id,))
                    connection.commit()
                    print(f"Proyecto con ID {proyecto_id} eliminado exitosamente.")
        except Error as e:
            print(f"Error al eliminar proyecto: {e}")
