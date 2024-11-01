# app/models/album.py

from utils.db_utils import get_db_connection, close_db_connection
from mysql.connector import Error

class Album:
    def __init__(self, id, nombre, fecha_lanzamiento, id_artista, nombre_artista=None):
        """
        Inicializa un álbum con sus atributos básicos y opcionales
        """
        self.id = id
        self.nombre = nombre
        self.fecha_lanzamiento = fecha_lanzamiento
        self.id_artista = id_artista
        self.nombre_artista = nombre_artista

    def __str__(self):
        """Representación en string del álbum"""
        artista = f" - {self.nombre_artista}" if self.nombre_artista else ""
        return f"Álbum: {self.nombre}{artista}, Fecha: {self.fecha_lanzamiento}"

    def to_dict(self):
        """Convierte el álbum a diccionario"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'fecha_lanzamiento': self.fecha_lanzamiento,
            'id_artista': self.id_artista,
            'nombre_artista': self.nombre_artista
        }
