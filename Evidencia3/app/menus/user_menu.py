# app/menus/user_menu.py
from services.user_service import (
    crear_usuario_interactivo,
    buscar_usuario,
    actualizar_usuario_interactivo,
    eliminar_usuario_interactivo,
    listar_usuarios,
    ordenar_usuarios
)

def mostrar_menu():
    print("\n--- Menú de Gestión de Usuarios ---")
    print("1. Crear usuario")
    print("2. Buscar usuario")
    print("3. Actualizar usuario")
    print("4. Eliminar usuario")
    print("5. Listar todos los usuarios")
    print("6. Ordenar usuarios")
    print("0. Volver al menú principal")
    return input("Seleccione una opción: ")

def ejecutar_menu():
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            crear_usuario_interactivo()
        elif opcion == '2':
            buscar_usuario()
        elif opcion == '3':
            actualizar_usuario_interactivo()
        elif opcion == '4':
            eliminar_usuario_interactivo()
        elif opcion == '5':
            usuarios = listar_usuarios()
            for usuario in usuarios:
                print(usuario)
        elif opcion == '6':
            ordenar_usuarios()
        elif opcion == '0':
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def user_menu():
    print("\n--- Gestión de Usuarios ---")
    ejecutar_menu()

if __name__ == "__main__":
    user_menu()
