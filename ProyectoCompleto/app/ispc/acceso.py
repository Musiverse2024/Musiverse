from datetime import datetime

class Acceso:
    def __init__(self, id, fecha_hora, hora_salida, usuario):
        self.id = id
        self.fecha_hora = fecha_hora
        self.hora_salida = hora_salida
        self.usuario = usuario

    def get_id(self):
        return self.id

    def get_fecha_hora(self):
        return self.fecha_hora

    def get_hora_salida(self):
        return self.hora_salida

    def get_usuario(self):
        return self.usuario

    def set_hora_salida(self, hora_salida):
        self.hora_salida = hora_salida