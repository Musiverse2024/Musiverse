# app/services/artist_service.py
from models.artist import Artista
from validaciones.artist_validaciones import ArtistValidaciones
from utils.db_utils import get_db_connection, close_db_connection
from mysql.connector import Error

class ArtistService:
    @classmethod
    def crear_artista(cls, nombre):
        """Crea un nuevo artista"""
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "INSERT INTO Artistas (nombre) VALUES (%s)"
                cursor.execute(query, (nombre,))
                connection.commit()
                return Artista(cursor.lastrowid, nombre)
            except Error as e:
                print(f"Error al crear artista: {e}")
            finally:
                close_db_connection(connection)
        return None

    @classmethod
    def obtener_artista(cls, id_artista):
        """Obtiene un artista por su ID"""
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM Artistas WHERE id = %s"
                cursor.execute(query, (id_artista,))
                result = cursor.fetchone()
                if result:
                    return Artista(**result)
            except Error as e:
                print(f"Error al obtener artista: {e}")
            finally:
                close_db_connection(connection)
        return None

    @classmethod
    def actualizar_artista(cls, id_artista, nuevo_nombre):
        """Actualiza un artista existente"""
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "UPDATE Artistas SET nombre = %s WHERE id = %s"
                cursor.execute(query, (nuevo_nombre, id_artista))
                connection.commit()
                return True
            except Error as e:
                print(f"Error al actualizar artista: {e}")
            finally:
                close_db_connection(connection)
        return False

    @classmethod
    def eliminar_artista(cls, id_artista):
        """Elimina un artista"""
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "DELETE FROM Artistas WHERE id = %s"
                cursor.execute(query, (id_artista,))
                connection.commit()
                return True
            except Error as e:
                print(f"Error al eliminar artista: {e}")
            finally:
                close_db_connection(connection)
        return False

    @classmethod
    def listar_artistas(cls):
        """Lista todos los artistas"""
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM Artistas"
                cursor.execute(query)
                results = cursor.fetchall()
                return [Artista(**result) for result in results]
            except Error as e:
                print(f"Error al listar artistas: {e}")
            finally:
                close_db_connection(connection)
        return []

    @classmethod
    def buscar_por_nombre(cls, nombre):
        """Busca artistas por nombre"""
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM Artistas WHERE nombre LIKE %s"
                cursor.execute(query, (f"%{nombre}%",))
                results = cursor.fetchall()
                return [Artista(**result) for result in results]
            except Error as e:
                print(f"Error al buscar artistas: {e}")
            finally:
                close_db_connection(connection)
        return []

    @classmethod
    def contar_artistas(cls):
        """Cuenta el total de artistas"""
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "SELECT COUNT(*) FROM Artistas"
                cursor.execute(query)
                result = cursor.fetchone()
                return result[0] if result else 0
            except Error as e:
                print(f"Error al contar artistas: {e}")
            finally:
                close_db_connection(connection)
        return 0

# Implementa aquí las demás funciones de servicio para artistas



