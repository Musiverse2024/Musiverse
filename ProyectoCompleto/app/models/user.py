# app/models/user.py
from utils.db_utils import get_db_connection, close_db_connection
from mysql.connector import Error

class Usuario:
    def __init__(self, id, nombre, apellido, correo_electronico, fecha_nacimiento, 
                 nombre_usuario, clave, dni):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo_electronico = correo_electronico
        self.fecha_nacimiento = fecha_nacimiento
        self.nombre_usuario = nombre_usuario
        self.clave = clave
        self.dni = dni

    @classmethod
    def obtener(cls, id_usuario):
        """Obtiene un usuario por su ID"""
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM Usuario WHERE id = %s"
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

    def __repr__(self):
        return f"Usuario(id={self.id}, nombre='{self.nombre}', apellido='{self.apellido}', " \
               f"correo_electronico='{self.correo_electronico}', " \
               f"fecha_nacimiento='{self.fecha_nacimiento}', " \
               f"nombre_usuario='{self.nombre_usuario}', clave='{self.clave}', " \
               f"dni='{self.dni}')"

    def to_dict(self):
        """Convierte el usuario a diccionario"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'correo_electronico': self.correo_electronico,
            'fecha_nacimiento': self.fecha_nacimiento,
            'nombre_usuario': self.nombre_usuario,
            'clave': self.clave,
            'dni': self.dni
        }
