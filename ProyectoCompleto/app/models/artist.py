# app/models/artist.py

class Artista:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return f"Artista: {self.nombre}"
