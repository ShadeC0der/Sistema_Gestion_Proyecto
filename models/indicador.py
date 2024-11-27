"""
Modelo para la tabla registro_indicadores.
"""

class Indicador:
    """
    Modelo para representar un registro de indicador económico.
    """

    def __init__(self, id=None, nombre_indicador=None, fecha_valor=None, valor=None, fecha_consulta=None, usuario_id=None, url_fuente=None):
        self.id = id
        self.nombre_indicador = nombre_indicador
        self.fecha_valor = fecha_valor
        self.valor = valor
        self.fecha_consulta = fecha_consulta
        self.usuario_id = usuario_id
        self.url_fuente = url_fuente

    def __repr__(self):
        return (
            f"Indicador(id={self.id}, nombre_indicador={self.nombre_indicador}, "
            f"fecha_valor={self.fecha_valor}, valor={self.valor}, "
            f"fecha_consulta={self.fecha_consulta}, usuario_id={self.usuario_id}, url_fuente={self.url_fuente})"
        )
