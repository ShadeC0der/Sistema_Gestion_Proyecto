"""
Handler para gestionar el menú de proyectos.
"""

from datetime import datetime
from controllers.proyecto_controller import ProyectoController
from models.proyecto import Proyecto
from views.menu import menu_proyecto

proyecto_controller = ProyectoController()


def mostrar_encabezado(titulo):
    """
    Muestra un encabezado decorado para las secciones.
    Args:
        titulo (str): Título del encabezado.
    """
    print("\n" + "*" * 40)
    print(f"{titulo.center(40)}")
    print("*" * 40)


def crear_proyecto():
    mostrar_encabezado("CREAR PROYECTO")
    nombre = input("Ingrese el nombre del proyecto: ").strip()
    if not nombre:
        print("Error: El nombre del proyecto no puede estar vacío.")
        return

    descripcion = input("Ingrese la descripción del proyecto: ").strip()
    if not descripcion:
        print("Error: La descripción del proyecto no puede estar vacía.")
        return

    while True:
        fecha_inicio_str = input("Ingrese la fecha de inicio del proyecto (YYYY-MM-DD): ").strip()
        try:
            fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Error: La fecha ingresada no tiene el formato válido (YYYY-MM-DD). Intente nuevamente.")

    proyecto = Proyecto(nombre=nombre, descripcion=descripcion, fecha_inicio=fecha_inicio)
    proyecto_controller.crear_proyecto(proyecto)


def listar_proyectos():
    mostrar_encabezado("LISTA DE PROYECTOS")
    proyectos = proyecto_controller.listar_proyectos()
    if not proyectos:
        print("No hay proyectos registrados.")
    else:
        for pro in proyectos:
            print(
                f"""
Proyecto ID: {pro.proyecto_id}
Nombre: {pro.nombre}
Descripción: {pro.descripcion}
Fecha de Inicio: {pro.fecha_inicio}
{"-" * 40}
"""
            )


def buscar_proyecto():
    mostrar_encabezado("BUSCAR PROYECTO")
    try:
        id_pro = int(input("Ingrese el ID del proyecto a buscar: "))
    except ValueError:
        print("Error: El ID del proyecto debe ser un número entero.")
        return

    proyecto = proyecto_controller.buscar_proyecto_por_id(id_pro)
    if proyecto:
        print(
            f"""
Proyecto encontrado:
Proyecto ID: {proyecto.proyecto_id}
Nombre: {proyecto.nombre}
Descripción: {proyecto.descripcion}
Fecha de Inicio: {proyecto.fecha_inicio}
{"*" * 40}
"""
        )
    else:
        print("Proyecto no encontrado.")


def modificar_proyecto():
    mostrar_encabezado("MODIFICAR PROYECTO")
    try:
        id_pro = int(input("Ingrese el ID del proyecto a modificar: "))
    except ValueError:
        print("Error: El ID del proyecto debe ser un número entero.")
        return

    proyecto = proyecto_controller.buscar_proyecto_por_id(id_pro)
    if not proyecto:
        print("Proyecto no encontrado.")
        return

    nombre = input(f"Ingrese el nuevo nombre del proyecto [{proyecto.nombre}]: ").strip() or proyecto.nombre
    descripcion = input(f"Ingrese la nueva descripción del proyecto [{proyecto.descripcion}]: ").strip() or proyecto.descripcion
    fecha_inicio_str = input(
        f"Ingrese la nueva fecha de inicio (YYYY-MM-DD) [{proyecto.fecha_inicio}]: "
    ).strip() or proyecto.fecha_inicio

    try:
        fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d").date()
    except ValueError:
        print("Error: La fecha ingresada no tiene el formato válido. No se realizaron cambios.")
        return

    proyecto_modificado = Proyecto(proyecto_id=id_pro, nombre=nombre, descripcion=descripcion, fecha_inicio=fecha_inicio)
    proyecto_controller.modificar_proyecto(proyecto_modificado)


def eliminar_proyecto():
    mostrar_encabezado("ELIMINAR PROYECTO")
    try:
        id_pro = int(input("Ingrese el ID del proyecto a eliminar: "))
    except ValueError:
        print("Error: El ID del proyecto debe ser un número entero.")
        return

    confirmacion = input(f"¿Está seguro que desea eliminar el proyecto con ID {id_pro}? (s/n): ").strip().lower()
    if confirmacion == 's':
        proyecto_controller.eliminar_proyecto(id_pro)


def manejar_menu_proyecto():
    while True:
        menu_proyecto()
        sub_opcion = input("Seleccione una opción: ").strip()

        if sub_opcion == "3.1":
            crear_proyecto()
        elif sub_opcion == "3.2":
            listar_proyectos()
        elif sub_opcion == "3.3":
            buscar_proyecto()
        elif sub_opcion == "3.4":
            modificar_proyecto()
        elif sub_opcion == "3.5":
            eliminar_proyecto()
        elif sub_opcion == "3.6":
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
