"""
Handler para gestionar el menú de generación de informes.
"""

import os
from datetime import datetime
from controllers.informes_controller import InformesController
from views.menu import menu_informes

informes_controller = InformesController()


def crear_carpeta_informes():
    """
    Crea una carpeta para almacenar los informes si no existe.
    """
    carpeta = "informes_generados"
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    return carpeta


def mostrar_encabezado(titulo):
    """
    Muestra un encabezado decorativo para las secciones.
    Args:
        titulo (str): Título del encabezado.
    """
    print("\n" + "*" * 40)
    print(f"{titulo.center(40)}")
    print("*" * 40)


def generar_informe_empleados():
    """
    Genera un informe de empleados en Excel.
    """
    mostrar_encabezado("GENERAR INFORME DE EMPLEADOS")
    carpeta = crear_carpeta_informes()
    archivo = os.path.join(carpeta, f"informe_empleados_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx")
    informes_controller.generar_informe_empleados(archivo)
    print(f"Informe de empleados generado exitosamente en '{archivo}'.")


def generar_informe_departamentos():
    """
    Genera un informe de departamentos en Excel.
    """
    mostrar_encabezado("GENERAR INFORME DE DEPARTAMENTOS")
    carpeta = crear_carpeta_informes()
    archivo = os.path.join(carpeta, f"informe_departamentos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx")
    informes_controller.generar_informe_departamentos(archivo)
    print(f"Informe de departamentos generado exitosamente en '{archivo}'.")


def generar_informe_proyectos():
    """
    Genera un informe de proyectos en Excel.
    """
    mostrar_encabezado("GENERAR INFORME DE PROYECTOS")
    carpeta = crear_carpeta_informes()
    archivo = os.path.join(carpeta, f"informe_proyectos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx")
    informes_controller.generar_informe_proyectos(archivo)
    print(f"Informe de proyectos generado exitosamente en '{archivo}'.")


def generar_informe_registros_tiempo():
    """
    Genera un informe de registros de tiempo en Excel.
    """
    mostrar_encabezado("GENERAR INFORME DE REGISTROS DE TIEMPO")
    carpeta = crear_carpeta_informes()
    archivo = os.path.join(carpeta, f"informe_registros_tiempo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx")
    informes_controller.generar_informe_registros_tiempo(archivo)
    print(f"Informe de registros de tiempo generado exitosamente en '{archivo}'.")


def manejar_menu_informes():
    """
    Maneja el menú de generación de informes.
    """
    while True:
        menu_informes()
        sub_opcion = input("Seleccione una opción: ").strip()

        if sub_opcion == "5.1":
            generar_informe_empleados()
        elif sub_opcion == "5.2":
            generar_informe_departamentos()
        elif sub_opcion == "5.3":
            generar_informe_proyectos()
        elif sub_opcion == "5.4":
            generar_informe_registros_tiempo()
        elif sub_opcion == "5.5":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
