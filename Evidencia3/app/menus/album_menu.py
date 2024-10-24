# app/menus/album_menu.py

from services.album_service import crear_album, obtener_album, listar_albumes, actualizar_album, eliminar_album, listar_albumes_por_artista
from services.song_service import listar_canciones_por_album
from services.artist_service import obtener_artista

def mostrar_menu_albumes():
    print("\n--- Menú de Gestión de Álbumes ---")
    print("1. Crear álbum")
    print("2. Buscar álbum")
    print("3. Listar todos los álbumes")
    print("4. Actualizar álbum")
    print("5. Eliminar álbum")
    print("6. Listar álbumes de un artista")
    print("7. Listar canciones de un álbum")
    print("0. Volver al menú principal")
    return input("Seleccione una opción: ")

def ejecutar_menu_albumes():
    while True:
        opcion = mostrar_menu_albumes()
        if opcion == '1':
            titulo = input("Ingrese el título del ��lbum: ")
            id_artista = int(input("Ingrese el ID del artista: "))
            ano_lanzamiento = int(input("Ingrese el año de lanzamiento: "))
            nuevo_album = crear_album(titulo, id_artista, ano_lanzamiento)
            if nuevo_album:
                print(f"Álbum creado exitosamente: {nuevo_album}")
            else:
                print("Error al crear el álbum.")
        elif opcion == '2':
            id_album = int(input("Ingrese el ID del álbum: "))
            album = obtener_album(id_album)
            if album:
                print(f"Álbum encontrado: {album}")
            else:
                print("Álbum no encontrado.")
        elif opcion == '3':
            albumes = listar_albumes()
            if albumes:
                print("\nLista de álbumes:")
                for album in albumes:
                    print(f"ID: {album.id_album}, Título: {album.titulo}, Año: {album.ano_lanzamiento}")
            else:
                print("No se encontraron álbumes.")
        elif opcion == '4':
            id_album = int(input("Ingrese el ID del álbum a actualizar: "))
            album = obtener_album(id_album)
            if album:
                nuevo_titulo = input("Ingrese el nuevo título del álbum: ")
                nuevo_ano = int(input("Ingrese el nuevo año de lanzamiento: "))
                if actualizar_album(id_album, nuevo_titulo, nuevo_ano):
                    print("Álbum actualizado exitosamente.")
                else:
                    print("Error al actualizar el álbum.")
            else:
                print("Álbum no encontrado.")
        elif opcion == '5':
            id_album = int(input("Ingrese el ID del álbum a eliminar: "))
            if eliminar_album(id_album):
                print("Álbum eliminado exitosamente.")
            else:
                print("Error al eliminar el álbum.")
        elif opcion == '6':
            id_artista = int(input("Ingrese el ID del artista: "))
            albumes = listar_albumes_por_artista(id_artista)
            if albumes:
                artista = obtener_artista(id_artista)
                print(f"\nÁlbumes del artista {artista.nombre_artista}:")
                for album in albumes:
                    print(f"ID: {album.id_album}, Título: {album.titulo}, Año: {album.ano_lanzamiento}")
            else:
                print("No se encontraron álbumes para este artista.")
        elif opcion == '7':
            id_album = int(input("Ingrese el ID del álbum: "))
            canciones = listar_canciones_por_album(id_album)
            if canciones:
                album = obtener_album(id_album)
                print(f"\nCanciones del álbum {album.titulo}:")
                for cancion in canciones:
                    print(f"ID: {cancion.id_cancion}, Título: {cancion.titulo}")
            else:
                print("No se encontraron canciones para este álbum.")
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def album_menu():
    print("\n--- Gestión de Álbumes ---")
    ejecutar_menu_albumes()

