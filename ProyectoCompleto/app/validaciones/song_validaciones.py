from utils.base_service import BaseValidator, ValidationError

class SongValidaciones(BaseValidator):
    def __init__(self):
        self.errores = []

    @staticmethod
    def validar_nombre(nombre):
        """Valida el nombre de la canción"""
        if not nombre or not isinstance(nombre, str):
            raise ValidationError("El nombre de la canción es requerido")
        if len(nombre) > 100:
            raise ValidationError("El nombre de la canción no puede exceder los 100 caracteres")
        return True

    @staticmethod
    def validar_id_album(id_album):
        """Valida el ID del álbum"""
        if not isinstance(id_album, int) or id_album <= 0:
            raise ValidationError("ID de álbum inválido")
        return True

    @staticmethod
    def validar_id_genero(id_genero):
        """Valida el ID del género"""
        if not isinstance(id_genero, int) or id_genero <= 0:
            raise ValidationError("ID de género inválido")
        return True

    def validate(self, data):
        """Valida los datos según las reglas de negocio"""
        errores = []
        
        if 'nombre' in data:
            try:
                self.validar_nombre(data['nombre'])
            except ValidationError as e:
                errores.append(str(e))

        if 'id_album' in data:
            try:
                self.validar_id_album(data['id_album'])
            except ValidationError as e:
                errores.append(str(e))

        if 'id_genero' in data:
            try:
                self.validar_id_genero(data['id_genero'])
            except ValidationError as e:
                errores.append(str(e))

        if errores:
            raise ValidationError("; ".join(errores))
        return True 