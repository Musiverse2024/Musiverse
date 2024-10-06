import re
import datetime

def validar_entrada(texto, tipo_dato, mensaje_error):
    while True:
        entrada = input(texto)
        try:
            if tipo_dato == int:
                valor = int(entrada)
            elif tipo_dato == float:
                valor = float(entrada)
            elif tipo_dato == str:
                valor = str(entrada).strip()
            else:
                raise ValueError(f"Tipo de dato no soportado: {tipo_dato}")
            return valor
        except ValueError:
            print(mensaje_error)

def validar_fecha(fecha):
    while True:
        try:
            fecha_obj = datetime.datetime.strptime(fecha, "%Y-%m-%d")
            if fecha_obj > datetime.datetime.now():
                raise ValueError("La fecha no puede ser en el futuro.")
            return fecha
        except ValueError as e:
            print(f"Error en la fecha: {str(e)}. Ingrese nuevamente la fecha (AAAA-MM-DD): ")
            fecha = input()

def validar_nombre_usuario(nombre_usuario, usuarios):
    while True:
        if any(user.username == nombre_usuario for user in usuarios):
            print("Nombre de usuario ya registrado.")
            nombre_usuario = input("Ingrese un nuevo nombre de usuario: ")
        elif not (6 <= len(nombre_usuario) <= 12):
            print("El nombre de usuario debe tener entre 6 y 12 caracteres.")
            nombre_usuario = input("Ingrese un nuevo nombre de usuario: ")
        else:
            return nombre_usuario

def validar_clave(clave):
    while True:
        errores = []
        if len(clave) < 8:
            errores.append("La clave debe tener al menos 8 caracteres.")
        if not re.search(r"[a-z]", clave):
            errores.append("La clave debe contener al menos una letra minúscula.")
        if not re.search(r"[A-Z]", clave):
            errores.append("La clave debe contener al menos una letra mayúscula.")
        if not re.search(r"[0-9]", clave):
            errores.append("La clave debe contener al menos un número.")
        if not re.search(r"[^a-zA-Z0-9]", clave):
            errores.append("La clave debe contener al menos un carácter especial.")
        
        if errores:
            print("\n".join(errores))
            clave = input("Ingrese una nueva clave: ")
        else:
            return clave

def validar_email(email):
    # Validar el formato del email
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None
