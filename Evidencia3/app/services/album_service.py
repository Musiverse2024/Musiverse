# app/services/album_service.py

from models.album import Album

def crear_album(titulo, id_artista, ano_lanzamiento):
    nuevo_album = Album.crear(titulo, id_artista, ano_lanzamiento)
    if nuevo_album:
        print(f"Álbum creado exitosamente: {nuevo_album}")
    else:
        print("Error al crear el álbum.")
    return nuevo_album

def obtener_album(id_album):
    album = Album.obtener(id_album)
    if not album:
        print(f"No se encontró ningún álbum con el ID {id_album}.")
    return album

def listar_albumes():
    albumes = Album.listar_todos()
    if not albumes:
        print("No se encontraron álbumes en la base de datos.")
    return albumes

def listar_albumes_por_artista(id_artista):
    albumes = Album.buscar_por_artista(id_artista)
    if not albumes:
        print(f"No se encontraron álbumes para el artista con ID {id_artista}.")
    return albumes

def actualizar_album(id_album, nuevo_titulo, nuevo_ano):
    album = Album.obtener(id_album)
    if album:
        album.titulo = nuevo_titulo
        album.ano_lanzamiento = nuevo_ano
        if album.actualizar():
            print("Álbum actualizado exitosamente.")
            return True
        else:
            print("Error al actualizar el álbum.")
    else:
        print(f"No se encontró ningún álbum con el ID {id_album}.")
    return False

def eliminar_album(id_album):
    album = Album.obtener(id_album)
    if album:
        if album.eliminar():
            print("Álbum eliminado exitosamente.")
            return True
        else:
            print("Error al eliminar el álbum.")
    else:
        print(f"No se encontró ningún álbum con el ID {id_album}.")
    return False

def buscar_albumes_por_titulo(titulo):
    albumes = Album.buscar_por_titulo(titulo)
    if not albumes:
        print(f"No se encontraron álbumes con el título '{titulo}'.")
    return albumes

def contar_albumes():
    return Album.contar()

def listar_albumes_paginados(pagina, por_pagina):
    albumes = Album.listar_paginados(pagina, por_pagina)
    if not albumes:
        print(f"No hay álbumes en la página {pagina}.")
    return albumes

# Implementa aquí las demás funciones de servicio para álbumes

