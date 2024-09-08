import datetime
from usuarios import ManejoUsuarios
from captcha.image import ImageCaptcha
import random
import string
import os

# Inicializamos el objeto para manejar usuarios
manejo_usuarios = ManejoUsuarios()

def generar_captcha():
    """Genera un CAPTCHA de texto y devuelve tanto la imagen como el texto"""
    letras = string.ascii_letters + string.digits
    texto_captcha = ''.join(random.choice(letras) for i in range(6))
    
    # Genera la imagen CAPTCHA
    image = ImageCaptcha(width=280, height=90)
    imagen_captcha = image.generate_image(texto_captcha)
    imagen_captcha.save('captcha.png')  # Guarda la imagen temporalmente
    
    return texto_captcha

def iniciar_sesion():
    """Gestiona el proceso de inicio de sesión con manejo de intentos fallidos y opciones para volver al menú principal."""
    max_intentos = 4
    intentos = 0

    while True:
        # Generar y mostrar CAPTCHA antes de cada intento
        captcha_texto = generar_captcha()
        print("\nPor favor, resuelva el CAPTCHA para continuar:")
        print("(Se ha generado una imagen 'captcha.png' en el directorio actual)")
        
        # Mostrar la imagen CAPTCHA generada
        # Aquí podrías abrir la imagen si estás en un entorno de escritorio:
        # os.system('captcha.png') # Abre la imagen en el visor predeterminado
        captcha_usuario = input("Ingrese el texto del CAPTCHA: ").strip()

        # Verificar si el CAPTCHA es correcto
        if captcha_usuario != captcha_texto:
            print("CAPTCHA incorrecto. Inténtelo de nuevo.")
            continue  # Volver al principio del bucle si el CAPTCHA falla

        # Continuar con el proceso de login
        print("\nInicio de sesión:")
        nombre_usuario = input("Nombre de usuario: ").strip()
        clave = input("Clave: ").strip()

        if manejo_usuarios.validar_acceso(nombre_usuario, clave):
            print("Acceso concedido.")
            registrar_ingreso(nombre_usuario)
            return True
        else:
            intentos += 1
            print("Nombre de usuario o clave incorrectos.")
            registrar_log(nombre_usuario, False)

        if intentos >= max_intentos:
            print("Número máximo de intentos alcanzado. Su acceso ha sido bloqueado.")
            return False

        opcion = input("¿Desea intentar nuevamente? (1. Sí, 2. No): ").strip()
        if opcion == "2":
            return False

def registrar_ingreso(nombre_usuario):
    """Registra el ingreso del usuario en un archivo."""
    with open("ingresos.txt", "a") as file:
        file.write(f"{nombre_usuario},{datetime.datetime.now()}\n")

def registrar_log(nombre_usuario, exito):
    """Registra los intentos de inicio de sesión en un archivo de log."""
    with open("log.txt", "a") as file:
        resultado = "Éxito" if exito else "Fallo"
        file.write(f"{nombre_usuario},{resultado},{datetime.datetime.now()}\n")

def recuperar_contraseña():
    """Función placeholder para recuperar contraseñas (no implementada)."""
    print("Funcionalidad de recuperación de contraseña no implementada.")
