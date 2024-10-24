# app/menus/artist_menu.py

from services.artist_service import crear_artista, obtener_artista, listar_artistas, actualizar_artista, eliminar_artista
from services.song_service import listar_canciones_por_artista

def mostrar_menu_artistas():
    print("\n--- Menú de Gestión de Artistas ---")
    print("1. Crear artista")
    print("2. Buscar artista")
    print("3. Listar todos los artistas")
    print("4. Actualizar artista")
    print("5. Eliminar artista")
    print("6. Listar canciones de un artista")
    print("0. Volver al menú principal")
    return input("Seleccione una opción: ")

def ejecutar_menu_artistas():
    while True:
        opcion = mostrar_menu_artistas()
        if opcion == '1':
            nombre_artista = input("Ingrese el nombre del artista: ")
            nuevo_artista = crear_artista(nombre_artista)
            if nuevo_artista:
                print(f"Artista creado exitosamente: {nuevo_artista}")
            else:
                print("Error al crear el artista.")
        elif opcion == '2':
            id_artista = int(input("Ingrese el ID del artista: "))
            artista = obtener_artista(id_artista)
            if artista:
                print(f"Artista encontrado: {artista}")
            else:
                print("Artista no encontrado.")
        elif opcion == '3':
            artistas = listar_artistas()
            if artistas:
                print("\nLista de artistas:")
                for artista in artistas:
                    print(f"ID: {artista.id_artista}, Nombre: {artista.nombre_artista}")
            else:
                print("No se encontraron artistas.")
        elif opcion == '4':
            id_artista = int(input("Ingrese el ID del artista a actualizar: "))
            artista = obtener_artista(id_artista)
            if artista:
                nuevo_nombre = input("Ingrese el nuevo nombre del artista: ")
                if actualizar_artista(id_artista, nuevo_nombre):
                    print("Artista actualizado exitosamente.")
                else:
                    print("Error al actualizar el artista.")
            else:
                print("Artista no encontrado.")
        elif opcion == '5':
            id_artista = int(input("Ingrese el ID del artista a eliminar: "))
            if eliminar_artista(id_artista):
                print("Artista eliminado exitosamente.")
            else:
                print("Error al eliminar el artista.")
        elif opcion == '6':
            id_artista = int(input("Ingrese el ID del artista: "))
            canciones = listar_canciones_por_artista(id_artista)
            if canciones:
                print(f"\nCanciones del artista (ID: {id_artista}):")
                for cancion in canciones:
                    print(f"ID: {cancion.id_cancion}, Título: {cancion.titulo}")
            else:
                print("No se encontraron canciones para este artista.")
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def artist_menu():
    print("\n--- Gestión de Artistas ---")
    ejecutar_menu_artistas()
