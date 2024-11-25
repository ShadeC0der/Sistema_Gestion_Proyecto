# Sistema de Gestión de Proyectos

Este es un sistema de gestión de proyectos desarrollado en Python con una estructura MVC (Modelo-Vista-Controlador). La aplicación permite realizar operaciones CRUD sobre empleados, departamentos, proyectos y registros de tiempo. También genera informes en formato Excel.

## Características principales

- **CRUD** para empleados, departamentos, proyectos y registros de tiempo.
- Generación de informes en formato Excel.
- Gestión modular con una arquitectura **MVC**.
- Colores personalizados para mejorar la experiencia en la terminal.
- Manejo de conexión a la base de datos con `mysql-connector-python`.

---

## Requisitos previos

Asegúrate de tener instalados los siguientes programas en tu sistema:

- **Python 3.8 o superior**
- **MySQL**

Además, instala las dependencias del proyecto utilizando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Estructura del archivo .env

Crea un archivo .env en el directorio raíz del proyecto con la siguiente estructura para configurar la conexión a la base de datos:

```
DB_USER=root              # Usuario de MySQL
DB_PASSWORD=              # Contraseña del usuario
DB_HOST=localhost         # Host de la base de datos
DB_NAME=gestionproyectos  # Nombre de la base de datos
DB_PORT=3306              # Puerto de MySQL (por defecto es 3306)
```