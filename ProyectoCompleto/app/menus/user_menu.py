# app/menus/user_menu.py
from services.user_service import UserService
from validaciones.user_validaciones import UserValidator

def solicitar_input_validado(mensaje, validacion_func, *args):
    """
    Función auxiliar para solicitar y validar input
    """
    while True:
        try:
            valor = input(mensaje)
            if args:
                validacion_func(valor, *args)
            else:
                validacion_func(valor)
            return valor
        except ValueError as e:
            print(f"\n⚠️ Error de validación: {str(e)}")
            print("Por favor, intente nuevamente.")

def mostrar_menu():
    """
    Muestra el menú principal de gestión de usuarios
    """
    print("\n=== Menú de Gestión de Usuarios ===")
    print("1. Crear usuario")
    print("2. Buscar usuario")
    print("3. Actualizar usuario")
    print("4. Eliminar usuario")
    print("5. Listar todos los usuarios")
    print("6. Ordenar usuarios")
    print("0. Volver al menú principal")
    return input("Seleccione una opción: ")

def mostrar_submenu_busqueda():
    """
    Muestra el submenú de opciones de búsqueda
    """
    print("\n--- Opciones de Búsqueda ---")
    print("1. Buscar por nombre")
    print("2. Buscar por correo")
    print("3. Buscar por DNI")
    print("0. Volver")
    return input("Seleccione una opción: ")

def mostrar_usuarios(usuarios):
    """
    Muestra la lista de usuarios con formato
    """
    if not usuarios:
        print("No se encontraron usuarios.")
        return
    
    print("\n=== Lista de Usuarios ===")
    print("ID  | Nombre        | Apellido      | Correo                | Usuario")
    print("-" * 75)
    for usuario in usuarios:
        print(f"{usuario.id:<4} | {usuario.nombre:<13} | {usuario.apellido:<12} | {usuario.correo_electronico:<20} | {usuario.nombre_usuario}")

def mostrar_usuarios_ordenados(usuarios):
    """
    Muestra la lista de usuarios ordenados con formato detallado
    """
    if not usuarios:
        print("No hay usuarios para mostrar")
        return
    
    print("\nUsuarios ordenados:")
    print("ID  | Nombre        | Apellido      | Correo                | F. Nacimiento | DNI")
    print("-" * 80)
    for user in usuarios:
        print(f"{user.id:<4} | {user.nombre:<13} | {user.apellido:<12} | "
              f"{user.correo_electronico:<20} | {user.fecha_nacimiento} | {user.dni}")

def ejecutar_menu():
    """
    Ejecuta el menú principal con manejo de errores mejorado y validación continua
    """
    while True:
        try:
            opcion = mostrar_menu()
            
            if opcion == '1':
                nombre = solicitar_input_validado(
                    "Ingrese el nombre: ",
                    UserValidator.validar_nombre
                )
                
                apellido = solicitar_input_validado(
                    "Ingrese el apellido: ",
                    UserValidator.validar_apellido
                )
                
                correo = solicitar_input_validado(
                    "Ingrese el correo electrónico: ",
                    UserValidator.validar_correo
                )
                
                nombre_usuario = solicitar_input_validado(
                    "Ingrese el nombre de usuario: ",
                    UserValidator.validar_nombre_usuario
                )
                
                clave = solicitar_input_validado(
                    "Ingrese la clave: ",
                    UserValidator.validar_clave
                )
                
                fecha_nacimiento = solicitar_input_validado(
                    "Ingrese la fecha de nacimiento (YYYY-MM-DD): ",
                    UserValidator.validar_fecha_nacimiento
                )
                
                dni = solicitar_input_validado(
                    "Ingrese el DNI: ",
                    UserValidator.validar_dni
                )
                
                # Llamar a la función con los parámetros recolectados
                nuevo_usuario = UserService.crear_usuario_interactivo(
                    nombre=nombre,
                    apellido=apellido,
                    correo_electronico=correo,
                    nombre_usuario=nombre_usuario,
                    clave=clave,
                    fecha_nacimiento=fecha_nacimiento,
                    dni=dni
                )
                
            elif opcion == '2':
                opcion_busqueda = mostrar_submenu_busqueda()
                if opcion_busqueda == '1':
                    nombre = solicitar_input_validado(
                        "Ingrese el nombre a buscar: ",
                        UserValidator.validar_nombre
                    )
                    UserService.buscar_usuario(nombre=nombre)
                elif opcion_busqueda == '2':
                    correo = solicitar_input_validado(
                        "Ingrese el correo a buscar: ",
                        UserValidator.validar_correo
                    )
                    UserService.buscar_usuario(correo=correo)
                elif opcion_busqueda == '3':
                    dni = solicitar_input_validado(
                        "Ingrese el DNI a buscar: ",
                        UserValidator.validar_dni
                    )
                    UserService.buscar_usuario(dni=dni)
                    
            elif opcion == '3':
                id_usuario = solicitar_input_validado(
                    "Ingrese el ID del usuario a actualizar: ",
                    lambda x: int(x) > 0
                )
                UserService.actualizar_usuario_interactivo(int(id_usuario))
                
            elif opcion == '4':
                # Llamar al método sin argumentos
                UserService.eliminar_usuario_interactivo()
                
            elif opcion == '5':
                usuarios = UserService.listar_usuarios()
                mostrar_usuarios(usuarios)
                
            elif opcion == '6':
                print("\n=== Ordenamiento de Usuarios ===")
                usuarios_ordenados = UserService.ordenar_usuarios()
                if usuarios_ordenados:
                    mostrar_usuarios_ordenados(usuarios_ordenados)
                    input("\nPresione Enter para ver la lista completa ordenada...")
                
            elif opcion == '0':
                print("Volviendo al menú principal...")
                break
                
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
                
        except ValueError as e:
            print(f"\n⚠️ Error de validación: {str(e)}")
        except Exception as e:
            print(f"\n❌ Error inesperado: {str(e)}")
        
        input("\nPresione Enter para continuar...")

def user_menu():
    """
    Punto de entrada principal del menú de usuarios
    """
    print("\n=== Gestión de Usuarios ===")
    ejecutar_menu()

if __name__ == "__main__":
    user_menu()
