"""
Modelo que representa la tabla de usuarios en el sistema.
"""

class Usuario:
    """
    Clase para representar un usuario del sistema.
    """
    def __init__(self, usuario_id=None, nombre_usuario="", password_hash="", rol="empleado"):
        """
        Inicializa una instancia de Usuario.

        Args:
            usuario_id (int, opcional): ID único del usuario.
            nombre_usuario (str): Nombre único del usuario.
            password_hash (str): Contraseña hasheada del usuario.
            rol (str): Rol del usuario ('admin' o 'empleado').
        """
        self.usuario_id = usuario_id
        self.nombre_usuario = nombre_usuario
        self.password_hash = password_hash
        self.rol = rol

    def __repr__(self):
        return f"Usuario(usuario_id={self.usuario_id}, nombre_usuario='{self.nombre_usuario}', rol='{self.rol}')"
