"""
Controlador para generar informes basados en datos de empleados, departamentos,
proyectos y registros de tiempo.
"""

import pandas as pd
from controllers.empleado_controller import EmpleadoController
from controllers.departamento_controller import DepartamentoController
from controllers.proyecto_controller import ProyectoController
from controllers.registro_tiempo_controller import RegistroDeTiempoController


class InformesController:
    """
    Controlador para generar informes en formato Excel.
    """

    def __init__(self):
        self.empleado_controller = EmpleadoController()
        self.departamento_controller = DepartamentoController()
        self.proyecto_controller = ProyectoController()
        self.registro_tiempo_controller = RegistroDeTiempoController()

    def generar_informe_empleados(self):
        """
        Genera un informe de empleados en formato Excel.
        """
        empleados = self.empleado_controller.listar_empleados()
        if not empleados:
            print("No hay empleados disponibles para generar el informe.")
            return

        # Convertir objetos a diccionarios
        empleados_dict = [empleado.__dict__ for empleado in empleados]
        df = pd.DataFrame(empleados_dict)
        df.columns = ['ID', 'RUT', 'Nombre', 'Dirección', 'Teléfono', 'Email',
                      'Fecha Inicio', 'Salario', 'Departamento ID'] 
        df.to_excel('informe_empleados.xlsx', index=False)
        print("Informe de empleados generado exitosamente en 'informe_empleados.xlsx'.")

    def generar_informe_departamentos(self):
        """
        Genera un informe de departamentos en formato Excel.
        """
        departamentos = self.departamento_controller.listar_departamentos()
        if not departamentos:
            print("No hay departamentos disponibles para generar el informe.")
            return

        departamentos_dict = [departamento.__dict__ for departamento in departamentos]
        df = pd.DataFrame(departamentos_dict)
        df.columns = ['ID', 'Nombre', 'Gerente ID']
        df.to_excel('informe_departamentos.xlsx', index=False)
        print("Informe de departamentos generado exitosamente en 'informe_departamentos.xlsx'.")

    def generar_informe_proyectos(self):
        """
        Genera un informe de proyectos en formato Excel.
        """
        proyectos = self.proyecto_controller.listar_proyectos()
        if not proyectos:
            print("No hay proyectos disponibles para generar el informe.")
            return

        proyectos_dict = [proyecto.__dict__ for proyecto in proyectos]
        df = pd.DataFrame(proyectos_dict)
        df.columns = ['ID', 'Nombre', 'Descripción', 'Fecha Inicio']
        df.to_excel('informe_proyectos.xlsx', index=False)
        print("Informe de proyectos generado exitosamente en 'informe_proyectos.xlsx'.")

    def generar_informe_registros_tiempo(self):
        """
        Genera un informe de registros de tiempo en formato Excel.
        """
        registros = self.registro_tiempo_controller.listar_registros()
        if not registros:
            print("No hay registros de tiempo disponibles para generar el informe.")
            return

        registros_dict = [registro.__dict__ for registro in registros]
        df = pd.DataFrame(registros_dict)
        df.columns = ['ID', 'Fecha', 'Horas Trabajadas', 'Descripción', 'Empleado ID']
        df.to_excel('informe_registros_tiempo.xlsx', index=False)
        # pylint: disable=line-too-long
        print("Informe de registros de tiempo generado exitosamente en 'informe_registros_tiempo.xlsx'.")
