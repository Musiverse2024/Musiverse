import pickle
import os
import datetime
from validaciones import validar_nombre_usuario, validar_clave

class Usuario:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
    
    def __str__(self):
        return f'ID: {self.id}, Username: {self.username}, Email: {self.email}'

class Acceso:
    def __init__(self, id, fechaIngreso, fechaSalida, usuarioLogueado):
        self.id = id
        self.fechaIngreso = fechaIngreso
        self.fechaSalida = fechaSalida
        self.usuarioLogueado = usuarioLogueado
    
    def __str__(self):
        return f'Acceso ID: {self.id}, Usuario: {self.usuarioLogueado.username}, Ingreso: {self.fechaIngreso}, Salida: {self.fechaSalida}'

# Funciones de carga y guardado de datos
def cargar_usuarios():
    if os.path.exists('usuarios.ispc'):
        with open('usuarios.ispc', 'rb') as archivo:
            return pickle.load(archivo)
    return []

def guardar_usuarios(usuarios):
    with open('usuarios.ispc', 'wb') as archivo:
        pickle.dump(usuarios, archivo)

def cargar_accesos():
    if os.path.exists('accesos.ispc'):
        with open('accesos.ispc', 'rb') as archivo:
            return pickle.load(archivo)
    return []

def guardar_accesos(accesos):
    with open('accesos.ispc', 'wb') as archivo:
        pickle.dump(accesos, archivo)

# Función para agregar un nuevo usuario
def agregar_usuario():
    usuarios = cargar_usuarios()
    id = len(usuarios) + 1  # Genera un nuevo ID
    username = validar_nombre_usuario(input('\nIngrese el username: '), usuarios)
    password = validar_clave(input('Ingrese el password: '))
    email = input('Ingrese el email: ')
    
    nuevo_usuario = Usuario(id, username, password, email)
    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios)
    print('Usuario agregado exitosamente.\n')

# Función para modificar un usuario existente
def modificar_usuario():
    usuarios = cargar_usuarios()
    id = int(input('\nIngrese el ID del usuario a modificar: '))
    usuario = next((u for u in usuarios if u.id == id), None)
    
    if usuario:
        usuario.username = validar_nombre_usuario(input('Ingrese el nuevo username: '), usuarios)
        usuario.password = validar_clave(input('Ingrese la nueva password: '))
        usuario.email = input('Ingrese el nuevo email: ')
        guardar_usuarios(usuarios)
        print('Usuario modificado exitosamente.')
    else:
        print('Usuario no encontrado.')

# Función para eliminar un usuario
def eliminar_usuario():
    usuarios = cargar_usuarios()
    criterio = input('Eliminar por (1) Username o (2) Email: ')
    
    if criterio == '1':
        username = input('Ingrese el username del usuario a eliminar: ')
        usuario = next((u for u in usuarios if u.username == username), None)
    elif criterio == '2':
        email = input('Ingrese el email del usuario a eliminar: ')
        usuario = next((u for u in usuarios if u.email == email), None)
    else:
        print('Opción no válida.')
        return

    if usuario:
        usuarios.remove(usuario)
        guardar_usuarios(usuarios)
        print('Usuario eliminado exitosamente.')
    else:
        print('Usuario no encontrado.')

        
# Funcion para buscar un usuario
def buscar_usuario():
    usuarios = cargar_usuarios()
    criterio = input('\nBuscar por (1) Username o (2) Email: ')
    
    if criterio == '1':
        username = input('Ingrese el username del usuario a buscar: ')
        usuario = next((u for u in usuarios if u.username == username), None)
        print(f'Buscando por username: {username}')  # Verifica que está buscando correctamente por username
    elif criterio == '2':
        email = input('Ingrese el email del usuario a buscar: ')
        usuario = next((u for u in usuarios if u.email == email), None)
        print(f'Buscando por email: {email}')  # Verifica que está buscando correctamente por email
    else:
        print('Opción no válida.')
        return

    if usuario:
        print(f'Usuario encontrado: {usuario}')
    else:
        print('Usuario no encontrado.')



# Función para mostrar todos los usuarios
def mostrar_usuarios():
    usuarios = cargar_usuarios()
    if usuarios:
        for usuario in usuarios:
            print(usuario)
    else:
        print('No hay usuarios registrados.')

# Función para simular el ingreso al sistema
def ingresar_al_sistema():
    usuarios = cargar_usuarios()
    username = input('Ingrese su username: ')
    password = input('Ingrese su password: ')
    usuario = next((u for u in usuarios if u.username == username and u.password == password), None)
    
    if usuario:
        accesos = cargar_accesos()
        id_acceso = len(accesos) + 1
        fecha_ingreso = datetime.datetime.now()
        accesos.append(Acceso(id_acceso, fecha_ingreso, None, usuario))
        guardar_accesos(accesos)
        print(f'Bienvenido {usuario.username}')
        return usuario
    else:
        print('Usuario o contraseña incorrectos.')
        return None

# Función para registrar la salida del sistema
def registrar_salida(usuario_logueado):
    accesos = cargar_accesos()
    acceso = next((a for a in accesos if a.usuarioLogueado == usuario_logueado and a.fechaSalida is None), None)
    
    if acceso:
        acceso.fechaSalida = datetime.datetime.now()
        guardar_accesos(accesos)
        print('Sesión cerrada correctamente.')
    else:
        print('No se encontró una sesión activa.')