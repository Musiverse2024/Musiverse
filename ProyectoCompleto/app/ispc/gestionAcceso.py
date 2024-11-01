import os
import pickle
from datetime import datetime
from ispc.acceso import Acceso

class GestionAcceso:
    ARCHIVO_ACCESOS = 'data/accesos.ispc'
    ARCHIVO_LOGS = 'data/logs.txt'

    @staticmethod
    def registrar_acceso(usuario):
        try:
            id = GestionAcceso.__generar_id()
            nuevo_acceso = Acceso(id, datetime.now(), None, usuario)
            
            accesos = GestionAcceso.cargar_accesos()
            accesos.append(nuevo_acceso)
            
            os.makedirs('data', exist_ok=True)
            
            with open(GestionAcceso.ARCHIVO_ACCESOS, 'wb') as archivo:
                pickle.dump(accesos, archivo)
            
            return nuevo_acceso
        except Exception as e:
            print(f"Error al registrar acceso: {str(e)}")
            return None

    @staticmethod
    def registrar_intento_fallido(username, password):
        try:
            with open(GestionAcceso.ARCHIVO_LOGS, 'a') as archivo:
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                archivo.write(f"[{fecha}] Intento fallido - Usuario: {username}, Clave: {password}\n")
        except Exception as e:
            print(f"Error al registrar intento fallido: {str(e)}")

    @staticmethod
    def cargar_accesos():
        if not os.path.exists(GestionAcceso.ARCHIVO_ACCESOS):
            return []
        try:
            with open(GestionAcceso.ARCHIVO_ACCESOS, 'rb') as archivo:
                return pickle.load(archivo)
        except Exception:
            return []

    @staticmethod
    def __generar_id():
        return datetime.now().strftime("%Y%m%d%H%M%S")