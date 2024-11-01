from models.usuario_genero import UsuarioGenero
from models.user import Usuario
from utils.db_utils import get_db_connection, close_db_connection
from mysql.connector import Error

class UsuarioGeneroService:
    @staticmethod
    def agregar_genero(id_usuario, id_genero):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                
                # Verificar que el usuario existe
                user_query = "SELECT * FROM Usuario WHERE id = %s"
                cursor.execute(user_query, (id_usuario,))
                usuario = cursor.fetchone()
                if not usuario:
                    print(f"No existe un usuario con ID {id_usuario}")
                    return None

                # Verificar que el género existe
                genero_query = "SELECT nombre FROM GeneroMusical WHERE id = %s"
                cursor.execute(genero_query, (id_genero,))
                genero = cursor.fetchone()
                if not genero:
                    print(f"No existe un género musical con ID {id_genero}")
                    return None

                # Verificar si ya existe la relación
                verify_query = """
                    SELECT 1 FROM UsuarioGenero 
                    WHERE id_usuario = %s AND id_genero = %s
                """
                cursor.execute(verify_query, (id_usuario, id_genero))
                if cursor.fetchone():
                    print(f"El usuario ya tiene asignado este género")
                    return None

                # Insertar la nueva relación
                insert_query = "INSERT INTO UsuarioGenero (id_usuario, id_genero) VALUES (%s, %s)"
                cursor.execute(insert_query, (id_usuario, id_genero))
                connection.commit()
                
                return UsuarioGenero(id_usuario, id_genero)
            except Error as e:
                print(f"Error al agregar género a usuario: {e}")
                return None
            finally:
                close_db_connection(connection)
        return None

    @staticmethod
    def eliminar_genero(id_usuario, id_genero):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "DELETE FROM UsuarioGenero WHERE id_usuario = %s AND id_genero = %s"
                cursor.execute(query, (id_usuario, id_genero))
                connection.commit()
                return cursor.rowcount > 0
            except Error as e:
                print(f"Error al eliminar género de usuario: {e}")
                return False
            finally:
                close_db_connection(connection)
        return False

    @staticmethod
    def obtener_generos_usuario(id_usuario):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = """
                    SELECT g.* FROM GeneroMusical g
                    JOIN UsuarioGenero ug ON g.id = ug.id_genero
                    WHERE ug.id_usuario = %s
                """
                cursor.execute(query, (id_usuario,))
                return cursor.fetchall()
            except Error as e:
                print(f"Error al obtener géneros del usuario: {e}")
                return []
            finally:
                close_db_connection(connection)
        return [] 