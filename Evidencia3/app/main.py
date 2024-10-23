# app/main.py
from menus.user_menu import user_menu
from menus.pluvial_menu import pluvial_menu
from menus.song_menu import song_menu
from menus.artist_menu import artist_menu
from menus.album_menu import album_menu

def main_menu():
    while True:
        print("\nBienvenido al sistema de gestión!")
        print("1. Gestión de Usuarios")
        print("2. Gestión de Datos Pluviales")
        print("3. Gestión de Música")
        print("4. Gestión de Artistas")
        print("5. Gestión de Álbumes")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            user_menu()
        elif opcion == '2':
            pluvial_menu()
        elif opcion == '3':
            song_menu()
        elif opcion == '4':
            artist_menu()
        elif opcion == '5':
            album_menu()
        elif opcion == '6':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main_menu()
