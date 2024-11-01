# app/services/album_service.py
from models.album import Album
from validaciones.album_validaciones import AlbumValidaciones
from utils.db_utils import get_db_connection, close_db_connection
from mysql.connector import Error
from utils.base_service import ValidationError

class AlbumService:
    @classmethod
    def crear_album(cls, nombre, id_artista, fecha_lanzamiento):
        """Crea un nuevo álbum"""
        try:
            validador = AlbumValidaciones()
            validador.validate({
                'nombre': nombre,
                'id_artista': id_artista,
                'fecha_lanzamiento': fecha_lanzamiento
            })
            
            connection = get_db_connection()
            if connection:
                try:
                    cursor = connection.cursor()
                    query = """
                        INSERT INTO Album (nombre, id_artista, fecha_lanzamiento) 
                        VALUES (%s, %s, %s)
                    """
                    cursor.execute(query, (nombre, id_artista, fecha_lanzamiento))
                    connection.commit()
                    return Album(cursor.lastrowid, nombre, fecha_lanzamiento, id_artista)
                finally:
                    close_db_connection(connection)
        except ValidationError as e:
            print(f"Error de validación: {str(e)}")
            raise
        except Error as e:
            print(f"Error de base de datos: {str(e)}")
        return None

    @classmethod
    def obtener_album(cls, id_album):
        """Obtiene un álbum por su ID"""
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = """
                    SELECT a.*, art.nombre as nombre_artista 
                    FROM Album a
                    LEFT JOIN Artistas art ON a.id_artista = art.id
                    WHERE a.id = %s
                """
                cursor.execute(query, (id_album,))
                result = cursor.fetchone()
                if result:
                    return Album(**result)
            except Error as e:
                print(f"Error al obtener álbum: {e}")
            finally:
                close_db_connection(connection)
        return None

    @classmethod
    def actualizar_album(cls, id_album, nombre, fecha_lanzamiento):
        """Actualiza un álbum existente"""
        try:
            validador = AlbumValidaciones()
            validador.validate({
                'nombre': nombre,
                'fecha_lanzamiento': fecha_lanzamiento
            })
            
            connection = get_db_connection()
            if connection:
                try:
                    cursor = connection.cursor()
                    query = "UPDATE Album SET nombre = %s, fecha_lanzamiento = %s WHERE id = %s"
                    cursor.execute(query, (nombre, fecha_lanzamiento, id_album))
                    connection.commit()
                    return True
                finally:
                    close_db_connection(connection)
        except ValidationError as e:
            print(f"Error de validación: {str(e)}")
            raise
        except Error as e:
            print(f"Error de base de datos: {str(e)}")
        return False

    @classmethod
    def eliminar_album(cls, id_album):
        """Elimina un álbum"""
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "DELETE FROM Album WHERE id = %s"
                cursor.execute(query, (id_album,))
                connection.commit()
                return True
            except Error as e:
                print(f"Error al eliminar álbum: {e}")
                return False
            finally:
                close_db_connection(connection)
        return False

    @classmethod
    def buscar_por_titulo(cls, titulo):
        """Busca álbumes por título"""
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = """
                    SELECT a.*, art.nombre as nombre_artista 
                    FROM Album a
                    LEFT JOIN Artistas art ON a.id_artista = art.id
                    WHERE a.nombre LIKE %s
                """
                cursor.execute(query, (f"%{titulo}%",))
                results = cursor.fetchall()
                return [Album(**result) for result in results]
            except Error as e:
                print(f"Error al buscar álbumes: {e}")
            finally:
                close_db_connection(connection)
        return []

    @classmethod
    def listar_albumes(cls):
        """Lista todos los álbumes con información del artista"""
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = """
                    SELECT a.*, art.nombre as nombre_artista 
                    FROM Album a
                    LEFT JOIN Artistas art ON a.id_artista = art.id
                """
                cursor.execute(query)
                results = cursor.fetchall()
                return [Album(**result) for result in results]
            except Error as e:
                print(f"Error al listar álbumes: {e}")
            finally:
                close_db_connection(connection)
        return []

    @classmethod
    def buscar_albumes_por_artista(cls, id_artista):
        """Busca álbumes por artista"""
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = """
                    SELECT a.*, art.nombre as nombre_artista 
                    FROM Album a
                    LEFT JOIN Artistas art ON a.id_artista = art.id
                    WHERE a.id_artista = %s
                """
                cursor.execute(query, (id_artista,))
                results = cursor.fetchall()
                return [Album(**result) for result in results]
            except Error as e:
                print(f"Error al buscar álbumes por artista: {e}")
            finally:
                close_db_connection(connection)
        return []

    @classmethod
    def contar_albumes(cls):
        """Cuenta el total de álbumes"""
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = """
                    SELECT COUNT(*) FROM Album
                """
                cursor.execute(query)
                result = cursor.fetchone()
                return result['COUNT(*)']
            except Error as e:
                print(f"Error al contar álbumes: {e}")
            finally:
                close_db_connection(connection)
        return 0

    @classmethod
    def listar_albumes_paginados(cls, pagina, por_pagina):
        """Lista álbumes con paginación"""
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = """
                    SELECT a.*, art.nombre as nombre_artista 
                    FROM Album a
                    LEFT JOIN Artistas art ON a.id_artista = art.id
                    LIMIT %s OFFSET %s
                """
                cursor.execute(query, (por_pagina, (pagina - 1) * por_pagina))
                results = cursor.fetchall()
                return [Album(**result) for result in results]
            except Error as e:
                print(f"Error al listar álbumes paginados: {e}")
            finally:
                close_db_connection(connection)
        return []

