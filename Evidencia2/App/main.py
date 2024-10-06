
import os
from datetime import datetime
from usuarios import (
    cargar_usuarios,
    agregar_usuario,
    modificar_usuario,
    eliminar_usuario,
    buscar_usuario,
    mostrar_usuarios,
    ingresar_al_sistema,
)

def menu_principal():
    while True:
        print('\n--- Menú Principal ---\n')
        print('1. Agregar un nuevo usuario')
        print('2. Modificar un usuario')
        print('3. Eliminar un usuario')
        print('4. Buscar un usuario')
        print('5. Mostrar todos los usuarios')
        print('6. Ingresar al sistema')
        print('7. Salir')
        
        opcion = input('\nSeleccione una opción: ')
        
        if opcion == '1':
            agregar_usuario()
        elif opcion == '2':
            modificar_usuario()
        elif opcion == '3':
            eliminar_usuario()
        elif opcion == '4':
            buscar_usuario()
        elif opcion == '5':
            mostrar_usuarios()
        elif opcion == '6':
            usuario_logueado = ingresar_al_sistema()
            if usuario_logueado:
                while True:
                    print('\n1. Salir al menú principal')
                    print('2. Salir de la aplicación')
                    opcion = input('\nSeleccione una opción: ')
                    if opcion == '1':
                        break
                    elif opcion == '2':
                        print('Saliendo de la aplicación...')
                        exit()
                    else:
                        print('Opción no válida.')
        elif opcion == '7':
            print('Saliendo del sistema...')
            break
        else:
            print('Opción no válida.')

if __name__ == "__main__":
    menu_principal()