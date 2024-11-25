"""
Punto de entrada principal para la aplicación de gestión.
"""
import mysql.connector
from colorama import Fore, Style, init
from views.menu import menu_principal
from handlers.empleado_handler import manejar_menu_empleado
from handlers.departamento_handler import manejar_menu_departamento
from handlers.proyecto_handler import manejar_menu_proyecto
from handlers.registro_tiempo_handler import manejar_menu_registro
from handlers.informes_handler import manejar_menu_informes
from config.database import db_config

# Inicializar colorama
init(autoreset=True)

def mostrar_mensaje_inicio():
    """
    Muestra un mensaje inicial con detalles del creador.
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}====================================")
    print(f"{Fore.YELLOW}Sistema de Gestión de Proyectos")
    print(f"{Fore.GREEN}Creado por: {Fore.MAGENTA}Christian Gutierrez, Ismael Aguila, Benjamin Velasquez y Jonathan Gallardo")
    print(f"{Fore.CYAN}{Style.BRIGHT}====================================\n")

def verificar_conexion_db():
    """
    Verifica la conexión a la base de datos y muestra el resultado.
    """
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print(f"{Fore.GREEN}Conexión a la base de datos exitosa.")
            print(f"{Fore.CYAN}{Style.BRIGHT}\n====================================")
        connection.close()
    except mysql.connector.Error as err:
        print(f"{Fore.RED}Error al conectar con la base de datos: {err}")
        print(f"{Fore.CYAN}{Style.BRIGHT}\n====================================")

def main():
    """
    Función principal que gestiona el flujo de la aplicación.
    """
    try:
        mostrar_mensaje_inicio()
        verificar_conexion_db()

        while True:
            print(f"{Fore.BLUE}{Style.BRIGHT}")
            menu_principal()
            opcion = input(f"{Fore.YELLOW}Seleccione una opción: ")

            if opcion == "1":
                manejar_menu_empleado()
            elif opcion == "2":
                manejar_menu_departamento()
            elif opcion == "3":
                manejar_menu_proyecto()
            elif opcion == "4":
                manejar_menu_registro()
            elif opcion == "5":
                manejar_menu_informes()
            elif opcion == "6":
                print(f"{Fore.RED}Saliendo del sistema...")
                break
            else:
                print(f"{Fore.RED}Opción no válida. Por favor, intente nuevamente.")
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Saliendo del sistema por interrupción (Ctrl+C)...")

if __name__ == "__main__":
    main()
