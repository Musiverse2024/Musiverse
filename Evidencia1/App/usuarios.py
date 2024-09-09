import random
import datetime
from validaciones import validar_dni, validar_nombre_usuario, validar_clave, validar_fecha
import aritmetica  # Importar el módulo de aritmética

class Usuario:
    def __init__(self, nombre, apellido, dni, correo, fecha_nacimiento, nombre_usuario, clave):
        self.nombre = nombre.strip()  # Eliminamos espacios en blanco
        self.apellido = apellido.strip()
        self.dni = dni.strip()
        self.correo = correo.strip()
        self.fecha_nacimiento = fecha_nacimiento.strip()  # Asegurarse de que la fecha esté en el formato correcto
        self.nombre_usuario = nombre_usuario.strip()
        self.clave = clave.strip()

class ManejoUsuarios:
    def __init__(self):
        self.usuarios = {}
        self.cargar_usuarios_desde_archivo()

    def cargar_usuarios_desde_archivo(self):
        """Carga los usuarios desde el archivo 'usuariosCreados.txt'."""
        try:
            with open("usuariosCreados.txt", "r") as file:
                for linea in file:
                    linea = linea.strip()
                    if linea == "":
                        continue  # Ignorar líneas vacías

                    try:
                        # Nos aseguramos de que las líneas tengan exactamente 7 valores
                        nombre, apellido, dni, correo, fecha_nacimiento, nombre_usuario, clave = linea.split(',')
                        # Creamos un objeto usuario con los datos cargados, eliminando espacios en blanco
                        usuario = Usuario(nombre, apellido, dni, correo, fecha_nacimiento, nombre_usuario, clave)
                        self.usuarios[dni] = usuario
                    except ValueError as e:
                        print(f"Error al procesar la línea: '{linea}'. Se esperaban 7 valores. {e}")
        except FileNotFoundError:
            print("No se encontró el archivo de usuarios. Se creará uno nuevo al registrar usuarios.")

    def generar_operacion_aleatoria(self):
        """Genera una operación aritmética aleatoria para el captcha."""
        operaciones = ['suma', 'resta', 'multiplicacion', 'division', 'promedio']
        operacion = random.choice(operaciones)

        if operacion == 'suma':
            a = round(random.uniform(1, 100), 2)
            b = round(random.uniform(1, 100), 2)
            resultado_correcto = round(aritmetica.sumar(a, b), 2)
            return f"{a} + {b}", resultado_correcto

        elif operacion == 'resta':
            a = round(random.uniform(1, 100), 2)
            b = round(random.uniform(1, 100), 2)
            resultado_correcto = round(aritmetica.restar(a, b), 2)
            return f"{a} - {b}", resultado_correcto

        elif operacion == 'multiplicacion':
            a = round(random.uniform(1, 100), 2)
            b = round(random.uniform(1, 100), 2)
            resultado_correcto = round(aritmetica.multiplicar(a, b), 2)
            return f"{a} * {b}", resultado_correcto

        elif operacion == 'division':
            a = round(random.uniform(1, 100), 2)
            b = round(random.uniform(1, 100), 2)
            resultado_correcto = round(aritmetica.dividir(a, b), 2)
            return f"{a} / {b}", resultado_correcto

        elif operacion == 'promedio':
            args = [round(random.uniform(1, 100), 2) for _ in range(random.randint(2, 5))]
            resultado_correcto = round(aritmetica.promedio_n(*args), 2)
            args_str = ', '.join(map(str, args))
            return f"Promedio de {args_str}", resultado_correcto

    def captcha(self):
        """Captcha empleando las funciones aritmeticas"""
        while True:
            operacion, resultado_correcto = self.generar_operacion_aleatoria()
            print(f"Resuelve la siguiente operación: {operacion}")
            
            try:
                respuesta_usuario = float(input("Introduce el resultado: "))
            except ValueError:
                print("Por favor, introduce un número válido.")
                continue

            if abs(respuesta_usuario - resultado_correcto) < 0.01:
                return True
            else:
                print("Respuesta incorrecta. Intenta de nuevo o escribe 'salir' para cancelar.")
                intento = input("¿Deseas intentar de nuevo o salir? (intentar/salir): ").strip().lower()
                if intento == 'salir':
                    return False

    def registrar_usuario(self, nombre, apellido, dni, correo, fecha_nacimiento, nombre_usuario, clave):
        try:
            dni = validar_dni(dni, self.usuarios)
        except ValueError as e:
            return f"Error en DNI: {str(e)}"

        try:
            nombre_usuario = validar_nombre_usuario(nombre_usuario, self.usuarios)
        except ValueError as e:
            return f"Error en nombre de usuario: {str(e)}"

        try:
            clave = validar_clave(clave)
        except ValueError as e:
            return f"Error en clave: {str(e)}"
        
        try:
            fecha_nacimiento = validar_fecha(fecha_nacimiento)
        except ValueError as e:
            return f"Error en fecha de nacimiento: {str(e)}"

        # Llamar a la función de captcha
        if not self.captcha():
            return "Registro cancelado por el usuario."

        # Crear un nuevo usuario
        usuario = Usuario(nombre, apellido, dni, correo, fecha_nacimiento, nombre_usuario, clave)
        self.usuarios[dni] = usuario
        self.registrar_usuario_en_archivo(usuario)
        return "Usuario registrado correctamente."

    def registrar_usuario_en_archivo(self, usuario):
        """Registra un usuario nuevo en el archivo 'usuariosCreados.txt'."""
        with open("usuariosCreados.txt", "a", newline='') as file:
            file.write(f"{usuario.nombre},{usuario.apellido},{usuario.dni},{usuario.correo},{usuario.fecha_nacimiento},{usuario.nombre_usuario},{usuario.clave}\n")

    def validar_acceso(self, nombre_usuario, clave):
        """Valida el acceso comprobando el nombre de usuario y la clave."""
        nombre_usuario = nombre_usuario.strip()
        clave = clave.strip()
        print(f"Validando acceso para: {nombre_usuario} con clave: {clave}")  # Agrega esta línea para depuración

        for user in self.usuarios.values():
            print(f"Comparando con usuario: {user.nombre_usuario} y clave: {user.clave}")  # Agrega esta línea para depuración
            if user.nombre_usuario == nombre_usuario and user.clave == clave:
                self.registrar_ingreso(user.nombre_usuario)
                return True
        return False

    def registrar_ingreso(self, nombre_usuario):
        """Registra el ingreso del usuario."""
        with open("ingresos.txt", "a") as file:
            file.write(f"{nombre_usuario},{datetime.datetime.now()}\n")