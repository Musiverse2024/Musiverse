class AccesosValidaciones:
    @staticmethod
    def validar_username(username):
        if not username:
            raise ValueError("El username no puede estar vacío")
        if len(username) < 3:
            raise ValueError("El username debe tener al menos 3 caracteres")
        if not username.isalnum():
            raise ValueError("El username solo puede contener letras y números")
        return True

    @staticmethod
    def validar_dni(dni):
        if not dni:
            raise ValueError("El DNI no puede estar vacío")
        if not str(dni).isdigit():
            raise ValueError("El DNI debe contener solo números")
        if len(str(dni)) < 7 or len(str(dni)) > 8:
            raise ValueError("El DNI debe tener entre 7 y 8 dígitos")
        return True

    @staticmethod
    def validar_email(email):
        if not email:
            raise ValueError("El email no puede estar vacío")
        if not '@' in email or not '.' in email:
            raise ValueError("Formato de email inválido")
        if len(email.split('@')[0]) < 1:
            raise ValueError("El email debe tener un nombre antes del @")
        if len(email.split('@')[1].split('.')[0]) < 1:
            raise ValueError("El email debe tener un dominio válido")
        return True

    @staticmethod
    def validar_password(password):
        if not password:
            raise ValueError("La contraseña no puede estar vacía")
        if len(password) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres")
        if not any(c.isupper() for c in password):
            raise ValueError("La contraseña debe contener al menos una mayúscula")
        if not any(c.isdigit() for c in password):
            raise ValueError("La contraseña debe contener al menos un número")
        return True