# app/menus/song_menu.py

from services.song_service import (
    crear_cancion_interactiva,
    actualizar_cancion_interactiva,
    eliminar_cancion_interactiva,
    listar_canciones_formateadas,
    buscar_canciones_interactiva,
    ordenar_canciones
)

def mostrar_menu_canciones():
    print("\n--- Menú de Gestión de Canciones ---")
    print("1. Crear canción")
    print("2. Buscar canciones")
    print("3. Actualizar canción")
    print("4. Eliminar canción")
    print("5. Listar todas las canciones")
    print("6. Ordenar canciones")
    print("0. Volver al menú principal")
    return input("Seleccione una opción: ")

def ejecutar_menu_canciones():
    while True:
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
            listar_canciones_formateadas()
        elif opcion == '6':
            ordenar_canciones()
        elif opcion == '0':
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def song_menu():
    print("\n--- Gestión de Canciones ---")
    ejecutar_menu_canciones()

if __name__ == "__main__":
    song_menu()

