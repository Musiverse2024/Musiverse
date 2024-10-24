# app/services/song_service.py

from models.song import Cancion
from models.artist import Artista
from models.album import Album
from datetime import datetime
from utils.db_utils import get_db_connection, close_db_connection

def crear_cancion(titulo, duracion, genero, id_album, id_artista):
    connection = get_db_connection()
    if connection:
        try:
            # Verificar si el artista existe
            artista = Artista.obtener(id_artista)
            if not artista:
                print("El artista especificado no existe.")
                return None

            # Verificar si el álbum existe
            album = Album.obtener(id_album)
            if not album:
                print("El álbum especificado no existe.")
                return None

            nueva_cancion = Cancion.crear(titulo, duracion, genero, id_album, id_artista)
            return nueva_cancion
        finally:
            close_db_connection(connection)
    return None

def obtener_cancion(id_cancion):
    connection = get_db_connection()
    if connection:
        try:
            return Cancion.obtener(id_cancion)
        finally:
            close_db_connection(connection)
    return None

def actualizar_cancion(cancion):
    connection = get_db_connection()
    if connection:
        try:
            return cancion.actualizar()
        finally:
            close_db_connection(connection)
    return False

def eliminar_cancion(cancion):
    connection = get_db_connection()
    if connection:
        try:
            return cancion.eliminar()
        finally:
            close_db_connection(connection)
    return False

def listar_canciones():
    connection = get_db_connection()
    if connection:
        try:
            return Cancion.listar_todos()
        finally:
            close_db_connection(connection)
    return []

def buscar_canciones_por_titulo(titulo):
    connection = get_db_connection()
    if connection:
        try:
            return Cancion.buscar_por_titulo(titulo)
        finally:
            close_db_connection(connection)
    return []

def buscar_canciones_por_artista(id_artista):
    connection = get_db_connection()
    if connection:
        try:
            return Cancion.buscar_por_artista(id_artista)
        finally:
            close_db_connection(connection)
    return []

def listar_canciones_por_artista(id_artista):
    connection = get_db_connection()
    if connection:
        try:
            return Cancion.buscar_por_artista(id_artista)
        finally:
            close_db_connection(connection)
    return []

def listar_canciones_por_album(id_album):
    connection = get_db_connection()
    if connection:
        try:
            return Cancion.buscar_por_album(id_album)
        finally:
            close_db_connection(connection)
    return []



def crear_cancion_interactiva():
    titulo = input("Ingrese el título de la canción: ")
    duracion = input("Ingrese la duración de la canción (HH:MM:SS): ")
    genero = input("Ingrese el género de la canción: ")
    
    # Mostrar artistas disponibles
    from services.artist_service import listar_artistas
    artistas = listar_artistas()
    if not artistas:
        print("No hay artistas disponibles. Por favor, cree un artista primero.")
        return
    
    print("\nArtistas disponibles:")
    for artista in artistas:
        print(f"ID: {artista.id_artista}, Nombre: {artista.nombre_artista}")
    
    while True:
        try:
            id_artista = int(input("Ingrese el ID del artista: "))
            if any(artista.id_artista == id_artista for artista in artistas):
                break
            else:
                print("ID de artista no válido. Por favor, elija un ID de la lista.")
        except ValueError:
            print("Por favor, ingrese un número válido para el ID del artista.")
    
    # Mostrar álbumes disponibles para el artista seleccionado
    from services.album_service import listar_albumes_por_artista
    albumes = listar_albumes_por_artista(id_artista)
    print("\nÁlbumes disponibles para este artista:")
    for album in albumes:
        print(f"ID: {album.id_album}, Título: {album.titulo}")
    
    while True:
        try:
            id_album = int(input("Ingrese el ID del álbum: "))
            if any(album.id_album == id_album for album in albumes):
                break
            else:
                print("ID de álbum no válido. Por favor, elija un ID de la lista.")
        except ValueError:
            print("Por favor, ingrese un número válido para el ID del álbum.")

    nueva_cancion = crear_cancion(titulo, duracion, genero, id_album, id_artista)
    if nueva_cancion:
        print(f"Canción creada exitosamente: {nueva_cancion}")
    else:
        print("Error al crear la canción.")

def actualizar_cancion_interactiva():
    id_cancion = int(input("Ingrese el ID de la canción a actualizar: "))
    cancion = obtener_cancion(id_cancion)
    if cancion:
        print(f"Canción actual: {cancion}")
        cancion.titulo = input("Nuevo título (deje en blanco para no cambiar): ") or cancion.titulo
        cancion.duracion = input("Nueva duración (HH:MM:SS) (deje en blanco para no cambiar): ") or cancion.duracion
        cancion.genero = input("Nuevo género (deje en blanco para no cambiar): ") or cancion.genero
        cancion.id_album = int(input("Nuevo ID de álbum (deje en blanco para no cambiar): ") or cancion.id_album)
        cancion.id_artista = int(input("Nuevo ID de artista (deje en blanco para no cambiar): ") or cancion.id_artista)

        if actualizar_cancion(cancion):
            print(f"Canción actualizada exitosamente: {cancion}")
        else:
            print("Error al actualizar la canción.")
    else:
        print("Canción no encontrada.")

def eliminar_cancion_interactiva():
    id_cancion = int(input("Ingrese el ID de la canción a eliminar: "))
    cancion = obtener_cancion(id_cancion)
    if cancion:
        confirmacion = input(f"¿Está seguro de que desea eliminar la canción '{cancion.titulo}'? (s/n): ")
        if confirmacion.lower() == 's':
            if eliminar_cancion(cancion):
                print("Canción eliminada exitosamente.")
            else:
                print("Error al eliminar la canción.")
        else:
            print("Operación de eliminación cancelada.")
    else:
        print("Canción no encontrada.")

def listar_canciones_formateadas():
    canciones = listar_canciones()
    if canciones:
        print("\nLista de canciones:")
        for cancion in canciones:
            print(f"ID: {cancion.id_cancion}, Título: {cancion.titulo}, Duración: {cancion.duracion}, Género: {cancion.genero}")
    else:
        print("No se encontraron canciones.")

def buscar_canciones_interactiva():
    opcion = input("Buscar por (1) título o (2) ID de artista: ")
    if opcion == '1':
        titulo = input("Ingrese el título a buscar: ")
        canciones = buscar_canciones_por_titulo(titulo)
    elif opcion == '2':
        id_artista = int(input("Ingrese el ID del artista: "))
        canciones = buscar_canciones_por_artista(id_artista)
    else:
        print("Opción no válida.")
        return

    if canciones:
        print("\nCanciones encontradas:")
        for cancion in canciones:
            print(f"ID: {cancion.id_cancion}, Título: {cancion.titulo}, Duración: {cancion.duracion}, Género: {cancion.genero}")
    else:
        print("No se encontraron canciones.")

def ordenar_canciones():
    canciones = listar_canciones()
    print("\nElija el método de ordenamiento:")
    print("1. Por título")
    print("2. Por duración")
    print("3. Por género")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        canciones.sort(key=lambda x: x.titulo)
    elif opcion == '2':
        canciones.sort(key=lambda x: datetime.strptime(x.duracion, '%H:%M:%S'))
    elif opcion == '3':
        canciones.sort(key=lambda x: x.genero)
    else:
        print("Opción no válida.")
        return

    print("\nCanciones ordenadas:")
    for cancion in canciones:
        print(f"Título: {cancion.titulo}, Duración: {cancion.duracion}, Género: {cancion.genero}")


