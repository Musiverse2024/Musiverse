from services.playlist_service import PlaylistService

def mostrar_menu():
    print("\n--- Menú de Gestión de Playlists ---")
    print("1. Crear playlist")
    print("2. Buscar playlist")
    print("3. Actualizar playlist")
    print("4. Eliminar playlist")
    print("5. Listar todas las playlists")
    print("6. Gestionar canciones en playlist")
    print("0. Volver al menú principal")

def playlist_menu():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        try:
            if opcion == "1":
                nombre = input("Ingrese el nombre de la playlist: ")
                id_usuario = int(input("Ingrese el ID del usuario: "))
                playlist = PlaylistService.crear_playlist(nombre, id_usuario)
                if playlist:
                    print(f"Playlist creada exitosamente: {playlist}")
                else:
                    print("Error al crear la playlist")
                    
            elif opcion == "2":
                id_playlist = int(input("Ingrese el ID de la playlist: "))
                playlist = PlaylistService.obtener_playlist(id_playlist)
                if playlist:
                    print(f"Playlist encontrada: {playlist}")
                else:
                    print("Playlist no encontrada")
                    
            elif opcion == "3":
                id_playlist = int(input("Ingrese el ID de la playlist: "))
                playlist = PlaylistService.obtener_playlist(id_playlist)
                if playlist:
                    nuevo_nombre = input("Nuevo nombre (Enter para mantener actual): ")
                    if nuevo_nombre:
                        playlist.nombre = nuevo_nombre
                    if PlaylistService.actualizar_playlist(playlist):
                        print("Playlist actualizada exitosamente")
                    else:
                        print("Error al actualizar la playlist")
                else:
                    print("Playlist no encontrada")
                    
            elif opcion == "4":
                id_playlist = int(input("Ingrese el ID de la playlist: "))
                if PlaylistService.eliminar_playlist(id_playlist):
                    print("Playlist eliminada exitosamente")
                else:
                    print("Error al eliminar la playlist")
                    
            elif opcion == "5":
                playlists = PlaylistService.listar_playlists()
                if playlists:
                    print("\nPlaylists disponibles:")
                    for playlist in playlists:
                        print(f"ID: {playlist.id}, Nombre: {playlist.nombre}, Usuario: {playlist.id_usuario}")
                else:
                    print("No hay playlists disponibles")
                    
            elif opcion == "6":
                gestionar_canciones_playlist()
                
            elif opcion == "0":
                break
                
            else:
                print("Opción no válida")
                
        except ValueError as e:
            print(f"Error: Entrada inválida - {str(e)}")
        except Exception as e:
            print(f"Error inesperado: {str(e)}")

def gestionar_canciones_playlist():
    while True:
        print("\n--- Gestión de Canciones en Playlist ---")
        print("1. Agregar canción")
        print("2. Eliminar canción")
        print("3. Ver canciones")
        print("4. Ver total de canciones")
        print("0. Volver al menú anterior")
        
        opcion = input("Seleccione una opción: ")
        
        try:
            if opcion == "1":
                id_playlist = int(input("Ingrese el ID de la playlist: "))
                id_cancion = int(input("Ingrese el ID de la canción: "))
                resultado = PlaylistService.agregar_cancion(id_playlist, id_cancion)
                if resultado:
                    print("Canción agregada exitosamente")
                else:
                    print("No se pudo agregar la canción")
                    
            elif opcion == "2":
                id_playlist = int(input("Ingrese el ID de la playlist: "))
                id_cancion = int(input("Ingrese el ID de la canción: "))
                if PlaylistService.eliminar_cancion(id_playlist, id_cancion):
                    print("Canción eliminada exitosamente")
                else:
                    print("No se pudo eliminar la canción")
                    
            elif opcion == "3":
                id_playlist = int(input("Ingrese el ID de la playlist: "))
                canciones = PlaylistService.obtener_canciones_playlist(id_playlist)
                if canciones:
                    print("\nCanciones en la playlist:")
                    for cancion in canciones:
                        print(f"ID: {cancion['id']}, Nombre: {cancion['nombre']}")
                else:
                    print("La playlist no tiene canciones")
                    
            elif opcion == "4":
                id_playlist = int(input("Ingrese el ID de la playlist: "))
                total = PlaylistService.obtener_total_canciones(id_playlist)
                print(f"Total de canciones en la playlist: {total}")
                
            elif opcion == "0":
                break
                
            else:
                print("Opción no válida")
                
        except ValueError:
            print("Error: Los IDs deben ser números")
