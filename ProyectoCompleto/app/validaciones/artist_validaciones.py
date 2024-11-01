from utils.base_service import BaseValidator, ValidationError

class ArtistValidaciones(BaseValidator):
    def __init__(self):
        self.errores = []

    def validar_nombre(self, nombre):
        """Valida el nombre del artista"""
        try:
            if not nombre or not isinstance(nombre, str):
                raise ValidationError("El nombre del artista es requerido")
            if len(nombre) > 100:
                raise ValidationError("El nombre del artista no puede exceder los 100 caracteres")
            return True
        except ValidationError as e:
            self.errores.append(str(e))
            return False

    def validar_id(self, id_artista):
        """Valida el ID del artista"""
        try:
            if not isinstance(id_artista, int):
                raise ValidationError("El ID debe ser un número entero")
            if id_artista <= 0:
                raise ValidationError("El ID debe ser mayor que cero")
            return True
        except ValidationError as e:
            self.errores.append(str(e))
            return False

    def validar_busqueda(self, termino):
        """Valida el término de búsqueda"""
        try:
            if not termino or not isinstance(termino, str):
                raise ValidationError("El término de búsqueda es requerido")
            if len(termino) > 100:
                raise ValidationError("El término de búsqueda no puede exceder los 100 caracteres")
            return True
        except ValidationError as e:
            self.errores.append(str(e))
            return False

    def validate(self, data):
        """Valida los datos según las reglas de negocio"""
        self.errores = []  # Reiniciar errores
        
        if 'nombre' in data:
            self.validar_nombre(data['nombre'])
            
        if 'id' in data:
            self.validar_id(data['id'])
            
        if 'nombre_busqueda' in data:
            self.validar_busqueda(data['nombre_busqueda'])

        if self.errores:
            raise ValidationError("; ".join(self.errores))
        
        return True

    def obtener_errores(self):
        """Retorna la lista de errores de validación"""
        return self.errores