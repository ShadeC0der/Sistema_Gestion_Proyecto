"""
Handler para gestionar el menú de empleados.
"""
from datetime import datetime
from controllers.empleado_controller import EmpleadoController
from models.empleado import Empleado
from views.menu import menu_empleado

empleado_controller = EmpleadoController()

def mostrar_encabezado(titulo):
    """
    Muestra un encabezado decorado para las secciones.
    Args:
        titulo (str): Título del encabezado.
    """
    print("\n" + "*" * 40)
    print(f"{titulo.center(40)}")
    print("*" * 40)

def crear_empleado():
    """
    Lógica para crear un nuevo empleado.
    """
    mostrar_encabezado("CREAR EMPLEADO")
    rut = input("Ingrese el RUT del empleado: ")
    nombre = input("Ingrese el nombre del empleado: ")
    direccion = input("Ingrese la dirección del empleado: ")
    telefono = input("Ingrese el teléfono del empleado: ")
    email = input("Ingrese el email del empleado: ")

    while True:
        fecha_inicio_str = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
        try:
            fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Error: La fecha ingresada no tiene el formato válido (YYYY-MM-DD). Intente nuevamente.")

    try:
        salario = float(input("Ingrese el salario del empleado: "))
        departamento_id = int(input("Ingrese el ID del departamento: "))
    except ValueError:
        print("Error: Entrada inválida. Intente nuevamente.")
        return

    empleado = Empleado(
        rut=rut,
        nombre=nombre,
        direccion=direccion,
        telefono=telefono,
        email=email,
        fecha_inicio=fecha_inicio,
        salario=salario,
        departamento_id=departamento_id,
    )

    empleado_controller.crear_empleado(empleado)
    print("\nEmpleado creado exitosamente.")
    print("*" * 40)

def listar_empleados():
    """Lógica para listar empleados."""
    mostrar_encabezado("LISTA DE EMPLEADOS")
    empleados = empleado_controller.listar_empleados()
    if not empleados:
        print("No hay empleados registrados.")
    else:
        for emp in empleados:
            print(
                f"""
Empleado ID: {emp.empleado_id}
RUT: {emp.rut}
Nombre: {emp.nombre}
Dirección: {emp.direccion}
Teléfono: {emp.telefono}
Email: {emp.email}
Fecha de Inicio: {emp.fecha_inicio}
Salario: ${emp.salario:.2f}
Departamento ID: {emp.departamento_id}
{"-" * 40}
"""
            )

def buscar_empleado():
    """Lógica para buscar un empleado por RUT."""
    mostrar_encabezado("BUSCAR EMPLEADO")
    rut = input("Ingrese el RUT del empleado a buscar: ")
    empleado = empleado_controller.buscar_empleado_por_rut(rut)
    if empleado:
        print(
            f"""
Empleado encontrado:
Empleado ID: {empleado.empleado_id}
RUT: {empleado.rut}
Nombre: {empleado.nombre}
Dirección: {empleado.direccion}
Teléfono: {empleado.telefono}
Email: {empleado.email}
Fecha de Inicio: {empleado.fecha_inicio}
Salario: ${empleado.salario:.2f}
Departamento ID: {empleado.departamento_id}
{"*" * 40}
"""
        )
    else:
        print("Empleado no encontrado.")

def modificar_empleado():
    """
    Lógica para modificar un empleado. Conserva valores actuales si se deja en blanco.
    """
    mostrar_encabezado("MODIFICAR EMPLEADO")
    rut = input("Ingrese el RUT del empleado a modificar: ")
    empleado = empleado_controller.buscar_empleado_por_rut(rut)
    
    if not empleado:
        print("Empleado no encontrado.")
        return

    print(f"Empleado encontrado: {empleado}")

    # Solicitar nuevos valores
    nombre = input(f"Ingrese el nuevo nombre [{empleado.nombre}]: ") or empleado.nombre
    direccion = input(f"Ingrese la nueva dirección [{empleado.direccion}]: ") or empleado.direccion
    telefono = input(f"Ingrese el nuevo teléfono [{empleado.telefono}]: ") or empleado.telefono
    email = input(f"Ingrese el nuevo email [{empleado.email}]: ") or empleado.email
    fecha_inicio_str = input(f"Ingrese la nueva fecha (YYYY-MM-DD) [{empleado.fecha_inicio}]: ") or empleado.fecha_inicio

    try:
        salario_input = input(f"Ingrese el nuevo salario [{empleado.salario}]: ")
        salario = float(salario_input) if salario_input else empleado.salario
        departamento_id_input = input(f"Ingrese el nuevo ID del departamento [{empleado.departamento_id}]: ")
        departamento_id = int(departamento_id_input) if departamento_id_input else empleado.departamento_id
    except ValueError:
        print("Error: Entrada inválida. No se realizaron cambios.")
        return

    empleado_modificado = Empleado(
        empleado_id=empleado.empleado_id,
        rut=rut,
        nombre=nombre,
        direccion=direccion,
        telefono=telefono,
        email=email,
        fecha_inicio=fecha_inicio_str,
        salario=salario,
        departamento_id=departamento_id,
    )

    empleado_controller.modificar_empleado(empleado_modificado)
    print("\nEmpleado modificado exitosamente.")
    print("*" * 40)

def eliminar_empleado():
    """Lógica para eliminar un empleado."""
    mostrar_encabezado("ELIMINAR EMPLEADO")
    rut = input("Ingrese el RUT del empleado a eliminar: ")
    empleado_controller.eliminar_empleado(rut)
    print("Empleado eliminado exitosamente.")
    print("*" * 40)

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
