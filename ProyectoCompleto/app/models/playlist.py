class Playlist:
    def __init__(self, id, nombre, id_usuario):
        self.id = id
        self.nombre = nombre
        self.id_usuario = id_usuario

    def __str__(self):
        return f"Playlist: {self.nombre}"

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'id_usuario': self.id_usuario
        }
