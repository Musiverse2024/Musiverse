# app/menus/artist_menu.py

from services.artist_service import ArtistService
from services.song_service import SongService
from validaciones.artist_validaciones import ArtistValidaciones

def mostrar_artista(artista):
    """Muestra los detalles de un artista"""
    print(f"\nID: {artista.id}")
    print(f"Nombre: {artista.nombre}")
    # Mostrar cantidad de álbumes si está disponible
    if hasattr(artista, 'cantidad_albumes'):
        print(f"Cantidad de álbumes: {artista.cantidad_albumes}")

def mostrar_artistas(artistas):
    """Muestra una lista de artistas"""
    if not artistas:
        print("\nNo se encontraron artistas.")
        return
    
    print("\n=== Lista de Artistas ===")
    for artista in artistas:
        mostrar_artista(artista)

def mostrar_menu_artistas():
    print("\n--- Menú de Gestión de Artistas ---")
    print("1. Crear artista")
    print("2. Buscar artista por nombre")
    print("3. Listar todos los artistas")
    print("4. Actualizar artista")
    print("5. Eliminar artista")
    print("6. Listar canciones de un artista")
    print("0. Volver al menú principal")
    return input("Seleccione una opción: ")

def ejecutar_menu_artistas():
    while True:
        try:
            opcion = mostrar_menu_artistas()
            if opcion == '1':
                nombre = input("Ingrese el nombre del artista: ")
                validador = ArtistValidaciones()
                datos = {'nombre': nombre}
                if validador.validate(datos):
                    nuevo_artista = ArtistService.crear_artista(nombre)
                    if nuevo_artista:
                        print("\n✅ Artista creado exitosamente:")
                        mostrar_artista(nuevo_artista)
                    else:
                        print("\n❌ Error al crear el artista")
            elif opcion == '2':
                nombre_buscar = input("Ingrese el nombre del artista a buscar: ")
                artistas = ArtistService.buscar_por_nombre(nombre_buscar)
                if artistas:
                    print("\nArtistas encontrados:")
                    mostrar_artistas(artistas)
                else:
                    print("\nNo se encontraron artistas con ese nombre.")
            elif opcion == '3':
                artistas = ArtistService.listar_artistas()
                mostrar_artistas(artistas)
            elif opcion == '4':
                id_artista = int(input("Ingrese el ID del artista a actualizar: "))
                artista = ArtistService.obtener_artista(id_artista)
                if artista:
                    nuevo_nombre = input("Ingrese el nuevo nombre del artista: ")
                    validador = ArtistValidaciones()
                    datos = {'nombre': nuevo_nombre, 'id': id_artista}
                    if validador.validate(datos):
                        if ArtistService.actualizar_artista(id_artista, nuevo_nombre):
                            print("\n✅ Artista actualizado exitosamente")
                        else:
                            print("\n❌ Error al actualizar el artista")
                else:
                    print("Artista no encontrado.")
            elif opcion == '5':
                id_artista = int(input("Ingrese el ID del artista a eliminar: "))
                if ArtistService.eliminar_artista(id_artista):
                    print("Artista eliminado exitosamente.")
                else:
                    print("Error al eliminar el artista.")
            elif opcion == '6':
                id_artista = int(input("Ingrese el ID del artista: "))
                canciones = SongService.listar_canciones_por_artista(id_artista)
                if canciones:
                    print(f"\nCanciones del artista (ID: {id_artista}):")
                    for cancion in canciones:
                        print(f"ID: {cancion.id}, Título: {cancion.nombre}")
                else:
                    print("No se encontraron canciones para este artista.")
            elif opcion == '0':
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError as e:
            print(f"\n⚠️ Error de validación: {str(e)}")
        except Exception as e:
            print(f"\n❌ Error inesperado: {str(e)}")

def artist_menu():
    print("\n--- Gestión de Artistas ---")
    ejecutar_menu_artistas()
