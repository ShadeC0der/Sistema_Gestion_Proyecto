"""
Handler para gestionar la lógica de autenticación y registro de usuarios.
"""
import re
from colorama import Fore
from controllers.usuario_controller import UsuarioController

usuario_controller = UsuarioController()


def validar_nombre_usuario(nombre_usuario):
    """
    Valida el formato del nombre de usuario.
    """
    if not re.match(r"^[a-zA-Z0-9_]{5,20}$", nombre_usuario):
        print(f"{Fore.RED}El nombre de usuario debe tener entre 5 y 20 caracteres alfanuméricos o guión bajo.")
        return False
    return True


def validar_contrasena(password):
    """
    Valida que la contraseña cumpla con requisitos de seguridad.
    """
    if len(password) < 8:
        print(f"{Fore.RED}La contraseña debe tener al menos 8 caracteres.")
        return False
    if not re.search(r"[A-Z]", password):
        print(f"{Fore.RED}La contraseña debe incluir al menos una letra mayúscula.")
        return False
    if not re.search(r"[a-z]", password):
        print(f"{Fore.RED}La contraseña debe incluir al menos una letra minúscula.")
        return False
    if not re.search(r"[0-9]", password):
        print(f"{Fore.RED}La contraseña debe incluir al menos un número.")
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print(f"{Fore.RED}La contraseña debe incluir al menos un carácter especial (!@#$%^&*).")
        return False
    return True


def registrar_usuario():
    """
    Permite registrar un nuevo usuario.
    """
    print(f"{Fore.CYAN}Registro de Usuario")
    while True:
        nombre_usuario = input(f"{Fore.YELLOW}Ingrese el nombre de usuario: {Fore.WHITE}")
        if not validar_nombre_usuario(nombre_usuario):
            continue

        password = input(f"{Fore.YELLOW}Ingrese la contraseña: {Fore.WHITE}")
        if not validar_contrasena(password):
            continue

        confirm_password = input(f"{Fore.YELLOW}Confirme la contraseña: {Fore.WHITE}")
        if password != confirm_password:
            print(f"{Fore.RED}Las contraseñas no coinciden. Intente nuevamente.")
            continue

        try:
            usuario_controller.crear_usuario(nombre_usuario, password, rol="empleado")
            print(f"{Fore.GREEN}Usuario '{nombre_usuario}' creado exitosamente.")
            break
        except Exception as err:
            print(f"{Fore.RED}Error al crear el usuario: {err}")
            break


def iniciar_sesion():
    """
    Solicita al usuario iniciar sesión.
    """
    print(f"{Fore.CYAN}Inicio de Sesión")
    while True:
        nombre_usuario = input(f"{Fore.YELLOW}Nombre de usuario: {Fore.WHITE}")
        password = input(f"{Fore.YELLOW}Contraseña: {Fore.WHITE}")
        resultado = usuario_controller.autenticar_usuario(nombre_usuario, password)

        if resultado["autenticado"]:
            print(f"{Fore.GREEN}Inicio de sesión exitoso. Rol: {resultado['usuario'].rol}")
            return resultado
        else:
            print(f"{Fore.RED}Credenciales incorrectas. Intente nuevamente.")
