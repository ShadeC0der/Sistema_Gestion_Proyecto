"""
Handler para gestionar el menú de registros de tiempo.
"""

from datetime import datetime
from controllers.registro_tiempo_controller import RegistroDeTiempoController
from models.registro_tiempo import RegistroDeTiempo
from views.menu import menu_registrodetiempo

registro_tiempo_controller = RegistroDeTiempoController()


def mostrar_encabezado(titulo):
    print("\n" + "*" * 40)
    print(f"{titulo.center(40)}")
    print("*" * 40)


def crear_registro_tiempo():
    mostrar_encabezado("CREAR REGISTRO DE TIEMPO")
    while True:
        fecha_str = input("Ingrese la fecha del registro (YYYY-MM-DD): ").strip()
        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Error: La fecha ingresada no tiene el formato válido (YYYY-MM-DD).")

    try:
        horas_trabajadas = float(input("Ingrese las horas trabajadas: ").strip())
    except ValueError:
        print("Error: Las horas trabajadas deben ser un número.")
        return

    descripcion = input("Ingrese la descripción del registro: ").strip()
    if not descripcion:
        print("Error: La descripción no puede estar vacía.")
        return

    try:
        empleado_id = int(input("Ingrese el ID del empleado: ").strip())
    except ValueError:
        print("Error: El ID del empleado debe ser un número entero.")
        return

    registro = RegistroDeTiempo(fecha=fecha, horas_trabajadas=horas_trabajadas, descripcion=descripcion, empleado_id=empleado_id)
    registro_tiempo_controller.crear_registro(registro)


def listar_registros_tiempo():
    mostrar_encabezado("LISTA DE REGISTROS DE TIEMPO")
    registros = registro_tiempo_controller.listar_registros()
    if not registros:
        print("No hay registros de tiempo disponibles.")
    else:
        for reg in registros:
            print(
                f"""
Registro ID: {reg.registro_id}
Fecha: {reg.fecha}
Horas Trabajadas: {reg.horas_trabajadas}
Descripción: {reg.descripcion}
Empleado ID: {reg.empleado_id}
{"-" * 40}
"""
            )


def buscar_registro_tiempo():
    mostrar_encabezado("BUSCAR REGISTRO DE TIEMPO")
    try:
        id_reg = int(input("Ingrese el ID del registro a buscar: ").strip())
    except ValueError:
        print("Error: El ID del registro debe ser un número entero.")
        return

    registro = registro_tiempo_controller.buscar_registro_por_id(id_reg)
    if registro:
        print(
            f"""
Registro encontrado:
Registro ID: {registro.registro_id}
Fecha: {registro.fecha}
Horas Trabajadas: {registro.horas_trabajadas}
Descripción: {registro.descripcion}
Empleado ID: {registro.empleado_id}
{"*" * 40}
"""
        )
    else:
        print("Registro de tiempo no encontrado.")


def modificar_registro_tiempo():
    mostrar_encabezado("MODIFICAR REGISTRO DE TIEMPO")
    try:
        id_reg = int(input("Ingrese el ID del registro a modificar: ").strip())
    except ValueError:
        print("Error: El ID del registro debe ser un número entero.")
        return

    registro = registro_tiempo_controller.buscar_registro_por_id(id_reg)
    if not registro:
        print("Registro de tiempo no encontrado.")
        return

    print(f"Registro actual: {registro}")

    fecha_str = input(f"Ingrese la nueva fecha (YYYY-MM-DD) [{registro.fecha}]: ").strip() or registro.fecha
    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date() if isinstance(fecha_str, str) else registro.fecha
    except ValueError:
        print("Error: La fecha ingresada no tiene el formato válido. No se realizaron cambios.")
        return

    try:
        horas_trabajadas = float(input(f"Ingrese las nuevas horas trabajadas [{registro.horas_trabajadas}]: ").strip()) or registro.horas_trabajadas
    except ValueError:
        print("Error: Las horas trabajadas deben ser un número.")
        return

    descripcion = input(f"Ingrese la nueva descripción [{registro.descripcion}]: ").strip() or registro.descripcion
    try:
        empleado_id = int(input(f"Ingrese el nuevo ID del empleado [{registro.empleado_id}]: ").strip()) or registro.empleado_id
    except ValueError:
        print("Error: El ID del empleado debe ser un número entero.")
        return

    registro_modificado = RegistroDeTiempo(
        registro_id=id_reg, fecha=fecha, horas_trabajadas=horas_trabajadas, descripcion=descripcion, empleado_id=empleado_id
    )
    registro_tiempo_controller.modificar_registro(registro_modificado)


def eliminar_registro_tiempo():
    mostrar_encabezado("ELIMINAR REGISTRO DE TIEMPO")
    try:
        id_reg = int(input("Ingrese el ID del registro a eliminar: ").strip())
    except ValueError:
        print("Error: El ID del registro debe ser un número entero.")
        return

    confirmacion = input(f"¿Está seguro que desea eliminar el registro con ID {id_reg}? (s/n): ").strip().lower()
    if confirmacion == 's':
        registro_tiempo_controller.eliminar_registro(id_reg)
    else:
        print("Operación cancelada.")


def manejar_menu_registro():
    while True:
        menu_registrodetiempo()
        sub_opcion = input("Seleccione una opción: ").strip()

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
