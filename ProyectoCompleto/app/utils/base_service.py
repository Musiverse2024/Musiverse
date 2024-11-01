from utils.db_utils import get_db_connection, close_db_connection
from mysql.connector import Error
from abc import ABC, abstractmethod

class ValidationError(Exception):
    """Excepción personalizada para errores de validación"""
    pass

class BaseValidator(ABC):
    """Clase base abstracta para validaciones"""
    @abstractmethod
    def validate(self, data):
        """Método abstracto que deben implementar todas las validaciones"""
        pass

class BaseService:
    @staticmethod
    def handle_db_operation(operation, error_msg="Error en operación de base de datos"):
        """
        Maneja operaciones de base de datos de manera segura
        
        Args:
            operation: Función que realiza la operación de BD
            error_msg: Mensaje personalizado en caso de error
        """
        connection = get_db_connection()
        if connection:
            try:
                result = operation(connection)
                connection.commit()
                return result
            except Error as e:
                print(f"{error_msg}: {e}")
                if connection.is_connected():
                    connection.rollback()
                return None
            finally:
                close_db_connection(connection)
        return None

    @staticmethod
    def handle_validation(validator: BaseValidator, data, operation_name):
        """
        Maneja validaciones de manera uniforme
        
        Args:
            validator: Instancia de BaseValidator
            data: Datos a validar
            operation_name: Nombre de la operación para mensajes de error
        """
        try:
            validator.validate(data)
            return True
        except ValidationError as e:
            print(f"Error de validación en {operation_name}: {e}")
            return False
        except Exception as e:
            print(f"Error inesperado en {operation_name}: {e}")
            return False

    @staticmethod
    def handle_transaction(operations):
        """
        Maneja múltiples operaciones en una transacción
        
        Args:
            operations: Lista de tuplas (operación, mensaje_error)
        """
        connection = get_db_connection()
        if connection:
            try:
                results = []
                for operation, error_msg in operations:
                    result = operation(connection)
                    if result is None:
                        raise Error(error_msg)
                    results.append(result)
                connection.commit()
                return results
            except Error as e:
                print(f"Error en transacción: {e}")
                if connection.is_connected():
                    connection.rollback()
                return None
            finally:
                close_db_connection(connection)
        return None 