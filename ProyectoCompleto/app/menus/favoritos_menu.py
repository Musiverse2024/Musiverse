def favoritos_menu():
    from services.favoritos_service import FavoritosService
    
    while True:
        print("\n=== Gestión de Favoritos ===")
        print("1. Agregar canción a favoritos")
        print("2. Eliminar canción de favoritos")
        print("3. Ver favoritos de usuario")
        print("4. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                id_usuario = int(input("Ingrese el ID del usuario: "))
                id_cancion = int(input("Ingrese el ID de la canción: "))
                resultado = FavoritosService.agregar_favorito(id_usuario, id_cancion)
                if resultado:
                    print("Canción agregada a favoritos exitosamente")
            except ValueError:
                print("Error: Los IDs deben ser números")
                
        elif opcion == "2":
            try:
                id_usuario = int(input("Ingrese el ID del usuario: "))
                id_cancion = int(input("Ingrese el ID de la canción: "))
                if FavoritosService.eliminar_favorito(id_usuario, id_cancion):
                    print("Canción eliminada de favoritos exitosamente")
                else:
                    print("No se pudo eliminar la canción de favoritos")
            except ValueError:
                print("Error: Los IDs deben ser números")
                
        elif opcion == "3":
            try:
                id_usuario = int(input("Ingrese el ID del usuario: "))
                favoritos = FavoritosService.obtener_favoritos_usuario(id_usuario)
                if favoritos:
                    print("\nCanciones favoritas:")
                    for cancion in favoritos:
                        print(f"ID: {cancion['id']}, Nombre: {cancion['nombre']}")
                else:
                    print("No hay canciones favoritas")
            except ValueError:
                print("Error: El ID debe ser un número")
                
        elif opcion == "4":
            break
        else:
            print("Opción no válida") 