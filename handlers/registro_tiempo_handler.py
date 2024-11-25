"""
Handler para gestionar el menú de registros de tiempo.
"""

from controllers.registro_tiempo_controller import RegistroDeTiempoController
from models.registro_tiempo import RegistroDeTiempo
from views.menu import menu_registrodetiempo

registro_tiempo_controller = RegistroDeTiempoController()

def crear_registro_tiempo():
    """Lógica para crear un registro de tiempo."""
    fecha = input("Ingrese la fecha del registro (YYYY-MM-DD): ")
    try:
        horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
    except ValueError:
        print("Error: Las horas trabajadas deben ser un número.")
        return
    descripcion = input("Ingrese la descripción del registro: ")
    try:
        empleado_id = int(input("Ingrese el ID del empleado: "))
    except ValueError:
        print("Error: El ID del empleado debe ser un número entero.")
        return
    # pylint: disable=line-too-long
    registro = RegistroDeTiempo(fecha=fecha, horas_trabajadas=horas_trabajadas, descripcion=descripcion, empleado_id=empleado_id)
    registro_tiempo_controller.crear_registro(registro)
    print("Registro de tiempo creado exitosamente.")

def listar_registros_tiempo():
    """Lógica para listar registros de tiempo."""
    registros = registro_tiempo_controller.listar_registros()
    if not registros:
        print("No hay registros de tiempo disponibles.")
    else:
        for reg in registros:
            print(reg)

def buscar_registro_tiempo():
    """Lógica para buscar un registro de tiempo por ID."""
    try:
        id_reg = int(input("Ingrese el ID del registro a buscar: "))
    except ValueError:
        print("Error: El ID del registro debe ser un número entero.")
        return
    registro = registro_tiempo_controller.buscar_registro_por_id(id_reg)
    if registro:
        print(registro)
    else:
        print("Registro de tiempo no encontrado.")

def modificar_registro_tiempo():
    """Lógica para modificar un registro de tiempo."""
    try:
        id_reg = int(input("Ingrese el ID del registro a modificar: "))
    except ValueError:
        print("Error: El ID del registro debe ser un número entero.")
        return
    registro = registro_tiempo_controller.buscar_registro_por_id(id_reg)
     # pylint: disable=line-too-long
    if registro:
        fecha = input("Ingrese la nueva fecha del registro (YYYY-MM-DD, deje vacío para mantener la actual): ") or registro.fecha
        try:
            horas_trabajadas = float(input("Ingrese las nuevas horas trabajadas (deje vacío para mantener el actual): ")) or registro.horas_trabajadas
        except ValueError:
            print("Error: Las horas trabajadas deben ser un número.")
            return
        descripcion = input("Ingrese la nueva descripción del registro (deje vacío para mantener la actual): ") or registro.descripcion
        try:
            empleado_id = int(input("Ingrese el nuevo ID del empleado (deje vacío para mantener el actual): ")) or registro.empleado_id
        except ValueError:
            print("Error: El ID del empleado debe ser un número entero.")
            return
        registro_modificado = RegistroDeTiempo(
            registro_id=id_reg, fecha=fecha, horas_trabajadas=horas_trabajadas,
            descripcion=descripcion, empleado_id=empleado_id
        )
        registro_tiempo_controller.modificar_registro(registro_modificado)
        print("Registro de tiempo modificado exitosamente.")
    else:
        print("Registro de tiempo no encontrado.")

def eliminar_registro_tiempo():
    """Lógica para eliminar un registro de tiempo."""
    try:
        id_reg = int(input("Ingrese el ID del registro a eliminar: "))
    except ValueError:
        print("Error: El ID del registro debe ser un número entero.")
        return
    confirmacion = input(f"¿Está seguro que desea eliminar el registro con ID {id_reg}? (s/n): ")
    if confirmacion.lower() == 's':
        registro_tiempo_controller.eliminar_registro(id_reg)
        print("Registro de tiempo eliminado exitosamente.")
    else:
        print("Operación cancelada.")

def manejar_menu_registro():
    """
    Maneja el menú de registros de tiempo.
    """
    while True:
        menu_registrodetiempo()
        sub_opcion = input("Seleccione una opción: ")

        if sub_opcion == "4.1":
            crear_registro_tiempo()
        elif sub_opcion == "4.2":
            listar_registros_tiempo()
        elif sub_opcion == "4.3":
            buscar_registro_tiempo()
        elif sub_opcion == "4.4":
            modificar_registro_tiempo()
        elif sub_opcion == "4.5":
            eliminar_registro_tiempo()
        elif sub_opcion == "4.6":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
