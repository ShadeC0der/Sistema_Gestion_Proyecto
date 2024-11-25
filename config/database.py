"""
Módulo para conexión con MySQL.
"""
import os  # Módulo estándar
from dotenv import load_dotenv  # Librería de terceros
import mysql.connector  # Librería de terceros

# Cargar variables de entorno
load_dotenv()

# Configuración de la base de datos
db_config = {
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'host': os.getenv('DB_HOST', 'localhost'),
    'database': os.getenv('DB_NAME', ''),
    'port': int(os.getenv('DB_PORT', '3306'))
}

# Ejemplo de conexión
def test_connection():
    """
    Prueba la conexión con la base de datos.
    """
    try:
        connection = mysql.connector.connect(**db_config)
        print("Conexión exitosa a la base de datos.")
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")

if __name__ == "__main__":
    test_connection()
