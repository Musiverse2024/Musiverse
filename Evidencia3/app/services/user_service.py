# app/services/user_service.py
from models.user import Usuario

def crear_usuario(nombre, apellido, correo_electronico, contraseña, fecha_nacimiento, pais, ciudad):
    return Usuario.crear(nombre, apellido, correo_electronico, contraseña, fecha_nacimiento, pais, ciudad)

def obtener_usuario(id_usuario):
    return Usuario.obtener(id_usuario)

def actualizar_usuario(usuario):
    return usuario.actualizar()

def eliminar_usuario(usuario):
    return usuario.eliminar()

def listar_usuarios():
    return Usuario.listar_todos()

def ordenar_usuarios():
    usuarios = listar_usuarios()
    print("\nElija el método de ordenamiento:")
    print("1. Burbuja")
    print("2. Selección")
    print("3. Inserción")
    print("4. Quicksort")
    print("5. Usar sort() de Python")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        # Implementación del método burbuja
        n = len(usuarios)
        for i in range(n):
            for j in range(0, n - i - 1):
                if usuarios[j].nombre > usuarios[j + 1].nombre:
                    usuarios[j], usuarios[j + 1] = usuarios[j + 1], usuarios[j]
        print("Ordenando usuarios con Burbuja...")
    elif opcion == '2':
        # Implementación del método de selección
        for i in range(len(usuarios)):
            min_idx = i
            for j in range(i + 1, len(usuarios)):
                if usuarios[min_idx].nombre > usuarios[j].nombre:
                    min_idx = j
            usuarios[i], usuarios[min_idx] = usuarios[min_idx], usuarios[i]
        print("Ordenando usuarios con Selección...")
    elif opcion == '3':
        # Implementación del método de inserción
        for i in range(1, len(usuarios)):
            key = usuarios[i]
            j = i - 1
            while j >= 0 and key.nombre < usuarios[j].nombre:
                usuarios[j + 1] = usuarios[j]
                j -= 1
            usuarios[j + 1] = key
        print("Ordenando usuarios con Inserción...")
    elif opcion == '4':
        # Implementación del método Quicksort
        def quicksort(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                quicksort(arr, low, pi - 1)
                quicksort(arr, pi + 1, high)

        def partition(arr, low, high):
            i = low - 1
            pivot = arr[high].nombre
            for j in range(low, high):
                if arr[j].nombre <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        quicksort(usuarios, 0, len(usuarios) - 1)
        print("Ordenando usuarios con Quicksort...")
    elif opcion == '5':
        usuarios.sort(key=lambda user: user.nombre)
        print("Usuarios ordenados usando sort() de Python.")
    else:
        print("Opción no válida.")
    
    print("Usuarios ordenados:", [user.nombre for user in usuarios])

def buscar_usuario():
    nombre = input("Ingrese el nombre de usuario a buscar: ")
    usuarios = listar_usuarios()
    encontrado = next((user for user in usuarios if user.nombre == nombre), None)
    if encontrado:
        print(f"Usuario encontrado: {encontrado}")
    else:
        print("Usuario no encontrado.")

def crear_usuario_interactivo():
    nombre = input("Ingrese el nombre del usuario: ")
    apellido = input("Ingrese el apellido del usuario: ")
    correo_electronico = input("Ingrese el correo electrónico del usuario: ")
    contraseña = input("Ingrese la contraseña del usuario: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del usuario (YYYY-MM-DD): ")
    pais = input("Ingrese el país del usuario: ")
    ciudad = input("Ingrese la ciudad del usuario: ")
    
    nuevo_usuario = crear_usuario(nombre, apellido, correo_electronico, contraseña, fecha_nacimiento, pais, ciudad)
    if nuevo_usuario:
        print(f"Usuario creado exitosamente: {nuevo_usuario}")
    else:
        print("Error al crear el usuario.")

def actualizar_usuario_interactivo():
    id_usuario = int(input("Ingrese el ID del usuario a actualizar: "))
    usuario = obtener_usuario(id_usuario)
    if usuario:
        print(f"Usuario actual: {usuario}")
        usuario.nombre = input("Nuevo nombre (deje en blanco para no cambiar): ") or usuario.nombre
        usuario.apellido = input("Nuevo apellido (deje en blanco para no cambiar): ") or usuario.apellido
        usuario.correo_electronico = input("Nuevo correo electrónico (deje en blanco para no cambiar): ") or usuario.correo_electronico
        usuario.contraseña = input("Nueva contraseña (deje en blanco para no cambiar): ") or usuario.contraseña
        usuario.fecha_nacimiento = input("Nueva fecha de nacimiento (YYYY-MM-DD) (deje en blanco para no cambiar): ") or usuario.fecha_nacimiento
        usuario.pais = input("Nuevo país (deje en blanco para no cambiar): ") or usuario.pais
        usuario.ciudad = input("Nueva ciudad (deje en blanco para no cambiar): ") or usuario.ciudad
        
        if actualizar_usuario(usuario):
            print(f"Usuario actualizado exitosamente: {usuario}")
        else:
            print("Error al actualizar el usuario.")
    else:
        print("Usuario no encontrado.")

def eliminar_usuario_interactivo():
    id_usuario = int(input("Ingrese el ID del usuario a eliminar: "))
    usuario = obtener_usuario(id_usuario)
    if usuario:
        confirmacion = input(f"¿Está seguro de que desea eliminar al usuario {usuario.nombre} {usuario.apellido}? (s/n): ")
        if confirmacion.lower() == 's':
            if eliminar_usuario(usuario):
                print("Usuario eliminado exitosamente.")
            else:
                print("Error al eliminar el usuario.")
        else:
            print("Operación de eliminación cancelada.")
    else:
        print("Usuario no encontrado.")