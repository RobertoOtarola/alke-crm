"""
Excepciones personalizadas para el dominio de Alke CRM.
Permite un manejo granular de errores en capas superiores.
"""

class AlkeCRMException(Exception):
    """Excepción base para todas las excepciones del proyecto."""
    def __init__(self, message: str, code: int = 500):
        self.message = message
        self.code = code
        super().__init__(self.message)

class ValidationError(AlkeCRMException):
    """Excepción para errores de validación de datos."""
    def __init__(self, message: str = "Error de validación"):
        super().__init__(message, code=400)

class InvalidEmailError(ValidationError):
    """El email no tiene un formato válido."""
    def __init__(self, email: str):
        super().__init__(f"El email '{email}' no tiene un formato válido.")

class InvalidPhoneError(ValidationError):
    """El teléfono no tiene un formato válido."""
    def __init__(self, phone: str):
        super().__init__(f"El teléfono '{phone}' no es válido.")

class ClientAlreadyExistsError(AlkeCRMException):
    """El cliente ya existe (duplicidad de email)."""
    def __init__(self, identifier: str):
        super().__init__(f"El cliente '{identifier}' ya existe en el sistema.", code=409)

class ClientNotFoundError(AlkeCRMException):
    """No se encontró el cliente solicitado."""
    def __init__(self, identifier: str):
        super().__init__(f"No se encontró el cliente: {identifier}", code=404)

class DatabaseError(AlkeCRMException):
    """Error genérico de base de datos."""
    def __init__(self, error_original: str):
        super().__init__(f"Error de base de datos: {error_original}", code=500)
        