"""
Punto de entrada principal para la aplicación de gestión.
"""
import os
from colorama import Fore, Style, init
from views.menu import menu_inicial, menu_principal
from handlers.empleado_handler import manejar_menu_empleado
from handlers.departamento_handler import manejar_menu_departamento
from handlers.proyecto_handler import manejar_menu_proyecto
from handlers.registro_tiempo_handler import manejar_menu_registro
from handlers.informes_handler import manejar_menu_informes
from handlers.usuario_handler import iniciar_sesion, registrar_usuario

# Inicializar colorama
init(autoreset=True)


def limpiar_parcial():
    """
    Limpia la consola excepto el encabezado.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    mostrar_encabezado()


def mostrar_encabezado():
    """
    Muestra el encabezado con detalles del creador. Este permanece estático.
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}====================================")
    print(f"{Fore.YELLOW}Sistema de Gestión de Proyectos")
    print(f"{Fore.GREEN}Creado por: {Fore.MAGENTA}Christian Gutierrez, Ismael Aguila, Benjamin Velasquez y Jonathan Gallardo")
    print(f"{Fore.CYAN}{Style.BRIGHT}====================================\n")


def main():
    """
    Función principal que gestiona el flujo de la aplicación.
    """
    try:
        # Mostrar encabezado
        os.system('cls' if os.name == 'nt' else 'clear')
        mostrar_encabezado()

        # Menú inicial: autenticación
        while True:
            menu_inicial()
            opcion = input(f"{Fore.YELLOW}Seleccione una opción: {Fore.WHITE}")

            if opcion == "1":
                resultado = iniciar_sesion()
                if resultado["autenticado"]:
                    break
            elif opcion == "2":
                registrar_usuario()
            elif opcion == "3":
                print(f"{Fore.RED}Saliendo del sistema...")
                return
            else:
                print(f"{Fore.RED}Opción no válida. Intente nuevamente.")

        # Menú principal
        while True:
            limpiar_parcial()

            menu_principal()
            opcion = input(f"{Fore.YELLOW}Seleccione una opción: {Fore.WHITE}")

            if opcion == "1":
                manejar_menu_empleado()
            elif opcion == "2":
                manejar_menu_departamento()
            elif opcion == "3":
                manejar_menu_proyecto()
            elif opcion == "4":
                manejar_menu_registro()
            elif opcion == "5":
                manejar_menu_informes()  # Sin restricción de rol
            elif opcion == "6":
                print(f"{Fore.RED}Saliendo del sistema...")
                break
            else:
                print(f"{Fore.RED}Opción no válida. Intente nuevamente.")

    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Saliendo del sistema por interrupción (Ctrl+C)...")
    except Exception as err:
        print(f"{Fore.RED}Ocurrió un error inesperado: {err}")


if __name__ == "__main__":
    main()
