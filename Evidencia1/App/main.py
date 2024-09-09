import aritmetica
import login
from validaciones import validar_entrada, validar_fecha, validar_dni, validar_nombre_usuario, validar_clave
from usuarios import ManejoUsuarios
CYAN = '\033[36m'
print(CYAN)

def mostrar_menu_aritmetica():
    """Muestra el menú de opciones de cálculo y maneja la selección del usuario."""
    while True:
        print("\n●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●")
        print("              Menú de Aritmética")
        print("●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●")
        print("1. Sumar")
        print("2. Restar")
        print("3. Dividir")
        print("4. Multiplicar")
        print("5. Sumar varios números")
        print("6. Promedio de varios números")
        print("7. Salir")

        opcion = validar_entrada("Seleccione una opción: ", int, "Opción inválida. Intente nuevamente.")

        if opcion == 1:
            a = validar_entrada("Ingrese el primer número: ", float, "Número inválido. Intente nuevamente.")
            b = validar_entrada("Ingrese el segundo número: ", float, "Número inválido. Intente nuevamente.")
            print(f"Resultado de la suma: {aritmetica.sumar(a, b)}")
        
        elif opcion == 2:
            a = validar_entrada("Ingrese el primer número: ", float, "Número inválido. Intente nuevamente.")
            b = validar_entrada("Ingrese el segundo número: ", float, "Número inválido. Intente nuevamente.")
            print(f"Resultado de la resta: {aritmetica.restar(a, b)}")
        
        elif opcion == 3:
            a = validar_entrada("Ingrese el primer número: ", float, "Número inválido. Intente nuevamente.")
            b = validar_entrada("Ingrese el segundo número: ", float, "Número inválido. Intente nuevamente.")
            print(f"Resultado de la división: {aritmetica.dividir(a, b)}")
        
        elif opcion == 4:
            a = validar_entrada("Ingrese el primer número: ", float, "Número inválido. Intente nuevamente.")
            b = validar_entrada("Ingrese el segundo número: ", float, "Número inválido. Intente nuevamente.")
            print(f"Resultado de la multiplicación: {aritmetica.multiplicar(a, b)}")
        
        elif opcion == 5:
            numeros = []
            while True:
                numero = validar_entrada("Ingrese un número (o 'fin' para terminar): ", str, "Entrada inválida.")
                if numero.lower() == 'fin':
                    break
                try:
                    numeros.append(float(numero))
                except ValueError:
                    print("Número inválido. Intente nuevamente.")
            print(f"Suma de los números: {aritmetica.sumar_n(*numeros)}")
        
        elif opcion == 6:
            numeros = []
            while True:
                numero = validar_entrada("Ingrese un número (o 'fin' para terminar): ", str, "Entrada inválida.")
                if numero.lower() == 'fin':
                    break
                try:
                    numeros.append(float(numero))
                except ValueError:
                    print("Número inválido. Intente nuevamente.")
            print(f"Promedio de los números: {aritmetica.promedio_n(*numeros)}")
        
        elif opcion == 7:
            print("Saliendo de la aplicación...")
            break
        
        else:
            print("Opción no válida. Inténtelo nuevamente.")

def main():
    """Función principal que gestiona el flujo de la aplicación."""
    manejo_usuarios = ManejoUsuarios()

    while True:
        print("\n●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●")
        print("    Bienvenido a la aplicación de Aritmética")
        print("●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●")
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        print("3. Olvidé mi contraseña")

        opcion = validar_entrada("Seleccione una opción: ", int, "Opción inválida. Intente nuevamente.")

        if opcion == 1:
            if login.iniciar_sesion():
                mostrar_menu_aritmetica()
                break
        elif opcion == 2:
            nombre = input("Nombre: ").strip()
            apellido = input("Apellido: ").strip()
            dni = validar_entrada("DNI: ", str, "DNI inválido. Intente nuevamente.")
            dni = validar_dni(dni, manejo_usuarios.usuarios)  # Validación directa del DNI
            correo = input("Correo: ").strip()
            fecha_nacimiento = input("Fecha de nacimiento (AAAA-MM-DD): ").strip()
            fecha_nacimiento = validar_fecha(fecha_nacimiento)  # Validación directa de la fecha
            nombre_usuario = validar_entrada("Nombre de usuario: ", str, "Nombre de usuario inválido. Intente nuevamente.")
            nombre_usuario = validar_nombre_usuario(nombre_usuario, manejo_usuarios.usuarios)  # Validación directa del nombre de usuario

            while True:
                clave = input("Clave: ").strip()
                clave = validar_clave(clave)  # Validación directa de la clave
                resultado_registro = manejo_usuarios.registrar_usuario(nombre, apellido, dni, correo, fecha_nacimiento, nombre_usuario, clave)
                print(resultado_registro)
                if "clave" not in resultado_registro.lower():
                    break  # Salimos del bucle solo cuando la clave es válida
        
        elif opcion == 3:
            login.recuperar_contraseña()
        
        else:
            print("Opción no válida. Inténtelo nuevamente.")

if __name__ == "__main__":
    main()
