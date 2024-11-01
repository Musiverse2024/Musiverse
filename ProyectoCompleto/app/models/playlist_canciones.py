from utils.db_utils import get_db_connection, close_db_connection
from mysql.connector import Error

class PlaylistCanciones:
    def __init__(self, id_playlist, id_cancion):
        self.id_playlist = id_playlist
        self.id_cancion = id_cancion

    def __str__(self):
        return f"PlaylistCanciones: Playlist ID {self.id_playlist}, Canción ID {self.id_cancion}"

    def to_dict(self):
        return {
            'id_playlist': self.id_playlist,
            'id_cancion': self.id_cancion
        } 