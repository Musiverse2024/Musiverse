# app/models/song.py

from utils.db_utils import get_db_connection, close_db_connection
from mysql.connector import Error

class Cancion:
    def __init__(self, id, nombre, id_album, id_genero, nombre_album=None, nombre_genero=None, 
                 nombre_artista=None, fecha_lanzamiento=None, **kwargs):
        """
        Inicializa una canción con información completa
        Incluye campos relacionados de Album, GeneroMusical y Artistas
        """
        self.id = id
        self.nombre = nombre
        self.id_album = id_album
        self.id_genero = id_genero
        # Campos relacionados opcionales
        self.nombre_album = nombre_album
        self.nombre_genero = nombre_genero
        self.nombre_artista = nombre_artista
        self.fecha_lanzamiento = fecha_lanzamiento

    def __str__(self):
        """Representación en string de la canción con información relacionada"""
        detalles = [
            f"Canción: {self.nombre}",
            f"Álbum: {self.nombre_album or 'N/A'}",
            f"Género: {self.nombre_genero or 'N/A'}"
        ]
        if self.nombre_artista:
            detalles.append(f"Artista: {self.nombre_artista}")
        return " | ".join(detalles)

    def to_dict(self):
        """
        Convierte la canción a diccionario incluyendo información relacionada
        """
        return {
            'id': self.id,
            'nombre': self.nombre,
            'id_album': self.id_album,
            'id_genero': self.id_genero,
            'nombre_album': self.nombre_album,
            'nombre_genero': self.nombre_genero,
            'nombre_artista': self.nombre_artista,
            'fecha_lanzamiento': self.fecha_lanzamiento
        }

    @classmethod
    def crear(cls, nombre, id_album, id_genero):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """INSERT INTO Canciones (nombre, id_album, id_genero) 
                           VALUES (%s, %s, %s)"""
                cursor.execute(query, (nombre, id_album, id_genero))
                connection.commit()
                id_cancion = cursor.lastrowid
                return cls(id_cancion, nombre, id_album, id_genero)
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
                query = "SELECT * FROM Canciones WHERE id = %s"
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
                query = """UPDATE Canciones SET nombre = %s, id_album = %s, id_genero = %s 
                           WHERE id = %s"""
                cursor.execute(query, (self.nombre, self.id_album, self.id_genero, 
                                       self.id,))
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
                query = "DELETE FROM Canciones WHERE id = %s"
                cursor.execute(query, (self.id,))
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
                query = "SELECT * FROM cancion WHERE nombre LIKE %s"
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

