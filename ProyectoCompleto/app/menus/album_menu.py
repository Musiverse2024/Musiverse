# app/menus/album_menu.py

from services.album_service import AlbumService
from services.song_service import SongService
from services.artist_service import ArtistService
from utils.base_service import ValidationError

def mostrar_album(album):
    """Muestra los detalles de un álbum"""
    print(f"\nID: {album.id}")
    print(f"Título: {album.nombre}")
    print(f"Artista: {album.nombre_artista}")
    print(f"Fecha de lanzamiento: {album.fecha_lanzamiento}")

def mostrar_albumes(albumes):
    """Muestra una lista de álbumes"""
    if not albumes:
        print("\nNo se encontraron álbumes.")
        return
    
    print("\n=== Lista de Álbumes ===")
    for album in albumes:
        mostrar_album(album)

def mostrar_menu_albumes():
    print("\n=== Menú de Gestión de Álbumes ===")
    print("1. Crear álbum")
    print("2. Buscar álbum")
    print("3. Listar álbumes")
    print("4. Actualizar álbum")
    print("5. Eliminar álbum")
    print("6. Buscar álbumes por artista")
    print("7. Listar canciones de un álbum")
    print("0. Volver al menú principal")
    return input("Seleccione una opción: ")

def ejecutar_menu_albumes():
    while True:
        try:
            opcion = mostrar_menu_albumes()
            if opcion == '1':
                nombre = input("Ingrese el nombre del álbum: ")
                id_artista = int(input("Ingrese el ID del artista: "))
                fecha_lanzamiento = input("Ingrese la fecha de lanzamiento (YYYY-MM-DD): ")
                
                try:
                    nuevo_album = AlbumService.crear_album(nombre, id_artista, fecha_lanzamiento)
                    if nuevo_album:
                        print("\n✅ Álbum creado exitosamente:")
                        mostrar_album(nuevo_album)
                    else:
                        print("\n❌ Error al crear el álbum")
                except ValidationError as e:
                    print(f"\n⚠️ Error de validación: {str(e)}")
            elif opcion == '2':
                id_album = int(input("Ingrese el ID del álbum: "))
                album = AlbumService.obtener_album(id_album)
                if album:
                    print(f"Álbum encontrado: {album}")
                else:
                    print("Álbum no encontrado.")
            elif opcion == '3':
                albumes = AlbumService.listar_albumes()
                mostrar_albumes(albumes)
            elif opcion == '4':
                id_album = int(input("Ingrese el ID del álbum a actualizar: "))
                album = AlbumService.obtener_album(id_album)
                if album:
                    nombre = input("Ingrese el nuevo nombre del álbum: ")
                    fecha_lanzamiento = input("Ingrese la nueva fecha de lanzamiento (YYYY-MM-DD): ")
                    try:
                        if AlbumService.actualizar_album(id_album, nombre, fecha_lanzamiento):
                            print("\n✅ Álbum actualizado exitosamente")
                        else:
                            print("\n❌ Error al actualizar el álbum")
                    except ValidationError as e:
                        print(f"\n⚠️ Error de validación: {str(e)}")
                else:
                    print("\nÁlbum no encontrado")
            elif opcion == '5':
                id_album = int(input("Ingrese el ID del álbum a eliminar: "))
                if AlbumService.eliminar_album(id_album):
                    print("Álbum eliminado exitosamente.")
                else:
                    print("Error al eliminar el álbum.")
            elif opcion == '6':
                id_artista = int(input("Ingrese el ID del artista: "))
                albumes = AlbumService.buscar_albumes_por_artista(id_artista)
                if albumes:
                    artista = ArtistService.obtener_artista(id_artista)
                    print(f"\nÁlbumes del artista {artista.nombre}:")
                    for album in albumes:
                        print(f"ID: {album.id}, Título: {album.nombre}")
                else:
                    print("No se encontraron álbumes para este artista.")
            elif opcion == '7':
                id_album = int(input("Ingrese el ID del álbum: "))
                canciones = SongService.listar_canciones_por_album(id_album)
                if canciones:
                    album = AlbumService.obtener_album(id_album)
                    print(f"\nCanciones del álbum {album.nombre}:")
                    for cancion in canciones:
                        print(f"ID: {cancion.id}, Título: {cancion.nombre}")
                else:
                    print("No se encontraron canciones para este álbum.")
            elif opcion == '0':
                break
            else:
                print("Opción no válida.")
                
            input("\nPresione Enter para continuar...")
        except ValueError as e:
            print(f"\n⚠️ Error: Valor inválido - {str(e)}")
        except ValidationError as e:
            print(f"\n⚠️ Error de validación: {str(e)}")
        except Exception as e:
            print(f"\n❌ Error inesperado: {str(e)}")

def album_menu():
    print("\n=== Gestión de Álbumes ===")
    ejecutar_menu_albumes()

if __name__ == "__main__":
    album_menu()

