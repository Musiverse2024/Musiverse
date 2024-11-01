from models.favoritos import Favoritos
from utils.db_utils import get_db_connection, close_db_connection
from mysql.connector import Error

class FavoritosService:
    @staticmethod
    def agregar_favorito(id_usuario, id_cancion):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                # Verificar si ya existe
                verify_query = """
                    SELECT 1 FROM Favoritos 
                    WHERE id_usuario = %s AND id_cancion = %s
                """
                cursor.execute(verify_query, (id_usuario, id_cancion))
                if cursor.fetchone():
                    print("La canción ya está en favoritos")
                    return None

                query = "INSERT INTO Favoritos (id_usuario, id_cancion) VALUES (%s, %s)"
                cursor.execute(query, (id_usuario, id_cancion))
                connection.commit()
                return Favoritos(id_usuario, id_cancion)
            except Error as e:
                print(f"Error al agregar favorito: {e}")
                return None
            finally:
                close_db_connection(connection)
        return None

    @staticmethod
    def eliminar_favorito(id_usuario, id_cancion):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "DELETE FROM Favoritos WHERE id_usuario = %s AND id_cancion = %s"
                cursor.execute(query, (id_usuario, id_cancion))
                connection.commit()
                return cursor.rowcount > 0
            except Error as e:
                print(f"Error al eliminar favorito: {e}")
                return False
            finally:
                close_db_connection(connection)
        return False

    @staticmethod
    def obtener_favoritos_usuario(id_usuario):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = """
                    SELECT c.* FROM Canciones c
                    JOIN Favoritos f ON c.id = f.id_cancion
                    WHERE f.id_usuario = %s
                """
                cursor.execute(query, (id_usuario,))
                return cursor.fetchall()
            except Error as e:
                print(f"Error al obtener favoritos: {e}")
                return []
            finally:
                close_db_connection(connection)
        return [] 