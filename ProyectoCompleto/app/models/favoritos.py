from utils.db_utils import get_db_connection, close_db_connection
from mysql.connector import Error

class Favoritos:
    def __init__(self, id_usuario, id_cancion):
        self.id_usuario = id_usuario
        self.id_cancion = id_cancion

    def __str__(self):
        return f"Favoritos: Usuario ID {self.id_usuario}, Canción ID {self.id_cancion}"

    def to_dict(self):
        return {
            'id_usuario': self.id_usuario,
            'id_cancion': self.id_cancion
        } 