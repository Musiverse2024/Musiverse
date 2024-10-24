# app/services/artist_service.py

from models.artist import Artista

def crear_artista(nombre_artista):
    nuevo_artista = Artista.crear(nombre_artista)
    if nuevo_artista:
        print(f"Artista creado exitosamente: {nuevo_artista}")
    else:
        print("Error al crear el artista.")
    return nuevo_artista

def obtener_artista(id_artista):
    artista = Artista.obtener(id_artista)
    if not artista:
        print(f"No se encontró ningún artista con el ID {id_artista}.")
    return artista

def listar_artistas():
    artistas = Artista.listar_todos()
    if not artistas:
        print("No se encontraron artistas en la base de datos.")
    return artistas

def actualizar_artista(id_artista, nuevo_nombre):
    artista = Artista.obtener(id_artista)
    if artista:
        artista.nombre_artista = nuevo_nombre
        if artista.actualizar():
            print("Artista actualizado exitosamente.")
            return True
        else:
            print("Error al actualizar el artista.")
    else:
        print(f"No se encontró ningún artista con el ID {id_artista}.")
    return False

def eliminar_artista(id_artista):
    artista = Artista.obtener(id_artista)
    if artista:
        if artista.eliminar():
            print("Artista eliminado exitosamente.")
            return True
        else:
            print("Error al eliminar el artista.")
    else:
        print(f"No se encontró ningún artista con el ID {id_artista}.")
    return False

def buscar_artistas_por_nombre(nombre):
    artistas = Artista.buscar_por_nombre(nombre)
    if not artistas:
        print(f"No se encontraron artistas con el nombre '{nombre}'.")
    return artistas

def contar_artistas():
    return Artista.contar()

def listar_artistas_paginados(pagina, por_pagina):
    artistas = Artista.listar_paginados(pagina, por_pagina)
    if not artistas:
        print(f"No hay artistas en la página {pagina}.")
    return artistas

# Implementa aquí las demás funciones de servicio para artistas



