import os
import sys
import pickle

# Agregar el directorio raíz al path de Python
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from ispc.gestionUsuario import GestionUsuario
from ispc.gestionAcceso import GestionAcceso
from ispc.validaciones import AccesosValidaciones
from ispc.busquedas_y_ordenamientos.ordenamiento import OrdenamientoUsuarios
from ispc.busquedas_y_ordenamientos.busqueda import BusquedaUsuarios

def solicitar_input_validado(mensaje, validacion_func, permitir_vacio=False):
    while True:
        try:
            valor = input(mensaje)
            if permitir_vacio and valor == "":
                return None
            validacion_func(valor)
            return valor
        except ValueError as e:
            print(f"\n⚠️ Error de validación: {str(e)}")
            print("Por favor, intente nuevamente.")

def mostrar_menu_crud_usuarios():
    while True:
        print("\n=== CRUD Usuarios ===")
        print("1. Crear usuario")
        print("2. Modificar usuario")
        print("3. Eliminar usuario")
        print("4. Listar usuarios")
        print("0. Volver")
        
        try:
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                username = solicitar_input_validado(
                    "Ingrese nombre de usuario: ",
                    AccesosValidaciones.validar_username
                )
                dni = solicitar_input_validado(
                    "Ingrese DNI: ",
                    AccesosValidaciones.validar_dni
                )
                password = solicitar_input_validado(
                    "Ingrese contraseña: ",
                    AccesosValidaciones.validar_password
                )
                email = solicitar_input_validado(
                    "Ingrese email: ",
                    AccesosValidaciones.validar_email
                )
                
                usuario = GestionUsuario.crear_usuario(username, dni, password, email)
                if usuario:
                    print("\n✅ Usuario creado exitosamente")
                else:
                    print("\n❌ Error al crear usuario")
                    
            elif opcion == "2":
                id_usuario = int(input("Ingrese ID del usuario a modificar: "))
                
                username = solicitar_input_validado(
                    "Nuevo nombre de usuario (Enter para mantener): ",
                    AccesosValidaciones.validar_username,
                    permitir_vacio=True
                )
                
                dni = solicitar_input_validado(
                    "Nuevo DNI (Enter para mantener): ",
                    AccesosValidaciones.validar_dni,
                    permitir_vacio=True
                )
                
                password = solicitar_input_validado(
                    "Nueva contraseña (Enter para mantener): ",
                    AccesosValidaciones.validar_password,
                    permitir_vacio=True
                )
                
                email = solicitar_input_validado(
                    "Nuevo email (Enter para mantener): ",
                    AccesosValidaciones.validar_email,
                    permitir_vacio=True
                )
                
                kwargs = {}
                if username is not None: kwargs['username'] = username
                if dni is not None: kwargs['dni'] = dni
                if password is not None: kwargs['password'] = password
                if email is not None: kwargs['email'] = email
                
                if GestionUsuario.modificar_usuario(id_usuario, **kwargs):
                    print("\n✅ Usuario modificado exitosamente")
                else:
                    print("\n❌ Usuario no encontrado")
                    
            elif opcion == "3":
                id_usuario = int(input("Ingrese ID del usuario a eliminar: "))
                if GestionUsuario.eliminar_usuario(id_usuario):
                    print("\n✅ Usuario eliminado exitosamente")
                else:
                    print("\n❌ Usuario no encontrado")
                    
            elif opcion == "4":
                usuarios = GestionUsuario.cargar_usuarios()
                if usuarios:
                    print("\n=== Lista de Usuarios ===")
                    for usuario in usuarios:
                        print(f"ID: {usuario.get_id()} | Username: {usuario.get_username()} | DNI: {usuario.get_dni()}")
                else:
                    print("\nNo hay usuarios registrados")
                    
            elif opcion == "0":
                break
                
            input("\nPresione Enter para continuar...")
            
        except ValueError as e:
            print(f"\n⚠️ Error de validación: {str(e)}")
        except Exception as e:
            print(f"\n❌ Error inesperado: {str(e)}")

def mostrar_menu_datos_accesos():
    while True:
        print("\n=== Datos de Accesos ===")
        print("1. Ver registro de accesos")
        print("2. Ver intentos fallidos")
        print("0. Volver")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            accesos = GestionAcceso.cargar_accesos()
            if accesos:
                print("\n=== Registro de Accesos ===")
                for acceso in accesos:
                    usuario = acceso.get_usuario()
                    print(f"Usuario: {usuario.get_username()} | Fecha: {acceso.get_fecha_hora()}")
            else:
                print("\nNo hay registros de accesos")
                
        elif opcion == "2":
            try:
                with open(GestionAcceso.ARCHIVO_LOGS, 'r') as archivo:
                    logs = archivo.readlines()
                    if logs:
                        print("\n=== Intentos Fallidos de Acceso ===")
                        for log in logs:
                            print(log.strip())
                    else:
                        print("\nNo hay registros de intentos fallidos")
            except FileNotFoundError:
                print("\nNo hay registros de intentos fallidos")
                
        elif opcion == "0":
            break
            
        input("\nPresione Enter para continuar...")

def mostrar_menu_ordenamiento_busqueda():
    while True:
        print("\n=== Ordenamiento y Búsqueda de Usuarios ===")
        print("1. Ordenar usuarios por username")
        print("2. Buscar usuario por DNI")
        print("3. Buscar usuario por username")
        print("4. Buscar usuario por email")
        print("5. Mostrar todos los usuarios")
        print("0. Volver")
        
        try:
            opcion = input("Seleccione una opción: ")
            usuarios = GestionUsuario.cargar_usuarios()
            
            if opcion == "1":
                if usuarios:
                    usuarios_ordenados = OrdenamientoUsuarios.ordenar_por_username(usuarios)
                    print("\n=== Usuarios Ordenados por Username ===")
                    for usuario in usuarios_ordenados:
                        print(f"Username: {usuario.get_username()} | DNI: {usuario.get_dni()}")
                else:
                    print("\nNo hay usuarios para ordenar")
                    
            elif opcion == "2":
                if not usuarios:
                    print("\nNo hay usuarios registrados")
                    continue
                    
                dni = solicitar_input_validado(
                    "Ingrese el DNI a buscar: ",
                    AccesosValidaciones.validar_dni
                )
                usuario, mensaje = BusquedaUsuarios.busqueda_binaria_dni(usuarios, int(dni))
                if usuario:
                    print(f"\nUsuario encontrado: {usuario.get_username()} ({mensaje})")
                else:
                    print(f"\nNo encontrado: {mensaje}")
                    
            elif opcion == "3":
                if not usuarios:
                    print("\nNo hay usuarios registrados")
                    continue
                    
                username = input("Ingrese el username a buscar: ")
                usuario, mensaje = BusquedaUsuarios.busqueda_username(usuarios, username)
                if usuario:
                    print(f"\nUsuario encontrado: {usuario.get_username()} ({mensaje})")
                else:
                    print(f"\nNo encontrado: {mensaje}")
                    
            elif opcion == "4":
                if not usuarios:
                    print("\nNo hay usuarios registrados")
                    continue
                    
                email = input("Ingrese el email a buscar: ")
                usuario, mensaje = BusquedaUsuarios.busqueda_secuencial_email(usuarios, email)
                if usuario:
                    print(f"\nUsuario encontrado: {usuario.get_username()} ({mensaje})")
                else:
                    print(f"\nNo encontrado: {mensaje}")

            elif opcion == "5":
                print("\n=== Usuarios en archivo usuarios.ispc ===")
                if usuarios:
                    for usuario in usuarios:
                        print(f"Username: {usuario.get_username()} | DNI: {usuario.get_dni()}")
                else:
                    print("No hay usuarios registrados")

                print("\n=== Usuarios en archivo usuariosOrdenadosPorUsername.ispc ===")
                if os.path.exists(OrdenamientoUsuarios.ARCHIVO_ORDENADO):
                    try:
                        with open(OrdenamientoUsuarios.ARCHIVO_ORDENADO, 'rb') as archivo:
                            usuarios_ordenados = pickle.load(archivo)
                            for usuario in usuarios_ordenados:
                                print(f"Username: {usuario.get_username()} | DNI: {usuario.get_dni()}")
                    except Exception as e:
                        print(f"Error al leer archivo ordenado: {str(e)}")
                else:
                    print("No existe el archivo de usuarios ordenados")
                    
            elif opcion == "0":
                break
                
            input("\nPresione Enter para continuar...")
            
        except Exception as e:
            print(f"\n❌ Error inesperado: {str(e)}")

def validar_acceso():
    print("\n=== Acceso al Sistema ===")
    try:
        username = solicitar_input_validado(
            "Usuario: ",
            AccesosValidaciones.validar_username
        )
        password = solicitar_input_validado(
            "Contraseña: ",
            AccesosValidaciones.validar_password
        )
        
        usuario = GestionUsuario.validar_credenciales(username, password)
        
        if usuario:
            GestionAcceso.registrar_acceso(usuario)
            print("\n✅ ¡Bienvenido al sistema!")
            return True
        else:
            GestionAcceso.registrar_intento_fallido(username, password)
            print("\n❌ Usuario o contraseña incorrectos")
            return False
    except ValueError as e:
        print(f"\n⚠️ Error de validación: {str(e)}")
        return False

def mostrar_menu_inicial():
    while True:
        print("\n=== Sistema ISPC ===")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Continuar como invitado")
        print("0. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            if validar_acceso():
                mostrar_menu_principal()
        elif opcion == "3":
            mostrar_menu_invitado()
        elif opcion == "0":
            break
        else:
            print("Opción no válida")

def registrar_usuario():
    print("\n=== Registro de Usuario ===")
    try:
        username = solicitar_input_validado(
            "Ingrese nombre de usuario: ",
            AccesosValidaciones.validar_username
        )
        dni = solicitar_input_validado(
            "Ingrese DNI: ",
            AccesosValidaciones.validar_dni
        )
        password = solicitar_input_validado(
            "Ingrese contraseña: ",
            AccesosValidaciones.validar_password
        )
        email = solicitar_input_validado(
            "Ingrese email: ",
            AccesosValidaciones.validar_email
        )
        
        usuario = GestionUsuario.crear_usuario(username, dni, password, email)
        if usuario:
            print("\n✅ Usuario registrado exitosamente")
            if validar_acceso():
                mostrar_menu_principal()
        else:
            print("\n❌ Error al registrar usuario")
    except ValueError as e:
        print(f"\n⚠️ Error de validación: {str(e)}")

def mostrar_menu_invitado():
    while True:
        print("\n=== Menú Invitado ===")
        print("1. Ver usuarios registrados")
        print("2. Buscar usuarios")
        print("0. Volver")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            usuarios = GestionUsuario.cargar_usuarios()
            if usuarios:
                print("\n=== Lista de Usuarios ===")
                for usuario in usuarios:
                    print(f"Username: {usuario.get_username()} | DNI: {usuario.get_dni()}")
            else:
                print("\nNo hay usuarios registrados")
        elif opcion == "2":
            mostrar_menu_ordenamiento_busqueda()
        elif opcion == "0":
            break
        
        input("\nPresione Enter para continuar...")

def mostrar_menu_principal():
    while True:
        print("\n=== Accesos ISPC ===")
        print("1. CRUD Usuarios")
        print("2. Mostrar datos de accesos")
        print("3. Ordenamiento y búsqueda de usuarios")
        print("0. Cerrar sesión")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_menu_crud_usuarios()
        elif opcion == "2":
            mostrar_menu_datos_accesos()
        elif opcion == "3":
            mostrar_menu_ordenamiento_busqueda()
        elif opcion == "0":
            break
        else:
            print("Opción no válida")

def accesos_ispc_menu():
    limpiar_pantalla()
    mostrar_menu_inicial()

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')