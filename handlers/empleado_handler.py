"""
Handler para gestionar el menú de empleados.
"""

from controllers.empleado_controller import EmpleadoController
from models.empleado import Empleado
from views.menu import menu_empleado

empleado_controller = EmpleadoController()

def crear_empleado():
    """Lógica para crear un empleado."""
    rut = input("Ingrese el RUT del empleado: ")
    nombre = input("Ingrese el nombre del empleado: ")
    direccion = input("Ingrese la dirección del empleado: ")
    telefono = input("Ingrese el teléfono del empleado: ")
    email = input("Ingrese el email del empleado: ")
    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    try:
        salario = float(input("Ingrese el salario del empleado: "))
        departamento_id = int(input("Ingrese el ID del departamento: "))
    except ValueError:
        print("Error: Entrada no válida.")
        return
    empleado = Empleado(
        rut=rut, nombre=nombre, direccion=direccion, telefono=telefono,
        email=email, fecha_inicio=fecha_inicio, salario=salario, departamento_id=departamento_id
    )
    empleado_controller.crear_empleado(empleado)
    print("Empleado creado exitosamente.")

def listar_empleados():
    """Lógica para listar empleados."""
    empleados = empleado_controller.listar_empleados()
    if not empleados:
        print("No hay empleados registrados.")
    else:
        for emp in empleados:
            print(emp)

def buscar_empleado():
    """Lógica para buscar un empleado por RUT."""
    rut = input("Ingrese el RUT del empleado a buscar: ")
    empleado = empleado_controller.buscar_empleado_por_rut(rut)
    if empleado:
        print(empleado)
    else:
        print("Empleado no encontrado.")

def modificar_empleado():
    """Lógica para modificar un empleado."""
    rut = input("Ingrese el RUT del empleado a modificar: ")
    empleado = empleado_controller.buscar_empleado_por_rut(rut)
    if empleado:
        nombre = input("Ingrese el nuevo nombre: ") or empleado.nombre
        direccion = input("Ingrese la nueva dirección: ") or empleado.direccion
        telefono = input("Ingrese el nuevo teléfono: ") or empleado.telefono
        email = input("Ingrese el nuevo email: ") or empleado.email
        fecha_inicio = input("Ingrese la nueva fecha (YYYY-MM-DD): ") or empleado.fecha_inicio
        # pylint: disable=line-too-long
        try:
            salario = float(input("Ingrese el nuevo salario: ")) or empleado.salario
            departamento_id = int(input("Ingrese el nuevo ID del departamento: ")) or empleado.departamento_id
        except ValueError:
            print("Error: Entrada no válida.")
            return
        empleado_modificado = Empleado(
            rut=rut, nombre=nombre, direccion=direccion, telefono=telefono,
            email=email, fecha_inicio=fecha_inicio, salario=salario, departamento_id=departamento_id
        )
        empleado_controller.modificar_empleado(empleado_modificado)
        print("Empleado modificado exitosamente.")
    else:
        print("Empleado no encontrado.")

def eliminar_empleado():
    """Lógica para eliminar un empleado."""
    rut = input("Ingrese el RUT del empleado a eliminar: ")
    empleado_controller.eliminar_empleado(rut)
    print("Empleado eliminado exitosamente.")

def manejar_menu_empleado():
    """
    Maneja el menú de empleados.
    """
    while True:
        menu_empleado()
        sub_opcion = input("Seleccione una opción: ")

        if sub_opcion == "1.1":
            crear_empleado()
        elif sub_opcion == "1.2":
            listar_empleados()
        elif sub_opcion == "1.3":
            buscar_empleado()
        elif sub_opcion == "1.4":
            modificar_empleado()
        elif sub_opcion == "1.5":
            eliminar_empleado()
        elif sub_opcion == "1.6":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
