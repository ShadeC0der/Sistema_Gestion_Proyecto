"""
Handler para gestionar el menú de departamentos.
"""

from controllers.departamento_controller import DepartamentoController
from models.departamento import Departamento
from views.menu import menu_departamento

departamento_controller = DepartamentoController()

def crear_departamento():
    """Lógica para crear un departamento."""
    nombre = input("Ingrese el nombre del departamento: ")
    gerente_id_input = input("Ingrese el ID del gerente (opcional): ")
    try:
        gerente_id = int(gerente_id_input) if gerente_id_input else None
    except ValueError:
        print("Error: El ID del gerente debe ser un número entero.")
        return
    nuevo_departamento = Departamento(nombre=nombre, gerente_id=gerente_id)
    departamento_controller.crear_departamento(nuevo_departamento)
    print("Departamento creado exitosamente.")

def listar_departamentos():
    """Lógica para listar departamentos."""
    departamentos = departamento_controller.listar_departamentos()
    if not departamentos:
        print("No hay departamentos registrados.")
    else:
        for dep in departamentos:
            print(dep)

def buscar_departamento():
    """Lógica para buscar un departamento por ID."""
    try:
        id_dep = int(input("Ingrese el ID del departamento a buscar: "))
    except ValueError:
        print("Error: El ID del departamento debe ser un número entero.")
        return
    departamento = departamento_controller.buscar_departamento_por_id(id_dep)
    if departamento:
        print(departamento)
    else:
        print("Departamento no encontrado.")

def modificar_departamento():
    """Lógica para modificar un departamento."""
    try:
        id_dep = int(input("Ingrese el ID del departamento a modificar: "))
    except ValueError:
        print("Error: El ID del departamento debe ser un número entero.")
        return
    # pylint: disable=line-too-long
    departamento = departamento_controller.buscar_departamento_por_id(id_dep)
    if departamento:
        nombre = input("Ingrese el nuevo nombre del departamento (deje vacío para mantener el actual): ") or departamento.nombre
        gerente_id_input = input("Ingrese el nuevo ID del gerente (opcional, deje vacío para mantener el actual): ")
        try:
            gerente_id = int(gerente_id_input) if gerente_id_input else departamento.gerente_id
        except ValueError:
            print("Error: El ID del gerente debe ser un número entero.")
            return
        departamento_modificado = Departamento(departamento_id=id_dep, nombre=nombre, gerente_id=gerente_id)
        departamento_controller.modificar_departamento(departamento_modificado)
        print("Departamento modificado exitosamente.")
    else:
        print("Departamento no encontrado.")

def eliminar_departamento():
    """Lógica para eliminar un departamento."""
    # pylint: disable=line-too-long
    try:
        id_dep = int(input("Ingrese el ID del departamento a eliminar: "))
    except ValueError:
        print("Error: El ID del departamento debe ser un número entero.")
        return
    confirmacion = input(f"¿Está seguro que desea eliminar el departamento con ID {id_dep}? (s/n): ")
    if confirmacion.lower() == 's':
        departamento_controller.eliminar_departamento(id_dep)
        print("Departamento eliminado exitosamente.")
    else:
        print("Operación cancelada.")

def manejar_menu_departamento():
    """
    Maneja el menú de departamentos.
    """
    while True:
        menu_departamento()
        sub_opcion = input("Seleccione una opción: ")

        if sub_opcion == "2.1":
            crear_departamento()
        elif sub_opcion == "2.2":
            listar_departamentos()
        elif sub_opcion == "2.3":
            buscar_departamento()
        elif sub_opcion == "2.4":
            modificar_departamento()
        elif sub_opcion == "2.5":
            eliminar_departamento()
        elif sub_opcion == "2.6":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
