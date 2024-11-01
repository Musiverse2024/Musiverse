from utils.db_utils import get_db_connection, close_db_connection
from mysql.connector import Error
from models.playlist import Playlist
from models.song import Cancion
from models.playlist_canciones import PlaylistCanciones

class PlaylistService:
    # Métodos principales de Playlist
    @staticmethod
    def crear_playlist(nombre, id_usuario):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "INSERT INTO Playlist (nombre, id_usuario) VALUES (%s, %s)"
                cursor.execute(query, (nombre, id_usuario))
                connection.commit()
                id_playlist = cursor.lastrowid
                return Playlist(id_playlist, nombre, id_usuario)
            except Error as e:
                print(f"Error al crear playlist: {e}")
                return None
            finally:
                close_db_connection(connection)
        return None

    @staticmethod
    def obtener_playlist(id_playlist):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM Playlist WHERE id = %s"
                cursor.execute(query, (id_playlist,))
                result = cursor.fetchone()
                if result:
                    return Playlist(**result)
                return None
            except Error as e:
                print(f"Error al obtener playlist: {e}")
                return None
            finally:
                close_db_connection(connection)
        return None

    @staticmethod
    def actualizar_playlist(playlist):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "UPDATE Playlist SET nombre = %s, id_usuario = %s WHERE id = %s"
                cursor.execute(query, (playlist.nombre, playlist.id_usuario, playlist.id))
                connection.commit()
                return cursor.rowcount > 0
            except Error as e:
                print(f"Error al actualizar playlist: {e}")
                return False
            finally:
                close_db_connection(connection)
        return False

    @staticmethod
    def eliminar_playlist(id_playlist):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                # Primero eliminamos las relaciones en PlaylistCanciones
                query_rel = "DELETE FROM PlaylistCanciones WHERE id_playlist = %s"
                cursor.execute(query_rel, (id_playlist,))
                
                # Luego eliminamos la playlist
                query = "DELETE FROM Playlist WHERE id = %s"
                cursor.execute(query, (id_playlist,))
                connection.commit()
                return cursor.rowcount > 0
            except Error as e:
                print(f"Error al eliminar playlist: {e}")
                return False
            finally:
                close_db_connection(connection)
        return False

    # Métodos de búsqueda y listado
    @staticmethod
    def listar_playlists():
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM Playlist"
                cursor.execute(query)
                results = cursor.fetchall()
                return [Playlist(**result) for result in results]
            except Error as e:
                print(f"Error al listar playlists: {e}")
                return []
            finally:
                close_db_connection(connection)
        return []

    @staticmethod
    def buscar_playlists_usuario(id_usuario):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM Playlist WHERE id_usuario = %s"
                cursor.execute(query, (id_usuario,))
                results = cursor.fetchall()
                return [Playlist(**result) for result in results]
            except Error as e:
                print(f"Error al buscar playlists del usuario: {e}")
                return []
            finally:
                close_db_connection(connection)
        return []

    # Métodos de gestión de canciones en playlist
    @staticmethod
    def agregar_cancion(id_playlist, id_cancion):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                # Verificar si la playlist existe
                if not PlaylistService.obtener_playlist(id_playlist):
                    print("La playlist no existe")
                    return None

                # Verificar si la canción existe
                verify_query = "SELECT id FROM Canciones WHERE id = %s"
                cursor.execute(verify_query, (id_cancion,))
                if not cursor.fetchone():
                    print("La canción no existe")
                    return None
                
                # Verificar si ya existe en la playlist
                verify_playlist_query = """
                    SELECT 1 FROM PlaylistCanciones 
                    WHERE id_playlist = %s AND id_cancion = %s
                """
                cursor.execute(verify_playlist_query, (id_playlist, id_cancion))
                if cursor.fetchone():
                    print("La canción ya está en la playlist")
                    return None

                # Agregar la canción
                query = "INSERT INTO PlaylistCanciones (id_playlist, id_cancion) VALUES (%s, %s)"
                cursor.execute(query, (id_playlist, id_cancion))
                connection.commit()
                return PlaylistCanciones(id_playlist, id_cancion)
            except Error as e:
                print(f"Error al agregar canción a playlist: {e}")
                return None
            finally:
                close_db_connection(connection)
        return None

    @staticmethod
    def eliminar_cancion(id_playlist, id_cancion):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "DELETE FROM PlaylistCanciones WHERE id_playlist = %s AND id_cancion = %s"
                cursor.execute(query, (id_playlist, id_cancion))
                connection.commit()
                return cursor.rowcount > 0
            except Error as e:
                print(f"Error al eliminar canción de playlist: {e}")
                return False
            finally:
                close_db_connection(connection)
        return False

    @staticmethod
    def obtener_canciones_playlist(id_playlist):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = """
                    SELECT c.* FROM Canciones c
                    JOIN PlaylistCanciones pc ON c.id = pc.id_cancion
                    WHERE pc.id_playlist = %s
                """
                cursor.execute(query, (id_playlist,))
                return cursor.fetchall()
            except Error as e:
                print(f"Error al obtener canciones de playlist: {e}")
                return []
            finally:
                close_db_connection(connection)
        return []

    # Nuevos métodos útiles
    @staticmethod
    def obtener_total_canciones(id_playlist):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """
                    SELECT COUNT(*) as total 
                    FROM PlaylistCanciones 
                    WHERE id_playlist = %s
                """
                cursor.execute(query, (id_playlist,))
                result = cursor.fetchone()
                return result[0] if result else 0
            except Error as e:
                print(f"Error al obtener total de canciones: {e}")
                return 0
            finally:
                close_db_connection(connection)
        return 0

    @staticmethod
    def verificar_permiso_usuario(id_playlist, id_usuario):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """
                    SELECT 1 FROM Playlist 
                    WHERE id = %s AND id_usuario = %s
                """
                cursor.execute(query, (id_playlist, id_usuario))
                return cursor.fetchone() is not None
            except Error as e:
                print(f"Error al verificar permiso: {e}")
                return False
            finally:
                close_db_connection(connection)
        return False
