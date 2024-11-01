from utils.db_utils import get_db_connection, close_db_connection
from mysql.connector import Error
from datetime import datetime

class HistorialReproduccion:
    def __init__(self, id, id_usuario, id_cancion, fecha_reproduccion):
        self.id = id
        self.id_usuario = id_usuario
        self.id_cancion = id_cancion
        self.fecha_reproduccion = fecha_reproduccion

    def __str__(self):
        return f"HistorialReproduccion: ID {self.id}, Usuario ID {self.id_usuario}, Canción ID {self.id_cancion}, Fecha {self.fecha_reproduccion}"

    def to_dict(self):
        return {
            'id': self.id,
            'id_usuario': self.id_usuario,
            'id_cancion': self.id_cancion,
            'fecha_reproduccion': self.fecha_reproduccion
        } 