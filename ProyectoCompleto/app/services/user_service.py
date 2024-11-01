# app/services/user_service.py
from models.user import Usuario
from validaciones.user_validaciones import UserValidator
from utils.base_service import BaseService
from utils.sorting_algorithms import SortingAlgorithms
from datetime import datetime
from datetime import date

class UserService(BaseService):
    @classmethod
    def crear_usuario(cls, nombre, apellido, correo_electronico, nombre_usuario, clave, fecha_nacimiento, dni):
        """Crea un nuevo usuario con validaciones"""
        data = {
            'nombre': nombre,
            'apellido': apellido,
            'correo_electronico': correo_electronico,
            'nombre_usuario': nombre_usuario,
            'clave': clave,
            'fecha_nacimiento': fecha_nacimiento,
            'dni': dni
        }
        
        validator = UserValidator()
        if not cls.handle_validation(validator, data, "crear_usuario"):
            return None

        def db_operation(connection):
            cursor = connection.cursor()
            query = """INSERT INTO Usuario (nombre, apellido, correo_electronico, 
                      fecha_nacimiento, nombre_usuario, clave, dni) 
                      VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, (nombre, apellido, correo_electronico, 
                                 fecha_nacimiento, nombre_usuario, clave, dni))
            id_usuario = cursor.lastrowid
            return Usuario(id_usuario, nombre, apellido, correo_electronico, 
                         fecha_nacimiento, nombre_usuario, clave, dni)

        return cls.handle_db_operation(db_operation, "Error al crear usuario")

    @classmethod
    def obtener_usuario(cls, id_usuario):
        """Obtiene un usuario por su ID"""
        def db_operation(connection):
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM Usuario WHERE id = %s"
            cursor.execute(query, (id_usuario,))
            result = cursor.fetchone()
            return Usuario(**result) if result else None

        return cls.handle_db_operation(db_operation, "Error al obtener usuario")

    @classmethod
    def actualizar_usuario(cls, usuario):
        """Actualiza un usuario existente"""
        try:
            # Primero validar los datos
            validator = UserValidator()
            datos_usuario = usuario.to_dict()
            
            # Asegurar que los tipos de datos sean correctos
            if datos_usuario['fecha_nacimiento'] is not None:
                if isinstance(datos_usuario['fecha_nacimiento'], (datetime, date)):
                    datos_usuario['fecha_nacimiento'] = datos_usuario['fecha_nacimiento'].strftime('%Y-%m-%d')
            
            # Asegurar que el DNI sea string
            if datos_usuario['dni'] is not None:
                datos_usuario['dni'] = str(datos_usuario['dni'])
            
            def db_operation(connection):
                cursor = connection.cursor()
                query = """UPDATE Usuario SET nombre = %s, apellido = %s, 
                          correo_electronico = %s, fecha_nacimiento = %s,
                          nombre_usuario = %s, clave = %s, dni = %s 
                          WHERE id = %s"""
                cursor.execute(query, (usuario.nombre, usuario.apellido, 
                                     usuario.correo_electronico, datos_usuario['fecha_nacimiento'],
                                     usuario.nombre_usuario, usuario.clave, 
                                     datos_usuario['dni'], usuario.id))
                return True  # Si llegamos aquí, la actualización fue exitosa

            return cls.handle_db_operation(db_operation, "Error al actualizar usuario")
        except Exception as e:
            print(f"Error inesperado en actualizar_usuario: {str(e)}")
            return False

    @classmethod
    def eliminar_usuario(cls, usuario):
        """Elimina un usuario y sus relaciones"""
        def db_operation(connection):
            cursor = connection.cursor()
            # Primero eliminar relaciones
            cursor.execute("DELETE FROM UsuarioGenero WHERE id_usuario = %s", (usuario.id,))
            # Luego eliminar el usuario
            cursor.execute("DELETE FROM Usuario WHERE id = %s", (usuario.id,))
            return cursor.rowcount > 0

        return cls.handle_db_operation(db_operation, "Error al eliminar usuario")

    @classmethod
    def obtener_generos_usuario(cls, id_usuario):
        """Obtiene los géneros musicales del usuario"""
        def db_operation(connection):
            cursor = connection.cursor(dictionary=True)
            query = """
                SELECT g.* FROM GeneroMusical g
                JOIN UsuarioGenero ug ON g.id = ug.id_genero
                WHERE ug.id_usuario = %s
            """
            cursor.execute(query, (id_usuario,))
            return cursor.fetchall()

        return cls.handle_db_operation(db_operation, "Error al obtener géneros del usuario")

    @classmethod
    def ordenar_usuarios(cls):
        """Ordena usuarios según criterio y método seleccionado"""
        def _obtener_criterio_ordenamiento():
            print("\nElija el criterio de ordenamiento:")
            opciones_criterio = {
                '1': ('nombre', lambda user: user.nombre.lower()),
                '2': ('apellido', lambda user: user.apellido.lower()),
                '3': ('fecha de nacimiento', lambda user: datetime.strptime(user.fecha_nacimiento, '%Y-%m-%d')),
                '4': ('DNI', lambda user: user.dni),
                '5': ('correo electrónico', lambda user: user.correo_electronico.lower())
            }
            
            for key, (nombre, _) in opciones_criterio.items():
                print(f"{key}. Por {nombre.title()}")
                
            criterio = input("Seleccione una opción: ")
            return opciones_criterio.get(criterio)

        def _obtener_metodo_ordenamiento():
            print("\nElija el método de ordenamiento:")
            opciones_ordenamiento = {
                '1': ('Burbuja', SortingAlgorithms.bubble_sort),
                '2': ('Selección', SortingAlgorithms.selection_sort),
                '3': ('Inserción', SortingAlgorithms.insertion_sort),
                '4': ('Quicksort', SortingAlgorithms.quicksort),
                '5': ('Python sort', lambda arr, key: sorted(arr, key=key))
            }
            
            for key, (nombre, _) in opciones_ordenamiento.items():
                print(f"{key}. {nombre}")
                
            opcion = input("Seleccione una opción: ")
            return opciones_ordenamiento.get(opcion)

        try:
            usuarios = cls.listar_usuarios()
            if not usuarios:
                print("No hay usuarios para ordenar")
                return []

            # Obtener criterio de ordenamiento
            criterio_info = _obtener_criterio_ordenamiento()
            if not criterio_info:
                print("Criterio no válido")
                return usuarios
                
            criterio_nombre, key_func = criterio_info

            # Obtener método de ordenamiento
            metodo_info = _obtener_metodo_ordenamiento()
            if not metodo_info:
                print("Método no válido")
                return usuarios
                
            nombre_metodo, metodo_ordenamiento = metodo_info
            
            print(f"\nOrdenando por {criterio_nombre} usando {nombre_metodo}...")
            resultado = metodo_ordenamiento(usuarios.copy(), key=key_func)
            print("Ordenamiento completado!")
            
            return resultado

        except Exception as e:
            print(f"Error al ordenar: {str(e)}")
            return usuarios

    @staticmethod
    def _mostrar_usuarios_preview(usuarios, criterio):
        for user in usuarios:
            valor = getattr(user, criterio.replace(' ', '_'))
            print(f"{valor}")

    @classmethod
    def buscar_usuario(cls, nombre=None, correo=None, dni=None):
        """
        Busca usuarios por diferentes criterios
        Args:
            nombre: Nombre a buscar
            correo: Correo electrónico a buscar
            dni: DNI a buscar
        Returns:
            Lista de usuarios que coinciden con el criterio
        """
        def db_operation(connection):
            cursor = connection.cursor(dictionary=True)
            
            if nombre:
                query = "SELECT * FROM Usuario WHERE nombre LIKE %s"
                param = f"%{nombre}%"
            elif correo:
                query = "SELECT * FROM Usuario WHERE correo_electronico = %s"
                param = correo
            elif dni:
                query = "SELECT * FROM Usuario WHERE dni = %s"
                param = dni
            else:
                return []

            cursor.execute(query, (param,))
            results = cursor.fetchall()
            usuarios = [Usuario(**row) for row in results]
            
            if usuarios:
                print("\nUsuarios encontrados:")
                for usuario in usuarios:
                    print(f"ID: {usuario.id}, Nombre: {usuario.nombre} {usuario.apellido}, "
                          f"Correo: {usuario.correo_electronico}")
            else:
                print("No se encontraron usuarios.")
                
            return usuarios

        return cls.handle_db_operation(db_operation, "Error al buscar usuario") or []

    @classmethod
    def crear_usuario_interactivo(cls, nombre, apellido, correo_electronico, nombre_usuario, clave, fecha_nacimiento, dni):
        """Crea un nuevo usuario de forma interactiva"""
        try:
            nuevo_usuario = cls.crear_usuario(
                nombre=nombre,
                apellido=apellido,
                correo_electronico=correo_electronico,
                nombre_usuario=nombre_usuario,
                clave=clave,
                fecha_nacimiento=fecha_nacimiento,
                dni=dni
            )
            
            if nuevo_usuario:
                print(f"Usuario creado exitosamente: {nuevo_usuario}")
            else:
                print("Error al crear el usuario")
                
            return nuevo_usuario
            
        except Exception as e:
            print(f"Error inesperado: {str(e)}")
            return None

    @classmethod
    def actualizar_usuario_interactivo(cls, id_usuario):
        """Actualiza un usuario de forma interactiva"""
        try:
            usuario = cls.obtener_usuario(id_usuario)
            if usuario:
                print(f"Usuario actual: {usuario}")
                # Solicitar nuevos datos
                nuevo_nombre = input("Nuevo nombre (Enter para mantener actual): ").strip()
                if nuevo_nombre:
                    usuario.nombre = nuevo_nombre
                    
                nuevo_apellido = input("Nuevo apellido (Enter para mantener actual): ").strip()
                if nuevo_apellido:
                    usuario.apellido = nuevo_apellido
                    
                nuevo_correo = input("Nuevo correo (Enter para mantener actual): ").strip()
                if nuevo_correo:
                    usuario.correo_electronico = nuevo_correo
                    
                nuevo_usuario = input("Nuevo nombre de usuario (Enter para mantener actual): ").strip()
                if nuevo_usuario:
                    usuario.nombre_usuario = nuevo_usuario
                    
                nueva_clave = input("Nueva clave (Enter para mantener actual): ").strip()
                if nueva_clave:
                    usuario.clave = nueva_clave
                    
                nueva_fecha = input("Nueva fecha de nacimiento (YYYY-MM-DD) (Enter para mantener actual): ").strip()
                if nueva_fecha:
                    usuario.fecha_nacimiento = nueva_fecha
                    
                nuevo_dni = input("Nuevo DNI (Enter para mantener actual): ").strip()
                if nuevo_dni:
                    usuario.dni = nuevo_dni
                
                # Intentar actualizar
                if cls.actualizar_usuario(usuario):
                    print(f"Usuario actualizado exitosamente: {usuario}")
                else:
                    print("Error al actualizar el usuario")
            else:
                print("Usuario no encontrado")
        except ValueError as e:
            print(f"Error de validación: {str(e)}")
        except Exception as e:
            print(f"Error inesperado: {str(e)}")

    @classmethod
    def eliminar_usuario_interactivo(cls):
        """Elimina un usuario de forma interactiva"""
        try:
            id_usuario = input("Ingrese el ID del usuario a eliminar: ").strip()
            if not id_usuario.isdigit():
                print("El ID debe ser un número")
                return
                
            id_usuario = int(id_usuario)
            usuario = cls.obtener_usuario(id_usuario)
            
            if usuario:
                confirmacion = input(f"¿Está seguro de que desea eliminar al usuario {usuario.nombre} {usuario.apellido}? (s/n): ")
                if confirmacion.lower() == 's':
                    if cls.eliminar_usuario(usuario):
                        print("Usuario eliminado exitosamente.")
                    else:
                        print("Error al eliminar el usuario.")
                else:
                    print("Operación de eliminación cancelada.")
            else:
                print("Usuario no encontrado.")
        except ValueError as e:
            print(f"Error de validación: {str(e)}")
        except Exception as e:
            print(f"Error inesperado: {str(e)}")

    @classmethod
    def listar_usuarios(cls):
        """Lista todos los usuarios"""
        def db_operation(connection):
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM Usuario"
            cursor.execute(query)
            results = cursor.fetchall()
            return [Usuario(**row) for row in results]
            
        return cls.handle_db_operation(db_operation, "Error al listar usuarios") or []