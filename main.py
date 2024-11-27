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
from handlers.indicadores_handler import manejar_menu_indicadores
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
    print(f"{Fore.CYAN}{Style.BRIGHT}{'=' * 36}")
    print(f"{Fore.YELLOW}     Sistema de Gestión de Proyectos")
    print(f"{Fore.GREEN}       Creado por: {Fore.MAGENTA}Christian Gutierrez")
    print(f"{Fore.CYAN}{Style.BRIGHT}{'=' * 36}{Style.RESET_ALL}\n")


def main():
    """
    Función principal que gestiona el flujo de la aplicación.
    """
    try:
        # Mostrar encabezado
        os.system('cls' if os.name == 'nt' else 'clear')
        mostrar_encabezado()

        # Menú inicial: autenticación
        usuario_actual = None
        while True:
            menu_inicial()
            opcion = input(f"{Fore.YELLOW}Seleccione una opción: {Style.RESET_ALL}")

            if opcion == "1":
                resultado = iniciar_sesion()
                if resultado["autenticado"]:
                    usuario_actual = resultado["usuario"]
                    break
            elif opcion == "2":
                registrar_usuario()
            elif opcion == "3":
                print(f"{Fore.RED}Saliendo del sistema...{Style.RESET_ALL}")
                return
            else:
                print(f"{Fore.RED}Opción no válida. Intente nuevamente.{Style.RESET_ALL}")

        # Menú principal
        while True:
            limpiar_parcial()

            menu_principal()
            opcion = input(f"{Fore.YELLOW}Seleccione una opción: {Style.RESET_ALL}")

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
                manejar_menu_indicadores(usuario_actual.usuario_id)  # Pasar usuario_id correctamente
            elif opcion == "7":
                print(f"{Fore.RED}Saliendo del sistema...{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.RED}Opción no válida. Intente nuevamente.{Style.RESET_ALL}")

    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Saliendo del sistema por interrupción (Ctrl+C)...{Style.RESET_ALL}")
    except Exception as err:
        print(f"{Fore.RED}Ocurrió un error inesperado: {err}{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
