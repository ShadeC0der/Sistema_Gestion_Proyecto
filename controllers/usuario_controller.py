"""
Controlador para la gestión de usuarios en el sistema.
"""
import bcrypt
import mysql.connector
from config.database import db_config
from models.usuario import Usuario


class UsuarioController:
    """
    Controlador para gestionar los usuarios del sistema, incluyendo autenticación y creación.
    """

    def __init__(self):
        """
        Inicializa el controlador con la configuración de la base de datos.
        """
        self.db_config = db_config

    def conectar(self):
        """
        Establece la conexión a la base de datos.

        Returns:
            connection: Objeto de conexión a la base de datos.
        """
        return mysql.connector.connect(**self.db_config)

    def crear_usuario(self, nombre_usuario, password, rol="empleado"):
        """
        Crea un nuevo usuario con una contraseña hasheada.

        Args:
            nombre_usuario (str): Nombre de usuario único.
            password (str): Contraseña en texto plano.
            rol (str): Rol del usuario ('admin' o 'empleado'). Por defecto es 'empleado'.

        Raises:
            mysql.connector.Error: Error en la ejecución de la consulta SQL.
        """
        password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        connection = self.conectar()
        cursor = connection.cursor()
        query = """
            INSERT INTO usuarios (nombre_usuario, password_hash, rol)
            VALUES (%s, %s, %s)
        """
        try:
            cursor.execute(query, (nombre_usuario, password_hash.decode("utf-8"), rol))
            connection.commit()
            print(f"Usuario '{nombre_usuario}' creado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al crear el usuario: {err}")
        finally:
            cursor.close()
            connection.close()

    def autenticar_usuario(self, nombre_usuario, password):
        """
        Autentica a un usuario verificando la contraseña.

        Args:
            nombre_usuario (str): Nombre del usuario.
            password (str): Contraseña en texto plano.

        Returns:
            dict: Un diccionario con el estado de autenticación y el rol del usuario.
        """
        connection = self.conectar()
        cursor = connection.cursor()
        query = """
            SELECT usuario_id, password_hash, rol FROM usuarios
            WHERE nombre_usuario = %s
        """
        try:
            cursor.execute(query, (nombre_usuario,))
            resultado = cursor.fetchone()
            if resultado:
                usuario_id, password_hash, rol = resultado
                if bcrypt.checkpw(password.encode("utf-8"), password_hash.encode("utf-8")):
                    return {"autenticado": True, "usuario": Usuario(usuario_id, nombre_usuario, password_hash, rol)}
            return {"autenticado": False}
        except mysql.connector.Error as err:
            print(f"Error durante la autenticación: {err}")
            return {"autenticado": False}
        finally:
            cursor.close()
            connection.close()
