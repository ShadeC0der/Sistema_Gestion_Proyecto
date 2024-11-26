"""
Handler para gestionar el menú de departamentos.
"""

from controllers.departamento_controller import DepartamentoController
from models.departamento import Departamento
from views.menu import menu_departamento

departamento_controller = DepartamentoController()


def mostrar_encabezado(titulo):
    """
    Muestra un encabezado decorado para las secciones.
    Args:
        titulo (str): Título del encabezado.
    """
    print("\n" + "*" * 40)
    print(f"{titulo.center(40)}")
    print("*" * 40)


def crear_departamento():
    mostrar_encabezado("CREAR DEPARTAMENTO")
    nombre = input("Ingrese el nombre del departamento: ").strip()
    if not nombre:
        print("Error: El nombre del departamento no puede estar vacío.")
        return

    gerente_id_input = input("Ingrese el ID del gerente (opcional): ").strip()
    try:
        gerente_id = int(gerente_id_input) if gerente_id_input else None
    except ValueError:
        print("Error: El ID del gerente debe ser un número entero.")
        return

    nuevo_departamento = Departamento(nombre=nombre, gerente_id=gerente_id)
    departamento_controller.crear_departamento(nuevo_departamento)


def listar_departamentos():
    mostrar_encabezado("LISTA DE DEPARTAMENTOS")
    departamentos = departamento_controller.listar_departamentos()
    if not departamentos:
        print("No hay departamentos registrados.")
    else:
        for dep in departamentos:
            print(
                f"""
Departamento ID: {dep.departamento_id}
Nombre: {dep.nombre}
Gerente ID: {dep.gerente_id if dep.gerente_id else 'No asignado'}
{"-" * 40}
"""
            )


def buscar_departamento():
    mostrar_encabezado("BUSCAR DEPARTAMENTO")
    try:
        id_dep = int(input("Ingrese el ID del departamento a buscar: "))
    except ValueError:
        print("Error: El ID del departamento debe ser un número entero.")
        return

    departamento = departamento_controller.buscar_departamento_por_id(id_dep)
    if departamento:
        print(
            f"""
Departamento encontrado:
Departamento ID: {departamento.departamento_id}
Nombre: {departamento.nombre}
Gerente ID: {departamento.gerente_id if departamento.gerente_id else 'No asignado'}
{"*" * 40}
"""
        )
    else:
        print("Departamento no encontrado.")


def modificar_departamento():
    mostrar_encabezado("MODIFICAR DEPARTAMENTO")
    try:
        id_dep = int(input("Ingrese el ID del departamento a modificar: "))
    except ValueError:
        print("Error: El ID del departamento debe ser un número entero.")
        return

    departamento = departamento_controller.buscar_departamento_por_id(id_dep)
    if not departamento:
        print("Departamento no encontrado.")
        return

    nombre = input(f"Ingrese el nuevo nombre [{departamento.nombre}]: ").strip() or departamento.nombre
    gerente_id_input = input(
        f"Ingrese el nuevo ID del gerente (opcional) [{departamento.gerente_id if departamento.gerente_id else 'No asignado'}]: "
    ).strip()

    try:
        gerente_id = int(gerente_id_input) if gerente_id_input else departamento.gerente_id
    except ValueError:
        print("Error: El ID del gerente debe ser un número entero.")
        return

    departamento_modificado = Departamento(departamento_id=id_dep, nombre=nombre, gerente_id=gerente_id)
    departamento_controller.modificar_departamento(departamento_modificado)


def eliminar_departamento():
    mostrar_encabezado("ELIMINAR DEPARTAMENTO")
    try:
        id_dep = int(input("Ingrese el ID del departamento a eliminar: "))
    except ValueError:
        print("Error: El ID del departamento debe ser un número entero.")
        return

    confirmacion = input(f"¿Está seguro que desea eliminar el departamento con ID {id_dep}? (s/n): ").strip().lower()
    if confirmacion == 's':
        departamento_controller.eliminar_departamento(id_dep)
    else:
        print("Operación cancelada.")


def manejar_menu_departamento():
    while True:
        menu_departamento()
        sub_opcion = input("Seleccione una opción: ").strip()

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
