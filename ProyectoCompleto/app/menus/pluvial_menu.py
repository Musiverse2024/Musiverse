# app/menus/pluvial_menu.py
from services.pluvial_service import cargar_datos_pluviales, consultar_datos_pluviales, visualizar_datos_pluviales

def pluvial_menu():
    while True:
        print("\nGestión de Datos Pluviales")
        print("1. Cargar datos")
        print("2. Consultar datos")
        print("3. Visualizar datos")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            cargar_datos_pluviales()
        elif opcion == '2':
            consultar_datos_pluviales()
        elif opcion == '3':
            visualizar_datos_pluviales()
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente nuevamente.")
