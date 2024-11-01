# app/main.py
from menus.accesos_ispc_menu import accesos_ispc_menu
from menus.user_menu import user_menu
from menus.pluvial_menu import pluvial_menu
from menus.song_menu import song_menu
from menus.artist_menu import artist_menu
from menus.album_menu import album_menu
from menus.playlist_menu import playlist_menu
from menus.usuario_genero_menu import usuario_genero_menu
from menus.historial_reproduccion_menu import historial_reproduccion_menu
from menus.favoritos_menu import favoritos_menu

def mostrar_menu_musiverse():
    while True:
        print("\n=== Musiverse ===")
        print("1. Gestión de Usuarios")
        print("2. Gestión de Música")
        print("3. Gestión de Artistas")
        print("4. Gestión de Álbumes")
        print("5. Gestión de Playlists")
        print("6. Gestión de Géneros por Usuario")
        print("7. Historial de Reproducción")
        print("8. Gestión de Favoritos")
        print("0. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            user_menu()
        elif opcion == "2":
            song_menu()
        elif opcion == "3":
            artist_menu()
        elif opcion == "4":
            album_menu()
        elif opcion == "5":
            playlist_menu()
        elif opcion == "6":
            usuario_genero_menu()
        elif opcion == "7":
            historial_reproduccion_menu()
        elif opcion == "8":
            favoritos_menu()
        elif opcion == "0":
            break
        else:
            print("Opción no válida")

def main_menu():
    while True:
        try:
            print("\n=== Sistema de Gestión ===")
            print("1. Accesos ISPC")
            print("2. Musiverse")
            print("3. Análisis de datos")
            print("0. Salir")
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                accesos_ispc_menu()
            elif opcion == "2":
                mostrar_menu_musiverse()
            elif opcion == "3":
                pluvial_menu()
            elif opcion == "0":
                print("Saliendo del sistema...")
                break
            else:
                print("\n⚠️ Opción no válida")
                
            input("\nPresione Enter para continuar...")
        except Exception as e:
            print(f"\n❌ Error inesperado: {str(e)}")
            input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    print("=== Bienvenido al Sistema de Gestión ===")
    print("Versión 1.0")
    main_menu()
