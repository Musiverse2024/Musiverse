from utils.db_utils import get_db_connection, close_db_connection
from mysql.connector import Error

class UsuarioGenero:
    def __init__(self, id_usuario, id_genero):
        self.id_usuario = id_usuario
        self.id_genero = id_genero

    def __str__(self):
        return f"UsuarioGenero: Usuario ID {self.id_usuario}, Género ID {self.id_genero}"

    def __repr__(self):
        return f"UsuarioGenero(id_usuario={self.id_usuario}, id_genero={self.id_genero})"

    def to_dict(self):
        return {
            'id_usuario': self.id_usuario,
            'id_genero': self.id_genero
        }

    # Agregar método para obtener información completa
    def obtener_info_completa(self):
        """
        Obtiene información detallada de la relación usuario-género
        """
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = """
                    SELECT u.nombre as nombre_usuario, g.nombre as nombre_genero
                    FROM Usuario u
                    JOIN UsuarioGenero ug ON u.id = ug.id_usuario
                    JOIN GeneroMusical g ON g.id = ug.id_genero
                    WHERE ug.id_usuario = %s AND ug.id_genero = %s
                """
                cursor.execute(query, (self.id_usuario, self.id_genero))
                return cursor.fetchone()
            except Error as e:
                print(f"Error al obtener información completa: {e}")
                return None
            finally:
                close_db_connection(connection)
        return None