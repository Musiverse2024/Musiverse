import pickle
import os
from datetime import datetime
from .usuario import Usuario

class GestionUsuario:
    ARCHIVO_USUARIOS = 'data/usuarios.ispc'
    
    @staticmethod
    def crear_usuario(username, dni, password, email):
        try:
            # Generar ID único
            id = GestionUsuario.__generar_id()
            nuevo_usuario = Usuario(id, username, dni, password, email)
            
            usuarios = GestionUsuario.cargar_usuarios()
            usuarios.append(nuevo_usuario)
            # Ordenar por DNI antes de guardar
            usuarios.sort(key=lambda x: x.get_dni())
            
            GestionUsuario.__guardar_usuarios(usuarios)
            return nuevo_usuario
        except Exception as e:
            print(f"Error al crear usuario: {str(e)}")
            return None

    @staticmethod
    def validar_credenciales(username, password):
        usuarios = GestionUsuario.cargar_usuarios()
        for usuario in usuarios:
            if usuario.get_username() == username and usuario.get_password() == password:
                return usuario
        return None

    @staticmethod
    def cargar_usuarios():
        if not os.path.exists(GestionUsuario.ARCHIVO_USUARIOS):
            return []
        try:
            with open(GestionUsuario.ARCHIVO_USUARIOS, 'rb') as archivo:
                return pickle.load(archivo)
        except Exception:
            return []

    @staticmethod
    def __guardar_usuarios(usuarios):
        # Asegurar que el directorio data existe
        os.makedirs('data', exist_ok=True)
        with open(GestionUsuario.ARCHIVO_USUARIOS, 'wb') as archivo:
            pickle.dump(usuarios, archivo)

    @staticmethod
    def __generar_id():
        usuarios = GestionUsuario.cargar_usuarios()
        if not usuarios:
            return 1
        return max(usuario.get_id() for usuario in usuarios) + 1

    @staticmethod
    def modificar_usuario(id, **kwargs):
        usuarios = GestionUsuario.cargar_usuarios()
        for usuario in usuarios:
            if usuario.get_id() == id:
                for key, value in kwargs.items():
                    if hasattr(usuario, f'set_{key}'):
                        getattr(usuario, f'set_{key}')(value)
                GestionUsuario.__guardar_usuarios(usuarios)
                return True
        return False

    @staticmethod
    def eliminar_usuario(id):
        usuarios = GestionUsuario.cargar_usuarios()
        usuarios = [u for u in usuarios if u.get_id() != id]
        GestionUsuario.__guardar_usuarios(usuarios)