# app/services/song_service.py
from models.song import Cancion
from validaciones.song_validaciones import SongValidaciones
from utils.db_utils import get_db_connection, close_db_connection
from mysql.connector import Error

class SongService:
    @classmethod
    def crear_cancion(cls, nombre, id_album, id_genero):
        """Crea una nueva canción"""
        try:
            # Crear instancia del validador y validar datos
            validador = SongValidaciones()
            datos = {
                'nombre': nombre,
                'id_album': id_album,
                'id_genero': id_genero
            }
            validador.validate(datos)
            
            connection = get_db_connection()
            if connection:
                try:
                    cursor = connection.cursor()
                    query = """INSERT INTO Canciones (nombre, id_album, id_genero) 
                              VALUES (%s, %s, %s)"""
                    cursor.execute(query, (nombre, id_album, id_genero))
                    connection.commit()
                    return Cancion(cursor.lastrowid, nombre, id_album, id_genero)
                finally:
                    close_db_connection(connection)
        except Exception as e:
            print(f"Error al crear canción: {str(e)}")
        return None

    @classmethod
    def obtener_cancion(cls, id_cancion):
        """Obtiene una canción por su ID"""
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = """
                    SELECT c.*, a.nombre as nombre_album, g.nombre as nombre_genero 
                    FROM Canciones c
                    LEFT JOIN Album a ON c.id_album = a.id
                    LEFT JOIN GeneroMusical g ON c.id_genero = g.id
                    WHERE c.id = %s
                """
                cursor.execute(query, (id_cancion,))
                result = cursor.fetchone()
                if result:
                    return Cancion(**result)
                return None
            finally:
                close_db_connection(connection)
        return None

    @classmethod
    def actualizar_cancion(cls, cancion):
        """Actualiza una canción existente"""
        try:
            SongValidaciones.validar_cancion_completa(
                cancion.nombre, cancion.id_album, cancion.id_genero
            )
            connection = get_db_connection()
            if connection:
                try:
                    cursor = connection.cursor()
                    query = """UPDATE Canciones 
                              SET nombre = %s, id_album = %s, id_genero = %s 
                              WHERE id = %s"""
                    cursor.execute(query, (
                        cancion.nombre, cancion.id_album, 
                        cancion.id_genero, cancion.id
                    ))
                    connection.commit()
                    return cursor.rowcount > 0
                finally:
                    close_db_connection(connection)
        except Exception as e:
            print(f"Error al actualizar canción: {str(e)}")
        return False

    @classmethod
    def eliminar_cancion(cls, id_cancion):
        """Elimina una canción y sus referencias"""
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                # Primero eliminar referencias en tablas relacionadas
                tablas_relacionadas = [
                    "PlaylistCanciones",
                    "Favoritos",
                    "HistorialReproduccion"
                ]
                for tabla in tablas_relacionadas:
                    cursor.execute(f"DELETE FROM {tabla} WHERE id_cancion = %s", (id_cancion,))
                
                # Luego eliminar la canción
                cursor.execute("DELETE FROM Canciones WHERE id = %s", (id_cancion,))
                connection.commit()
                return cursor.rowcount > 0
            finally:
                close_db_connection(connection)
        return False

    @classmethod
    def listar_canciones(cls):
        """Lista todas las canciones con información relacionada"""
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = """
                    SELECT c.*, a.nombre as nombre_album, g.nombre as nombre_genero
                    FROM Canciones c
                    LEFT JOIN Album a ON c.id_album = a.id
                    LEFT JOIN GeneroMusical g ON c.id_genero = g.id
                """
                cursor.execute(query)
                results = cursor.fetchall()
                return [Cancion(**row) for row in results]
            finally:
                close_db_connection(connection)
        return []

    @classmethod
    def buscar_por_nombre(cls, nombre):
        """Busca canciones por nombre"""
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = """
                    SELECT c.*, a.nombre as nombre_album, g.nombre as nombre_genero
                    FROM Canciones c
                    LEFT JOIN Album a ON c.id_album = a.id
                    LEFT JOIN GeneroMusical g ON c.id_genero = g.id
                    WHERE c.nombre LIKE %s
                """
                cursor.execute(query, (f"%{nombre}%",))
                results = cursor.fetchall()
                return [Cancion(**row) for row in results]
            finally:
                close_db_connection(connection)
        return []

    @classmethod
    def listar_canciones_por_artista(cls, id_artista):
        """Lista todas las canciones de un artista específico"""
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = """
                    SELECT c.*, alb.nombre as nombre_album, g.nombre as nombre_genero,
                           art.nombre as nombre_artista
                    FROM Canciones c
                    INNER JOIN Album alb ON c.id_album = alb.id
                    INNER JOIN Artistas art ON alb.id_artista = art.id
                    LEFT JOIN GeneroMusical g ON c.id_genero = g.id
                    WHERE art.id = %s
                """
                cursor.execute(query, (id_artista,))
                results = cursor.fetchall()
                return [Cancion(**row) for row in results]
            except Error as e:
                print(f"Error al listar canciones del artista: {e}")
            finally:
                close_db_connection(connection)
        return []

    @classmethod
    def listar_canciones_por_album(cls, id_album):
        """Lista todas las canciones de un álbum específico"""
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = """
                    SELECT c.*, a.nombre as nombre_album, g.nombre as nombre_genero
                    FROM Canciones c
                    LEFT JOIN Album a ON c.id_album = a.id
                    LEFT JOIN GeneroMusical g ON c.id_genero = g.id
                    WHERE c.id_album = %s
                """
                cursor.execute(query, (id_album,))
                results = cursor.fetchall()
                return [Cancion(**row) for row in results]
            finally:
                close_db_connection(connection)
        return []

    # Métodos interactivos...
    # (El resto de los métodos interactivos se mantienen igual)


