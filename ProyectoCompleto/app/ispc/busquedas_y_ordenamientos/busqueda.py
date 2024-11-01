import os
from datetime import datetime
from .ordenamiento import OrdenamientoUsuarios

class BusquedaUsuarios:
    @staticmethod
    def busqueda_binaria_dni(usuarios, dni_buscar):
        # Crear directorio data si no existe
        os.makedirs('data', exist_ok=True)
        
        archivo_log = f'data/buscandoUsuarioPorDNI-{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
        
        if not usuarios:
            return None, "No hay usuarios registrados"
            
        # Verificar límites
        if dni_buscar < usuarios[0].get_dni():
            return None, "DNI más pequeño que el menor registrado"
        if dni_buscar > usuarios[-1].get_dni():
            return None, "DNI más grande que el mayor registrado"
            
        izquierda = 0
        derecha = len(usuarios) - 1
        intentos = 0
        
        with open(archivo_log, 'w') as log:
            log.write(f"Búsqueda Binaria por DNI: buscando el DNI {dni_buscar} en el archivo usuarios.ispc que contiene {len(usuarios)} usuarios.\n")
            
            while izquierda <= derecha:
                intentos += 1
                medio = (izquierda + derecha) // 2
                dni_actual = usuarios[medio].get_dni()
                
                mensaje_log = f"Intento {intentos}: DNI del usuario de la posición {medio} es {dni_actual} "
                
                if dni_actual == dni_buscar:
                    mensaje_log += f"por lo tanto se encontró el usuario en {intentos} intentos"
                    log.write(mensaje_log + "\n")
                    return usuarios[medio], f"Encontrado en {intentos} intentos"
                    
                elif dni_actual < dni_buscar:
                    mensaje_log += f"por lo tanto se buscará en la subsecuencia de la derecha (DNI más grandes) (posición {medio + 1} a {derecha})"
                    izquierda = medio + 1
                else:
                    mensaje_log += f"por lo tanto se buscará en la subsecuencia de la izquierda (DNI más chicos) (posición {izquierda} a {medio - 1})"
                    derecha = medio - 1
                    
                log.write(mensaje_log + "\n")
            
            mensaje_final = f"Se realizaron {intentos} intentos y no se encontró el DNI buscado"
            log.write(mensaje_final + "\n")
            return None, mensaje_final

    @staticmethod
    def busqueda_secuencial_email(usuarios, email):
        intentos = 0
        for usuario in usuarios:
            intentos += 1
            print(f"Intento {intentos}: {email} es {'igual' if usuario.get_email() == email else 'distinto'} a {usuario.get_email()}")
            if usuario.get_email() == email:
                return usuario, f"Encontrado en {intentos} intentos"
        return None, f"No se encontró el usuario con email {email} después de {intentos} intentos"

    @staticmethod
    def busqueda_username(usuarios, username):
        # Verificar si existe archivo ordenado
        if os.path.exists(OrdenamientoUsuarios.ARCHIVO_ORDENADO):
            return BusquedaUsuarios.__busqueda_binaria_username(usuarios, username)
        else:
            return BusquedaUsuarios.__busqueda_secuencial_username(usuarios, username)

    @staticmethod
    def __busqueda_binaria_username(usuarios, username):
        # Crear directorio data si no existe
        os.makedirs('data', exist_ok=True)
        
        archivo_log = f'data/buscandoUsuarioPorUsername-{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
        intentos = 0
        izquierda = 0
        derecha = len(usuarios) - 1
        
        with open(archivo_log, 'w') as log:
            log.write(f"Búsqueda Binaria por Username: buscando '{username}' en {len(usuarios)} usuarios.\n")
            
            while izquierda <= derecha:
                intentos += 1
                medio = (izquierda + derecha) // 2
                username_actual = usuarios[medio].get_username()
                
                mensaje_log = f"Intento {intentos}: Username en posición {medio} es '{username_actual}' "
                
                if username_actual == username:
                    mensaje_log += f"- Usuario encontrado en {intentos} intentos"
                    log.write(mensaje_log + "\n")
                    return usuarios[medio], f"Encontrado con búsqueda binaria en {intentos} intentos"
                elif username_actual < username:
                    mensaje_log += f"- Buscando en la mitad derecha (posición {medio + 1} a {derecha})"
                    izquierda = medio + 1
                else:
                    mensaje_log += f"- Buscando en la mitad izquierda (posición {izquierda} a {medio - 1})"
                    derecha = medio - 1
                
                log.write(mensaje_log + "\n")
            
            mensaje_final = f"No se encontró el username después de {intentos} intentos"
            log.write(mensaje_final + "\n")
            return None, f"No encontrado con búsqueda binaria después de {intentos} intentos"

    @staticmethod
    def __busqueda_secuencial_username(usuarios, username):
        intentos = 0
        for usuario in usuarios:
            intentos += 1
            print(f"Intento {intentos}: {username} es {'igual' if usuario.get_username() == username else 'distinto'} a {usuario.get_username()}")
            if usuario.get_username() == username:
                return usuario, f"Encontrado con búsqueda secuencial en {intentos} intentos"
        return None, f"No encontrado con búsqueda secuencial después de {intentos} intentos" 