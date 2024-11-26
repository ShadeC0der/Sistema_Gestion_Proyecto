"""
Módulo para gestionar la visualización de los menús en la aplicación.
"""
from colorama import Fore, Style

def menu_inicial():
    """
    Muestra el menú inicial de la aplicación.
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}\nBienvenido al Sistema de Gestión de Proyectos")
    print(f"{Fore.YELLOW}1.{Fore.GREEN} Iniciar Sesión")
    print(f"{Fore.YELLOW}2.{Fore.GREEN} Registrarse")
    print(f"{Fore.YELLOW}3.{Fore.RED} Salir\n")

def menu_principal():
    """
    Muestra el menú principal de la aplicación.
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}Menu Principal{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}1.{Fore.GREEN} Registro de Empleados")
    print(f"{Fore.YELLOW}2.{Fore.GREEN} Gestión de Departamentos")
    print(f"{Fore.YELLOW}3.{Fore.GREEN} Gestión de Proyecto")
    print(f"{Fore.YELLOW}4.{Fore.GREEN} Registro de Tiempo")
    print(f"{Fore.YELLOW}5.{Fore.GREEN} Generar Informes")
    print(f"{Fore.YELLOW}6.{Fore.GREEN} Salir")

def menu_empleado():
    """
    Muestra el menú para la gestión de empleados.
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}\n1. Gestión de Empleados{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}1.1.{Fore.GREEN} Crear Empleado")
    print(f"{Fore.YELLOW}1.2.{Fore.GREEN} Listar Empleado")
    print(f"{Fore.YELLOW}1.3.{Fore.GREEN} Buscar Empleado")
    print(f"{Fore.YELLOW}1.4.{Fore.GREEN} Modificar Empleado")
    print(f"{Fore.YELLOW}1.5.{Fore.GREEN} Eliminar Empleado")
    print(f"{Fore.YELLOW}1.6.{Fore.GREEN} Volver al menú Principal")

def menu_departamento():
    """
    Muestra el menú para la gestión de departamentos.
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}\n2. Gestión de Departamentos{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}2.1.{Fore.GREEN} Crear Departamento")
    print(f"{Fore.YELLOW}2.2.{Fore.GREEN} Listar Departamentos")
    print(f"{Fore.YELLOW}2.3.{Fore.GREEN} Buscar Departamento")
    print(f"{Fore.YELLOW}2.4.{Fore.GREEN} Modificar Departamento")
    print(f"{Fore.YELLOW}2.5.{Fore.GREEN} Eliminar Departamento")
    print(f"{Fore.YELLOW}2.6.{Fore.GREEN} Volver al menú Principal")

def menu_proyecto():
    """
    Muestra el menú para la gestión de proyectos.
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}\n3. Gestión de Proyectos{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}3.1.{Fore.GREEN} Crear Proyecto")
    print(f"{Fore.YELLOW}3.2.{Fore.GREEN} Listar Proyecto")
    print(f"{Fore.YELLOW}3.3.{Fore.GREEN} Buscar Proyecto")
    print(f"{Fore.YELLOW}3.4.{Fore.GREEN} Modificar Proyecto")
    print(f"{Fore.YELLOW}3.5.{Fore.GREEN} Eliminar Proyecto")
    print(f"{Fore.YELLOW}3.6.{Fore.GREEN} Volver al menú Principal")
    
def menu_registrodetiempo():
    """
    Muestra el menú para la gestión de registros de tiempo.
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}\n4. Registro de Tiempo{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}4.1.{Fore.GREEN} Crear Registro de tiempo")
    print(f"{Fore.YELLOW}4.2.{Fore.GREEN} Listar Registro de tiempo")
    print(f"{Fore.YELLOW}4.3.{Fore.GREEN} Buscar Registro de tiempo")
    print(f"{Fore.YELLOW}4.4.{Fore.GREEN} Modificar Registro de tiempo")
    print(f"{Fore.YELLOW}4.5.{Fore.GREEN} Eliminar Registro de tiempo")
    print(f"{Fore.YELLOW}4.6.{Fore.GREEN} Volver al menú Principal")
    
def menu_informes():
    """
    Muestra el menú para la generación de informes.
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}\n5. Generación de Informes{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}5.1.{Fore.GREEN} Informe de Empleados (Excel)")
    print(f"{Fore.YELLOW}5.2.{Fore.GREEN} Informe de Departamentos (Excel)")
    print(f"{Fore.YELLOW}5.3.{Fore.GREEN} Informe de Proyectos (Excel)")
    print(f"{Fore.YELLOW}5.4.{Fore.GREEN} Informe de Registros de Tiempo (Excel)")
    print(f"{Fore.YELLOW}5.5.{Fore.GREEN} Informe de Empleados (PDF)")
    print(f"{Fore.YELLOW}5.6.{Fore.GREEN} Volver al menú Principal")
