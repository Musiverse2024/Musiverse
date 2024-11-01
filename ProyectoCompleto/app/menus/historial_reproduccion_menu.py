def historial_reproduccion_menu():
    from services.historial_reproduccion_service import HistorialReproduccionService
    
    while True:
        print("\n=== Gestión de Historial de Reproducción ===")
        print("1. Registrar reproducción")
        print("2. Ver historial de usuario")
        print("3. Limpiar historial de usuario")
        print("4. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                id_usuario = int(input("Ingrese el ID del usuario: "))
                id_cancion = int(input("Ingrese el ID de la canción: "))
                resultado = HistorialReproduccionService.registrar_reproduccion(id_usuario, id_cancion)
                if resultado:
                    print("Reproducción registrada exitosamente")
            except ValueError:
                print("Error: Los IDs deben ser números")
                
        elif opcion == "2":
            try:
                id_usuario = int(input("Ingrese el ID del usuario: "))
                limite = int(input("Ingrese el número de registros a mostrar: "))
                historial = HistorialReproduccionService.obtener_historial_usuario(id_usuario, limite)
                if historial:
                    print("\nHistorial de reproducción:")
                    for registro in historial:
                        print(f"Canción: {registro['nombre_cancion']}, Fecha: {registro['fecha_reproduccion']}")
                else:
                    print("No hay historial de reproducción")
            except ValueError:
                print("Error: Los valores deben ser números")
                
        elif opcion == "3":
            try:
                id_usuario = int(input("Ingrese el ID del usuario: "))
                if HistorialReproduccionService.limpiar_historial(id_usuario):
                    print("Historial limpiado exitosamente")
                else:
                    print("No se pudo limpiar el historial")
            except ValueError:
                print("Error: El ID debe ser un número")
                
        elif opcion == "4":
            break
        else:
            print("Opción no válida") 