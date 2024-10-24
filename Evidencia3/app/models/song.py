# app/models/song.py

from utils.db_utils import get_db_connection, close_db_connection
from mysql.connector import Error

class Cancion:
    def __init__(self, id_cancion, titulo, duracion, genero, id_album, id_artista):
        self.id_cancion = id_cancion
        self.titulo = titulo
        self.duracion = duracion
        self.genero = genero
        self.id_album = id_album
        self.id_artista = id_artista

    def __str__(self):
        return f"Canción: {self.titulo}, Duración: {self.duracion}, Género: {self.genero}"

    @classmethod
    def crear(cls, titulo, duracion, genero, id_album, id_artista):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """INSERT INTO cancion (titulo, duracion, genero, id_album, id_artista) 
                           VALUES (%s, %s, %s, %s, %s)"""
                cursor.execute(query, (titulo, duracion, genero, id_album, id_artista))
                connection.commit()
                id_cancion = cursor.lastrowid
                return cls(id_cancion, titulo, duracion, genero, id_album, id_artista)
            except Error as e:
                print(f"Error al crear canción: {e}")
                return None
            finally:
                close_db_connection(connection)
        return None

    @classmethod
    def obtener(cls, id_cancion):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM cancion WHERE id_cancion = %s"
                cursor.execute(query, (id_cancion,))
                result = cursor.fetchone()
                if result:
                    return cls(**result)
                return None
            except Error as e:
                print(f"Error al obtener canción: {e}")
                return None
            finally:
                close_db_connection(connection)
        return None

    def actualizar(self):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """UPDATE cancion SET titulo = %s, duracion = %s, genero = %s, 
                           id_album = %s, id_artista = %s WHERE id_cancion = %s"""
                cursor.execute(query, (self.titulo, self.duracion, self.genero, 
                                       self.id_album, self.id_artista, self.id_cancion))
                connection.commit()
                return cursor.rowcount > 0
            except Error as e:
                print(f"Error al actualizar canción: {e}")
                return False
            finally:
                close_db_connection(connection)
        return False

    def eliminar(self):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "DELETE FROM cancion WHERE id_cancion = %s"
                cursor.execute(query, (self.id_cancion,))
                connection.commit()
                return cursor.rowcount > 0
            except Error as e:
                print(f"Error al eliminar canción: {e}")
                return False
            finally:
                close_db_connection(connection)
        return False

    @classmethod
    def listar_todos(cls):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM cancion"
                cursor.execute(query)
                results = cursor.fetchall()
                return [cls(**row) for row in results]
            except Error as e:
                print(f"Error al listar canciones: {e}")
                return []
            finally:
                close_db_connection(connection)
        return []

    @classmethod
    def buscar_por_titulo(cls, titulo):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM cancion WHERE titulo LIKE %s"
                cursor.execute(query, (f"%{titulo}%",))
                results = cursor.fetchall()
                return [cls(**row) for row in results]
            except Error as e:
                print(f"Error al buscar canciones por título: {e}")
                return []
            finally:
                close_db_connection(connection)
        return []

    @classmethod
    def buscar_por_artista(cls, id_artista):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM cancion WHERE id_artista = %s"
                cursor.execute(query, (id_artista,))
                results = cursor.fetchall()
                return [cls(**row) for row in results]
            except Error as e:
                print(f"Error al buscar canciones por artista: {e}")
                return []
            finally:
                close_db_connection(connection)
        return []

