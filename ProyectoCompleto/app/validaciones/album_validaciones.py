from datetime import datetime
from utils.base_service import BaseValidator, ValidationError

class AlbumValidaciones(BaseValidator):
    def __init__(self):
        self.errores = []

    def validar_nombre(self, nombre):
        """Valida el nombre del álbum"""
        try:
            if not nombre or not isinstance(nombre, str):
                raise ValidationError("El nombre del álbum es requerido")
            if len(nombre) > 100:
                raise ValidationError("El nombre del álbum no puede exceder los 100 caracteres")
            return True
        except ValidationError as e:
            self.errores.append(str(e))
            return False

    def validar_id_artista(self, id_artista):
        """Valida el ID del artista"""
        try:
            if not isinstance(id_artista, int):
                raise ValidationError("El ID del artista debe ser un número entero")
            if id_artista <= 0:
                raise ValidationError("ID de artista inválido")
            return True
        except ValidationError as e:
            self.errores.append(str(e))
            return False

    def validar_fecha_lanzamiento(self, fecha):
        """Valida la fecha de lanzamiento"""
        try:
            if isinstance(fecha, str):
                try:
                    datetime.strptime(fecha, '%Y-%m-%d')
                except ValueError:
                    raise ValidationError("Formato de fecha inválido (debe ser YYYY-MM-DD)")
            elif isinstance(fecha, int):
                current_year = datetime.now().year
                if fecha < 1900 or fecha > current_year:
                    raise ValidationError(f"El año debe estar entre 1900 y {current_year}")
            else:
                raise ValidationError("Formato de fecha inválido")
            return True
        except ValidationError as e:
            self.errores.append(str(e))
            return False

    def validate(self, data):
        """Valida los datos según las reglas de negocio"""
        self.errores = []  # Reiniciar errores
        
        if 'nombre' in data:
            self.validar_nombre(data['nombre'])
            
        if 'id_artista' in data:
            self.validar_id_artista(data['id_artista'])
            
        if 'fecha_lanzamiento' in data:
            self.validar_fecha_lanzamiento(data['fecha_lanzamiento'])

        if self.errores:
            raise ValidationError("; ".join(self.errores))
        
        return True 