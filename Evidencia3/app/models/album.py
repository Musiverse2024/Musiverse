# app/models/album.py

from utils.db_utils import get_db_connection, close_db_connection
from mysql.connector import Error

class Album:
    def __init__(self, id_album, titulo, id_artista, ano_lanzamiento):
        self.id_album = id_album
        self.titulo = titulo
        self.id_artista = id_artista
        self.ano_lanzamiento = ano_lanzamiento

    def __str__(self):
        return f"Álbum: {self.titulo}, Año: {self.ano_lanzamiento}"

    @classmethod
    def crear(cls, titulo, id_artista, ano_lanzamiento):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "INSERT INTO album (titulo, id_artista, ano_lanzamiento) VALUES (%s, %s, %s)"
                cursor.execute(query, (titulo, id_artista, ano_lanzamiento))
                connection.commit()
                id_album = cursor.lastrowid
                return cls(id_album, titulo, id_artista, ano_lanzamiento)
            except Error as e:
                print(f"Error al crear álbum: {e}")
                return None
            finally:
                close_db_connection(connection)
        return None

    @classmethod
    def obtener(cls, id_album):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM album WHERE id_album = %s"
                cursor.execute(query, (id_album,))
                result = cursor.fetchone()
                if result:
                    return cls(**result)
            except Error as e:
                print(f"Error al obtener álbum: {e}")
            finally:
                close_db_connection(connection)
        return None

    def actualizar(self):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "UPDATE album SET titulo = %s, ano_lanzamiento = %s WHERE id_album = %s"
                cursor.execute(query, (self.titulo, self.ano_lanzamiento, self.id_album))
                connection.commit()
                return True
            except Error as e:
                print(f"Error al actualizar álbum: {e}")
                return False
            finally:
                close_db_connection(connection)
        return False

    def eliminar(self):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "DELETE FROM album WHERE id_album = %s"
                cursor.execute(query, (self.id_album,))
                connection.commit()
                return True
            except Error as e:
                print(f"Error al eliminar álbum: {e}")
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
                query = "SELECT * FROM album"
                cursor.execute(query)
                results = cursor.fetchall()
                return [cls(**result) for result in results]
            except Error as e:
                print(f"Error al listar álbumes: {e}")
            finally:
                close_db_connection(connection)
        return []

    @classmethod
    def buscar_por_artista(cls, id_artista):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM album WHERE id_artista = %s"
                cursor.execute(query, (id_artista,))
                results = cursor.fetchall()
                return [cls(**result) for result in results]
            except Error as e:
                print(f"Error al buscar álbumes por artista: {e}")
            finally:
                close_db_connection(connection)
        return []

    @classmethod
    def buscar_por_titulo(cls, titulo):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM album WHERE titulo LIKE %s"
                cursor.execute(query, (f"%{titulo}%",))
                results = cursor.fetchall()
                return [cls(**result) for result in results]
            except Error as e:
                print(f"Error al buscar álbumes por título: {e}")
            finally:
                close_db_connection(connection)
        return []

    @classmethod
    def contar(cls):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "SELECT COUNT(*) FROM album"
                cursor.execute(query)
                result = cursor.fetchone()
                return result[0] if result else 0
            except Error as e:
                print(f"Error al contar álbumes: {e}")
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
                query = "SELECT * FROM album LIMIT %s OFFSET %s"
                cursor.execute(query, (por_pagina, offset))
                results = cursor.fetchall()
                return [cls(**result) for result in results]
            except Error as e:
                print(f"Error al listar álbumes paginados: {e}")
            finally:
                close_db_connection(connection)
        return []
