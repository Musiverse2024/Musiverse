from models.historial_reproduccion import HistorialReproduccion
from utils.db_utils import get_db_connection, close_db_connection
from mysql.connector import Error
from datetime import datetime

class HistorialReproduccionService:
    @staticmethod
    def registrar_reproduccion(id_usuario, id_cancion):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                fecha_actual = datetime.now()
                query = """
                    INSERT INTO HistorialReproduccion 
                    (id_usuario, id_cancion, fecha_reproduccion) 
                    VALUES (%s, %s, %s)
                """
                cursor.execute(query, (id_usuario, id_cancion, fecha_actual))
                connection.commit()
                id_historial = cursor.lastrowid
                return HistorialReproduccion(id_historial, id_usuario, id_cancion, fecha_actual)
            except Error as e:
                print(f"Error al registrar reproducción: {e}")
                return None
            finally:
                close_db_connection(connection)
        return None

    @staticmethod
    def obtener_historial_usuario(id_usuario, limite=10):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = """
                    SELECT h.*, c.nombre as nombre_cancion 
                    FROM HistorialReproduccion h
                    JOIN Canciones c ON h.id_cancion = c.id
                    WHERE h.id_usuario = %s
                    ORDER BY h.fecha_reproduccion DESC
                    LIMIT %s
                """
                cursor.execute(query, (id_usuario, limite))
                return cursor.fetchall()
            except Error as e:
                print(f"Error al obtener historial: {e}")
                return []
            finally:
                close_db_connection(connection)
        return []

    @staticmethod
    def limpiar_historial(id_usuario):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "DELETE FROM HistorialReproduccion WHERE id_usuario = %s"
                cursor.execute(query, (id_usuario,))
                connection.commit()
                return cursor.rowcount > 0
            except Error as e:
                print(f"Error al limpiar historial: {e}")
                return False
            finally:
                close_db_connection(connection)
        return False 