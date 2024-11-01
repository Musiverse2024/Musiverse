from utils.base_service import BaseValidator, ValidationError
from datetime import datetime
import re

class UserValidator(BaseValidator):
    @staticmethod
    def validar_nombre(nombre):
        """Valida el nombre de usuario"""
        if not nombre or len(nombre) < 2 or not nombre.replace(" ", "").isalpha():
            raise ValueError("El nombre debe contener al menos 2 caracteres y solo letras")
        return True

    @staticmethod
    def validar_apellido(apellido):
        """Valida el apellido de usuario"""
        if not apellido or len(apellido) < 2 or not apellido.replace(" ", "").isalpha():
            raise ValueError("El apellido debe contener al menos 2 caracteres y solo letras")
        return True

    @staticmethod
    def validar_correo(correo):
        """Valida el correo electrónico"""
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not correo or not re.match(patron, correo):
            raise ValueError("Correo electrónico inválido")
        return True

    @staticmethod
    def validar_fecha_nacimiento(fecha):
        """Valida la fecha de nacimiento"""
        try:
            # Si no hay cambios o la fecha es None, retornar True
            if fecha is None or fecha == '':
                return True
            
            # Si ya es un objeto datetime o date, convertirlo a string
            from datetime import date
            if isinstance(fecha, (datetime, date)):
                fecha = fecha.strftime('%Y-%m-%d')
            # Validar el formato
            datetime.strptime(fecha, '%Y-%m-%d')
            return True
        except (ValueError, AttributeError) as e:
            raise ValueError("Formato de fecha inválido (YYYY-MM-DD)")

    @staticmethod
    def validar_dni(dni):
        """Valida el DNI"""
        # Convertir a string si es un número
        dni_str = str(dni) if dni is not None else ''
        if not dni_str.isdigit() or len(dni_str) != 8:
            raise ValueError("DNI debe contener 8 dígitos")
        return True

    @staticmethod
    def validar_nombre_usuario(nombre_usuario):
        """Valida el nombre de usuario del sistema"""
        if not nombre_usuario or len(nombre_usuario) < 4:
            raise ValueError("El nombre de usuario debe tener al menos 4 caracteres")
        # Verificar que solo contenga letras, números y guiones bajos
        if not all(c.isalnum() or c == '_' for c in nombre_usuario):
            raise ValueError("El nombre de usuario solo puede contener letras, números y guiones bajos")
        return True

    @staticmethod
    def validar_clave(clave):
        """Valida la clave del usuario"""
        if not clave or len(clave) < 6:
            raise ValueError("La clave debe tener al menos 6 caracteres")
        # Verificar que contenga al menos una letra y un número
        if not any(c.isalpha() for c in clave) or not any(c.isdigit() for c in clave):
            raise ValueError("La clave debe contener al menos una letra y un número")
        return True

    def validate(self, data, operation=None):
        """Método principal de validación"""
        errors = []
        validaciones = {
            'nombre': self.validar_nombre,
            'apellido': self.validar_apellido,
            'correo_electronico': self.validar_correo,
            'nombre_usuario': self.validar_nombre_usuario,
            'clave': self.validar_clave,
            'fecha_nacimiento': self.validar_fecha_nacimiento,
            'dni': self.validar_dni
        }
        
        for campo, validacion in validaciones.items():
            if campo in data:
                try:
                    validacion(data[campo])
                except ValueError as e:
                    errors.append(str(e))
                
        if errors:
            raise ValidationError("; ".join(errors))
        return True