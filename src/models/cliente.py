from abc import ABC, abstractmethod
from src.validators.email_validator import validar_email
from src.validators.telefono_validator import validar_telefono

class Cliente(ABC):
    def __init__(self, uid: int, nombre: str, email: str, telefono: str):
        self._uid = uid
        self._nombre = nombre
        self._email = email
        self._telefono = telefono
        
        # Validaciones al instanciar
        validar_email(self._email)
        validar_telefono(self._telefono)

    @property
    def uid(self):
        return self._uid

    @property
    def nombre(self):
        return self._nombre
        
    @property
    def email(self):
        return self._email

    # --- ESTO FALTABA ---
    @property
    def telefono(self):
        return self._telefono
    # --------------------

    @abstractmethod
    def mostrar_info(self) -> str:
        """Método polimórfico que deben implementar las subclases."""
        pass

    def to_dict(self) -> dict:
        """Serialización para base de datos y exportaciones."""
        return {
            "uid": self._uid,
            "nombre": self._nombre,
            "email": self._email,
            "telefono": self._telefono,
            "tipo": self.__class__.__name__
        }
    