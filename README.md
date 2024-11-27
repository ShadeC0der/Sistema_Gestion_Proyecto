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
---

## Base de Datos Utilizada

```sql
-- Crear tabla Departamento sin clave foránea
CREATE TABLE departamento (
    departamento_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    gerente_id INT
);

-- Crear tabla Empleado sin clave foránea
CREATE TABLE empleado (
    empleado_id INT PRIMARY KEY AUTO_INCREMENT,
    rut VARCHAR(12) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(15),
    email VARCHAR(100),
    fecha_inicio DATE,
    salario DECIMAL(10, 2) CHECK (salario >= 0),
    departamento_id INT
);

-- Crear tabla Proyecto
CREATE TABLE proyecto (
    proyecto_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT,
    fecha_inicio DATE
);

-- Crear tabla intermedia para la relación muchos a muchos entre Empleado y Proyecto
CREATE TABLE empleado_proyecto (
    empleado_id INT,
    proyecto_id INT,
    PRIMARY KEY (empleado_id, proyecto_id)
);

-- Crear tabla Registro de Tiempo
CREATE TABLE registro_de_tiempo (
    registro_id INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATE NOT NULL,
    horas_trabajadas FLOAT CHECK (horas_trabajadas >= 0),
    descripcion TEXT,
    empleado_id INT
);

-- Agregar claves foráneas después de crear las tablas
ALTER TABLE departamento
ADD CONSTRAINT fk_departamento_gerente
FOREIGN KEY (gerente_id) REFERENCES empleado(empleado_id);

ALTER TABLE empleado
ADD CONSTRAINT fk_empleado_departamento
FOREIGN KEY (departamento_id) REFERENCES departamento(departamento_id);

ALTER TABLE empleado_proyecto
ADD CONSTRAINT fk_empleado_proyecto_empleado
FOREIGN KEY (empleado_id) REFERENCES empleado(empleado_id),
ADD CONSTRAINT fk_empleado_proyecto_proyecto
FOREIGN KEY (proyecto_id) REFERENCES proyecto(proyecto_id);

ALTER TABLE registro_de_tiempo
ADD CONSTRAINT fk_registro_tiempo_empleado
FOREIGN KEY (empleado_id) REFERENCES empleado(empleado_id);

-- Crear índices para mejorar el rendimiento
CREATE INDEX idx_empleado_departamento ON empleado(departamento_id);
CREATE INDEX idx_empleado_proyecto ON empleado_proyecto(empleado_id, proyecto_id);
CREATE INDEX idx_registro_empleado ON registro_de_tiempo(empleado_id);

CREATE TABLE usuarios (
    usuario_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_usuario VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    rol ENUM('admin', 'empleado') DEFAULT 'empleado' NOT NULL
);

CREATE TABLE registro_indicadores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_indicador VARCHAR(50) NOT NULL,
    fecha_valor DATE NOT NULL,
    valor DECIMAL(10, 2) NOT NULL,
    fecha_consulta DATETIME NOT NULL,
    usuario_id INT NOT NULL,
    url_fuente VARCHAR(255) NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```