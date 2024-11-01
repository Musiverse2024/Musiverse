from services.usuario_genero_service import UsuarioGeneroService

def mostrar_menu_usuario_genero():
    """Muestra el menú de opciones para gestión de géneros por usuario"""
    print("\n=== Gestión de Géneros por Usuario ===")
    print("1. Agregar género a usuario")
    print("2. Eliminar género de usuario")
    print("3. Ver géneros de un usuario")
    print("0. Volver al menú principal")
    return input("Seleccione una opción: ")

def mostrar_generos_usuario(generos):
    """Muestra los géneros asignados a un usuario"""
    if not generos:
        print("\nEl usuario no tiene géneros asignados.")
        return
    
    print("\n=== Géneros del Usuario ===")
    for genero in generos:
        print(f"ID: {genero['id']}")
        print(f"Nombre: {genero['nombre']}")
        print("-" * 20)

def ejecutar_menu_usuario_genero():
    """Ejecuta el menú de gestión de géneros por usuario"""
    while True:
        try:
            opcion = mostrar_menu_usuario_genero()
            
            if opcion == '1':
                id_usuario = int(input("Ingrese el ID del usuario: "))
                id_genero = int(input("Ingrese el ID del género: "))
                resultado = UsuarioGeneroService.agregar_genero(id_usuario, id_genero)
                if resultado:
                    print("\n✅ Género agregado exitosamente")
                else:
                    print("\n❌ Error al agregar el género")
            elif opcion == '2':
                id_usuario = int(input("Ingrese el ID del usuario: "))
                id_genero = int(input("Ingrese el ID del género: "))
                if UsuarioGeneroService.eliminar_genero(id_usuario, id_genero):
                    print("\n✅ Género eliminado exitosamente")
                else:
                    print("\n❌ Error al eliminar el género")
            elif opcion == '3':
                id_usuario = int(input("Ingrese el ID del usuario: "))
                generos = UsuarioGeneroService.obtener_generos_usuario(id_usuario)
                mostrar_generos_usuario(generos)
            elif opcion == '0':
                break
            else:
                print("\n⚠️ Opción no válida")
                
            input("\nPresione Enter para continuar...")
        except ValueError as e:
            print(f"\n⚠️ Error de validación: {str(e)}")
        except Exception as e:
            print(f"\n❌ Error inesperado: {str(e)}")

def usuario_genero_menu():
    """Punto de entrada para el menú de géneros por usuario"""
    print("\n=== Gestión de Géneros por Usuario ===")
    ejecutar_menu_usuario_genero() 