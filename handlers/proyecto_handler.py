"""
Handler para gestionar el menú de proyectos.
"""

from controllers.proyecto_controller import ProyectoController
from models.proyecto import Proyecto
from views.menu import menu_proyecto

proyecto_controller = ProyectoController()

def crear_proyecto():
    """Lógica para crear un proyecto."""
    nombre = input("Ingrese el nombre del proyecto: ")
    descripcion = input("Ingrese la descripción del proyecto: ")
    fecha_inicio = input("Ingrese la fecha de inicio del proyecto (YYYY-MM-DD): ")
    proyecto = Proyecto(nombre=nombre, descripcion=descripcion, fecha_inicio=fecha_inicio)
    proyecto_controller.crear_proyecto(proyecto)
    print("Proyecto creado exitosamente.")

def listar_proyectos():
    """Lógica para listar proyectos."""
    proyectos = proyecto_controller.listar_proyectos()
    if not proyectos:
        print("No hay proyectos registrados.")
    else:
        for pro in proyectos:
            print(pro)

def buscar_proyecto():
    """Lógica para buscar un proyecto por ID."""
    try:
        id_pro = int(input("Ingrese el ID del proyecto a buscar: "))
    except ValueError:
        print("Error: El ID del proyecto debe ser un número entero.")
        return
    proyecto = proyecto_controller.buscar_proyecto_por_id(id_pro)
    if proyecto:
        print(proyecto)
    else:
        print("Proyecto no encontrado.")

def modificar_proyecto():
    """Lógica para modificar un proyecto."""
    try:
        id_pro = int(input("Ingrese el ID del proyecto a modificar: "))
    except ValueError:
        print("Error: El ID del proyecto debe ser un número entero.")
        return
    proyecto = proyecto_controller.buscar_proyecto_por_id(id_pro)
     # pylint: disable=line-too-long
    if proyecto:
        nombre = input("Ingrese el nuevo nombre del proyecto (deje vacío para mantener el actual): ") or proyecto.nombre
        descripcion = input("Ingrese la nueva descripción del proyecto (deje vacío para mantener la actual): ") or proyecto.descripcion
        fecha_inicio = input("Ingrese la nueva fecha de inicio (YYYY-MM-DD, deje vacío para mantener la actual): ") or proyecto.fecha_inicio
        proyecto_modificado = Proyecto(proyecto_id=id_pro, nombre=nombre, descripcion=descripcion, fecha_inicio=fecha_inicio)
        proyecto_controller.modificar_proyecto(proyecto_modificado)
        print("Proyecto modificado exitosamente.")
    else:
        print("Proyecto no encontrado.")

def eliminar_proyecto():
    """Lógica para eliminar un proyecto."""
    try:
        id_pro = int(input("Ingrese el ID del proyecto a eliminar: "))
    except ValueError:
        print("Error: El ID del proyecto debe ser un número entero.")
        return
    confirmacion = input(f"¿Está seguro que desea eliminar el proyecto con ID {id_pro}? (s/n): ")
    if confirmacion.lower() == 's':
        proyecto_controller.eliminar_proyecto(id_pro)
        print("Proyecto eliminado exitosamente.")
    else:
        print("Operación cancelada.")

def manejar_menu_proyecto():
    """
    Maneja el menú de proyectos.
    """
    while True:
        menu_proyecto()
        sub_opcion = input("Seleccione una opción: ")

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
            print("Opción no válida. Por favor, seleccione una opción válida.")
