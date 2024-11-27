"""
Controlador para gestionar la consulta y el registro de indicadores económicos.
"""

from datetime import datetime
import requests
import mysql.connector
from mysql.connector import Error
from config.database import db_config


class IndicadoresController:
    """
    Clase para consultar indicadores económicos desde una API externa
    y registrar los resultados en la base de datos.
    """

    def __init__(self):
        self.api_url = "https://mindicador.cl/api"  # URL de la API
        self.db_config = db_config

    def conectar(self):
        """
        Establece una conexión con la base de datos.
        Returns:
            mysql.connector.connection.MySQLConnection: Conexión activa.
        """
        return mysql.connector.connect(**self.db_config)

    def consultar_indicador(self, indicador, fecha_inicio=None, fecha_fin=None):
        """
        Consulta un indicador económico desde la API.

        Args:
            indicador (str): Nombre del indicador a consultar (ej. "uf", "dolar", "euro").
            fecha_inicio (str): Fecha de inicio en formato 'YYYY-MM-DD' (opcional).
            fecha_fin (str): Fecha de fin en formato 'YYYY-MM-DD' (opcional).

        Returns:
            list: Datos del indicador o lista vacía si ocurre un error.
        """
        try:
            url = f"{self.api_url}/{indicador}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            datos = response.json().get("serie", [])

            # Filtrar por fechas si se proporcionan
            if fecha_inicio and fecha_fin:
                fecha_inicio_dt = datetime.strptime(fecha_inicio, '%Y-%m-%d')
                fecha_fin_dt = datetime.strptime(fecha_fin, '%Y-%m-%d')
                datos_filtrados = [
                    dato for dato in datos
                    if fecha_inicio_dt <= datetime.strptime(dato["fecha"][:10], '%Y-%m-%d') <= fecha_fin_dt
                ]
                return datos_filtrados
            else:
                return datos
        except requests.RequestException as e:
            print(f"Error al consultar el indicador: {e}")
            return []

    def registrar_indicador(self, datos, indicador, usuario_id, url_fuente):
        """
        Registra los datos de un indicador económico en la base de datos.

        Args:
            datos (list): Lista de datos del indicador a registrar.
            indicador (str): Nombre del indicador.
            usuario_id (int): ID del usuario que realiza el registro.
            url_fuente (str): URL del sitio de donde provienen los datos.
        """
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    query = """
                    INSERT INTO registro_indicadores
                    (nombre_indicador, fecha_valor, valor, fecha_consulta, usuario_id, url_fuente)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """
                    fecha_consulta = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    for dato in datos:
                        cursor.execute(query, (
                            indicador,
                            dato["fecha"][:10],
                            dato["valor"],
                            fecha_consulta,
                            usuario_id,  # Asegurarse de que usuario_id es un entero
                            url_fuente
                        ))
                    connection.commit()
                    print("Registro de indicador guardado exitosamente.")
        except Error as e:
            print(f"Error al registrar el indicador en la base de datos: {e}")

    def listar_indicadores_registrados(self):
        """
        Lista los indicadores económicos registrados en la base de datos.

        Returns:
            list[dict]: Lista de indicadores registrados.
        """
        try:
            with self.conectar() as connection:
                with connection.cursor(dictionary=True) as cursor:
                    query = "SELECT * FROM registro_indicadores"
                    cursor.execute(query)
                    return cursor.fetchall()
        except Error as e:
            print(f"Error al listar indicadores registrados: {e}")
            return []

    def eliminar_registro_indicador(self, registro_id):
        """
        Elimina un registro de indicador económico por su ID.

        Args:
            registro_id (int): ID del registro a eliminar.
        """
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    query = "DELETE FROM registro_indicadores WHERE id = %s"
                    cursor.execute(query, (registro_id,))
                    connection.commit()
                    print(f"Registro con ID {registro_id} eliminado exitosamente.")
        except Error as e:
            print(f"Error al eliminar el registro del indicador: {e}")
