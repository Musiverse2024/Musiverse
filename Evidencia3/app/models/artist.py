# app/models/artist.py

from utils.db_utils import get_db_connection, close_db_connection
from mysql.connector import Error

class Artista:
    def __init__(self, id_artista, nombre_artista):
        self.id_artista = id_artista
        self.nombre_artista = nombre_artista

    def __str__(self):
        return f"Artista: {self.nombre_artista}"

    @classmethod
    def crear(cls, nombre_artista):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "INSERT INTO artista (nombre_artista) VALUES (%s)"
                cursor.execute(query, (nombre_artista,))
                connection.commit()
                id_artista = cursor.lastrowid
                return cls(id_artista, nombre_artista)
            except Error as e:
                print(f"Error al crear artista: {e}")
                return None
            finally:
                close_db_connection(connection)
        return None

    @classmethod
    def obtener(cls, id_artista):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM artista WHERE id_artista = %s"
                cursor.execute(query, (id_artista,))
                result = cursor.fetchone()
                if result:
                    return cls(**result)
            except Error as e:
                print(f"Error al obtener artista: {e}")
            finally:
                close_db_connection(connection)
        return None

    def actualizar(self):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "UPDATE artista SET nombre_artista = %s WHERE id_artista = %s"
                cursor.execute(query, (self.nombre_artista, self.id_artista))
                connection.commit()
                return True
            except Error as e:
                print(f"Error al actualizar artista: {e}")
                return False
            finally:
                close_db_connection(connection)
        return False

    def eliminar(self):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "DELETE FROM artista WHERE id_artista = %s"
                cursor.execute(query, (self.id_artista,))
                connection.commit()
                return True
            except Error as e:
                print(f"Error al eliminar artista: {e}")
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
                query = "SELECT * FROM artista"
                cursor.execute(query)
                results = cursor.fetchall()
                return [cls(**result) for result in results]
            except Error as e:
                print(f"Error al listar artistas: {e}")
            finally:
                close_db_connection(connection)
        return []

    @classmethod
    def buscar_por_nombre(cls, nombre):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM artista WHERE nombre_artista LIKE %s"
                cursor.execute(query, (f"%{nombre}%",))
                results = cursor.fetchall()
                return [cls(**result) for result in results]
            except Error as e:
                print(f"Error al buscar artistas por nombre: {e}")
            finally:
                close_db_connection(connection)
        return []

    @classmethod
    def contar(cls):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "SELECT COUNT(*) FROM artista"
                cursor.execute(query)
                result = cursor.fetchone()
                return result[0] if result else 0
            except Error as e:
                print(f"Error al contar artistas: {e}")
            finally:
                close_db_connection(connection)
        return 0

    @classmethod
    def listar_paginados(cls, pagina, por_pagina):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                offset = (pagina - 1) * por_pagina
                query = "SELECT * FROM artista LIMIT %s OFFSET %s"
                cursor.execute(query, (por_pagina, offset))
                results = cursor.fetchall()
                return [cls(**result) for result in results]
            except Error as e:
                print(f"Error al listar artistas paginados: {e}")
            finally:
                close_db_connection(connection)
        return []
