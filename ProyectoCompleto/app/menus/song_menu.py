# app/menus/song_menu.py
from services.song_service import SongService
from validaciones.song_validaciones import SongValidaciones

def mostrar_menu_canciones():
    """Muestra el menú de opciones para gestión de canciones"""
    print("\n=== Menú de Gestión de Canciones ===")
    print("1. Crear canción")
    print("2. Buscar canciones")
    print("3. Actualizar canción")
    print("4. Eliminar canción")
    print("5. Listar todas las canciones")
    print("6. Ordenar canciones")
    print("0. Volver al menú principal")
    return input("Seleccione una opción: ")

def mostrar_cancion(cancion):
    """Muestra los detalles de una canción"""
    print(f"\nID: {cancion.id}")
    print(f"Nombre: {cancion.nombre}")
    print(f"Álbum: {cancion.nombre_album or 'N/A'}")
    print(f"Género: {cancion.nombre_genero or 'N/A'}")
    print(f"Artista: {cancion.nombre_artista or 'N/A'}")
    if cancion.fecha_lanzamiento:
        print(f"Fecha de lanzamiento: {cancion.fecha_lanzamiento}")

def mostrar_canciones(canciones):
    """Muestra una lista de canciones"""
    if not canciones:
        print("\nNo se encontraron canciones.")
        return
    
    print("\n=== Lista de Canciones ===")
    for cancion in canciones:
        mostrar_cancion(cancion)

def crear_cancion_interactiva():
    """Interfaz interactiva para crear una canción"""
    try:
        print("\n=== Crear Nueva Canción ===")
        datos = {
            'nombre': input("Ingrese el nombre de la canción: ").strip(),
            'id_album': int(input("Ingrese el ID del álbum: ")),
            'id_genero': int(input("Ingrese el ID del género: "))
        }
        
        validador = SongValidaciones()
        if validador.validate(datos):
            cancion = SongService.crear_cancion(**datos)
            if cancion:
                print("\n✅ Canción creada exitosamente:")
                mostrar_cancion(cancion)
            else:
                print("\n❌ Error al crear la canción")
    except ValueError as e:
        print(f"\n⚠️ Error de validación: {str(e)}")
    except Exception as e:
        print(f"\n❌ Error inesperado: {str(e)}")

def buscar_canciones_interactiva():
    """Interfaz interactiva para buscar canciones"""
    try:
        print("\n=== Buscar Canciones ===")
        nombre = input("Ingrese el nombre de la canción a buscar: ").strip()
        canciones = SongService.buscar_por_nombre(nombre)
        mostrar_canciones(canciones)
    except Exception as e:
        print(f"\n❌ Error al buscar canciones: {str(e)}")

def actualizar_cancion_interactiva():
    """Interfaz interactiva para actualizar una canción"""
    try:
        print("\n=== Actualizar Canción ===")
        id_cancion = int(input("Ingrese el ID de la canción a actualizar: "))
        cancion = SongService.obtener_cancion(id_cancion)
        
        if not cancion:
            print("\n❌ Canción no encontrada")
            return

        print("\nCanción actual:")
        mostrar_cancion(cancion)
        
        datos = {}
        nombre = input("\nNuevo nombre (Enter para mantener actual): ").strip()
        if nombre:
            datos['nombre'] = nombre

        id_album = input("Nuevo ID de álbum (Enter para mantener actual): ").strip()
        if id_album:
            datos['id_album'] = int(id_album)

        id_genero = input("Nuevo ID de género (Enter para mantener actual): ").strip()
        if id_genero:
            datos['id_genero'] = int(id_genero)

        if datos:
            validador = SongValidaciones()
            if validador.validate(datos):
                cancion_actualizada = SongService.actualizar_cancion(id_cancion, **datos)
                if cancion_actualizada:
                    print("\n✅ Canción actualizada exitosamente")
                    mostrar_cancion(cancion_actualizada)
                else:
                    print("\n❌ Error al actualizar la canción")
        else:
            print("\nNo se realizaron cambios")
    except ValueError as e:
        print(f"\n⚠️ Error de validación: {str(e)}")
    except Exception as e:
        print(f"\n❌ Error inesperado: {str(e)}")

def eliminar_cancion_interactiva():
    """Interfaz interactiva para eliminar una canción"""
    try:
        print("\n=== Eliminar Canción ===")
        id_cancion = int(input("Ingrese el ID de la canción a eliminar: "))
        cancion = SongService.obtener_cancion(id_cancion)
        
        if not cancion:
            print("\n❌ Canción no encontrada")
            return

        print("\nCanción a eliminar:")
        mostrar_cancion(cancion)
        
        confirmacion = input("\n¿Está seguro de eliminar esta canción? (s/n): ").lower()
        if confirmacion == 's':
            if SongService.eliminar_cancion(id_cancion):
                print("\n✅ Canción eliminada exitosamente")
            else:
                print("\n❌ Error al eliminar la canción")
        else:
            print("\nOperación cancelada")
    except ValueError as e:
        print(f"\n⚠️ Error de validación: {str(e)}")
    except Exception as e:
        print(f"\n❌ Error inesperado: {str(e)}")

def ejecutar_menu_canciones():
    """Ejecuta el menú principal de gestión de canciones"""
    while True:
        try:
            opcion = mostrar_menu_canciones()
            
            if opcion == '1':
                crear_cancion_interactiva()
            elif opcion == '2':
                buscar_canciones_interactiva()
            elif opcion == '3':
                actualizar_cancion_interactiva()
            elif opcion == '4':
                eliminar_cancion_interactiva()
            elif opcion == '5':
                canciones = SongService.listar_canciones()
                mostrar_canciones(canciones)
            elif opcion == '6':
                print("\n⚠️ Función de ordenamiento no implementada")
            elif opcion == '0':
                print("\nVolviendo al menú principal...")
                break
            else:
                print("\n⚠️ Opción no válida")
                
            input("\nPresione Enter para continuar...")
        except Exception as e:
            print(f"\n❌ Error inesperado: {str(e)}")
            input("\nPresione Enter para continuar...")

def song_menu():
    """Punto de entrada para el menú de canciones"""
    print("\n=== Gestión de Canciones ===")
    ejecutar_menu_canciones()

if __name__ == "__main__":
    song_menu()

