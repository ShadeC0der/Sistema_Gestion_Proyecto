"""
Handler para gestionar el menú de generación de informes.
"""

from controllers.informes_controller import InformesController
from views.menu import menu_informes

informes_controller = InformesController()

def generar_informe_empleados():
    """Genera un informe de empleados en Excel."""
    informes_controller.generar_informe_empleados()
    print("Informe de empleados generado exitosamente en 'informe_empleados.xlsx'.")

def generar_informe_departamentos():
    """Genera un informe de departamentos en Excel."""
    informes_controller.generar_informe_departamentos()
    print("Informe de departamentos generado exitosamente en 'informe_departamentos.xlsx'.")

def generar_informe_proyectos():
    """Genera un informe de proyectos en Excel."""
    informes_controller.generar_informe_proyectos()
    print("Informe de proyectos generado exitosamente en 'informe_proyectos.xlsx'.")


def generar_informe_registros_tiempo():
    """Genera un informe de registros de tiempo en Excel."""
    informes_controller.generar_informe_registros_tiempo()
     # pylint: disable=line-too-long
    print("Informe de registros de tiempo generado exitosamente en 'informe_registros_tiempo.xlsx'.")

def manejar_menu_informes():
    """
    Maneja el menú de generación de informes.
    """
    while True:
        menu_informes()
        sub_opcion = input("Seleccione una opción: ")

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
