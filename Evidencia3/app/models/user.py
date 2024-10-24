# app/models/user.py
from utils.db_utils import get_db_connection, close_db_connection
from mysql.connector import Error

class Usuario:
    def __init__(self, id_usuario, nombre, apellido, correo_electronico, contraseña, fecha_nacimiento, pais, ciudad):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.correo_electronico = correo_electronico
        self.contraseña = contraseña
        self.fecha_nacimiento = fecha_nacimiento
        self.pais = pais
        self.ciudad = ciudad

    def __repr__(self):
        return f"Usuario(id_usuario={self.id_usuario}, nombre='{self.nombre}', apellido='{self.apellido}', correo_electronico='{self.correo_electronico}', fecha_nacimiento='{self.fecha_nacimiento}', pais='{self.pais}', ciudad='{self.ciudad}')"

    @classmethod
    def crear(cls, nombre, apellido, correo_electronico, contraseña, fecha_nacimiento, pais, ciudad):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """INSERT INTO usuario (nombre, apellido, correo_electronico, contraseña, fecha_nacimiento, pais, ciudad) 
                           VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                cursor.execute(query, (nombre, apellido, correo_electronico, contraseña, fecha_nacimiento, pais, ciudad))
                connection.commit()
                id_usuario = cursor.lastrowid
                return cls(id_usuario, nombre, apellido, correo_electronico, contraseña, fecha_nacimiento, pais, ciudad)
            except Error as e:
                print(f"Error al crear usuario: {e}")
                return None
            finally:
                close_db_connection(connection)
        return None

    @classmethod
    def obtener(cls, id_usuario):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM usuario WHERE id_usuario = %s"
                cursor.execute(query, (id_usuario,))
                result = cursor.fetchone()
                if result:
                    return cls(**result)
                return None
            except Error as e:
                print(f"Error al obtener usuario: {e}")
                return None
            finally:
                close_db_connection(connection)
        return None

    def actualizar(self):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """UPDATE usuario SET nombre = %s, apellido = %s, correo_electronico = %s, 
                           contraseña = %s, fecha_nacimiento = %s, pais = %s, ciudad = %s 
                           WHERE id_usuario = %s"""
                cursor.execute(query, (self.nombre, self.apellido, self.correo_electronico, 
                                       self.contraseña, self.fecha_nacimiento, self.pais, 
                                       self.ciudad, self.id_usuario))
                connection.commit()
                return cursor.rowcount > 0
            except Error as e:
                print(f"Error al actualizar usuario: {e}")
                return False
            finally:
                close_db_connection(connection)
        return False

    def eliminar(self):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "DELETE FROM usuario WHERE id_usuario = %s"
                cursor.execute(query, (self.id_usuario,))
                connection.commit()
                return cursor.rowcount > 0
            except Error as e:
                print(f"Error al eliminar usuario: {e}")
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
                query = "SELECT * FROM usuario"
                cursor.execute(query)
                results = cursor.fetchall()
                return [cls(**row) for row in results]
            except Error as e:
                print(f"Error al listar usuarios: {e}")
                return []
            finally:
                close_db_connection(connection)
        return []
