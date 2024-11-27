"""
Handler para gestionar la consulta y el registro de indicadores económicos.
"""

from controllers.indicadores_controller import IndicadoresController
from colorama import Fore, Style

indicadores_controller = IndicadoresController()


def mostrar_encabezado(titulo):
    """
    Muestra un encabezado decorado para las secciones.
    Args:
        titulo (str): Título del encabezado.
    """
    print(f"\n{Fore.CYAN}{'*' * 40}")
    print(f"{titulo.center(40)}")
    print(f"{'*' * 40}{Style.RESET_ALL}")


def consultar_indicador():
    """
    Interfaz para consultar un indicador económico.
    """
    mostrar_encabezado("CONSULTA DE INDICADORES ECONÓMICOS")
    print(f"{Fore.YELLOW}1.{Fore.GREEN} Unidad de Fomento (UF)")
    print(f"{Fore.YELLOW}2.{Fore.GREEN} Índice de Valor Promedio (IVP)")
    print(f"{Fore.YELLOW}3.{Fore.GREEN} Índice de Precios al Consumidor (IPC)")
    print(f"{Fore.YELLOW}4.{Fore.GREEN} Unidad Tributaria Mensual (UTM)")
    print(f"{Fore.YELLOW}5.{Fore.GREEN} Dólar Observado")
    print(f"{Fore.YELLOW}6.{Fore.GREEN} Euro{Style.RESET_ALL}")

    indicadores = ["uf", "ivp", "ipc", "utm", "dolar", "euro"]

    try:
        opcion = int(input(f"{Fore.YELLOW}Seleccione un indicador: {Style.RESET_ALL}").strip())
        indicador = indicadores[opcion - 1]
    except (IndexError, ValueError):
        print(f"{Fore.RED}Error: Selección inválida. Intente nuevamente.{Style.RESET_ALL}")
        return

    fecha = input(f"{Fore.YELLOW}Ingrese la fecha (YYYY-MM-DD) o deje vacío para datos recientes: {Style.RESET_ALL}").strip()
    datos = indicadores_controller.consultar_indicador(indicador, fecha_inicio=fecha)
    if datos:
        print(f"\n{Fore.CYAN}Resultado de la consulta:{Style.RESET_ALL}")
        for dato in datos:
            print(f"{Fore.GREEN}Fecha: {dato['fecha']} - Valor: {dato['valor']}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}No se encontraron datos para la fecha especificada.{Style.RESET_ALL}")


def registrar_indicador(usuario_id):
    """
    Interfaz para registrar un indicador económico en la base de datos.
    """
    mostrar_encabezado("REGISTRO DE INDICADORES ECONÓMICOS")
    print(f"{Fore.YELLOW}1.{Fore.GREEN} Unidad de Fomento (UF)")
    print(f"{Fore.YELLOW}2.{Fore.GREEN} Índice de Valor Promedio (IVP)")
    print(f"{Fore.YELLOW}3.{Fore.GREEN} Índice de Precios al Consumidor (IPC)")
    print(f"{Fore.YELLOW}4.{Fore.GREEN} Unidad Tributaria Mensual (UTM)")
    print(f"{Fore.YELLOW}5.{Fore.GREEN} Dólar Observado")
    print(f"{Fore.YELLOW}6.{Fore.GREEN} Euro{Style.RESET_ALL}")

    indicadores = ["uf", "ivp", "ipc", "utm", "dolar", "euro"]

    try:
        opcion = int(input(f"{Fore.YELLOW}Seleccione un indicador para registrar: {Style.RESET_ALL}").strip())
        indicador = indicadores[opcion - 1]
    except (IndexError, ValueError):
        print(f"{Fore.RED}Error: Selección inválida. Intente nuevamente.{Style.RESET_ALL}")
        return

    fecha_inicio = input(f"{Fore.YELLOW}Ingrese la fecha (YYYY-MM-DD): {Style.RESET_ALL}").strip()
    fecha_fin = input(f"{Fore.YELLOW}Ingrese la fecha de fin (YYYY-MM-DD) o deje vacío si es la misma fecha: {Style.RESET_ALL}").strip()
    if not fecha_fin:
        fecha_fin = fecha_inicio

    datos = indicadores_controller.consultar_indicador(indicador, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)
    if datos:
        indicadores_controller.registrar_indicador(
            datos=datos,
            indicador=indicador,
            usuario_id=usuario_id,
            url_fuente=indicadores_controller.api_url
        )
    else:
        print(f"{Fore.RED}No se encontraron datos para el período especificado.{Style.RESET_ALL}")


def listar_indicadores_registrados():
    """
    Lista los indicadores registrados en la base de datos.
    """
    mostrar_encabezado("LISTA DE INDICADORES REGISTRADOS")
    registros = indicadores_controller.listar_indicadores_registrados()
    if registros:
        for registro in registros:
            print(f"{Fore.GREEN}ID: {registro['id']}, Indicador: {registro['nombre_indicador']}, "
                  f"Fecha Valor: {registro['fecha_valor']}, Valor: {registro['valor']}, "
                  f"Fecha Consulta: {registro['fecha_consulta']}, Usuario ID: {registro['usuario_id']}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}No hay indicadores registrados.{Style.RESET_ALL}")


def eliminar_indicador():
    """
    Elimina un registro de indicador económico.
    """
    mostrar_encabezado("ELIMINAR REGISTRO DE INDICADOR")
    registro_id = input(f"{Fore.YELLOW}Ingrese el ID del registro a eliminar: {Style.RESET_ALL}").strip()
    indicadores_controller.eliminar_registro_indicador(registro_id)


def manejar_menu_indicadores(usuario_id):
    """
    Maneja el menú de indicadores económicos.
    """
    while True:
        mostrar_encabezado("MENÚ DE INDICADORES ECONÓMICOS")
        print(f"{Fore.YELLOW}1.{Fore.GREEN} Consultar Indicador Económico")
        print(f"{Fore.YELLOW}2.{Fore.GREEN} Registrar Indicador Económico")
        print(f"{Fore.YELLOW}3.{Fore.GREEN} Listar Indicadores Registrados")
        print(f"{Fore.YELLOW}4.{Fore.GREEN} Eliminar Indicador Registrado")
        print(f"{Fore.YELLOW}5.{Fore.GREEN} Volver al Menú Principal{Style.RESET_ALL}")

        opcion = input(f"{Fore.YELLOW}Seleccione una opción: {Style.RESET_ALL}").strip()

        if opcion == "1":
            consultar_indicador()
        elif opcion == "2":
            registrar_indicador(usuario_id)
        elif opcion == "3":
            listar_indicadores_registrados()
        elif opcion == "4":
            eliminar_indicador()
        elif opcion == "5":
            break
        else:
            print(f"{Fore.RED}Opción no válida.{Style.RESET_ALL}")
