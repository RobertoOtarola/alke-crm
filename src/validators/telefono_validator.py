import re
from src.core.exceptions import InvalidPhoneError

def validar_telefono(telefono: str) -> None:
    """Valida formato internacional básico (ej: +56912345678)."""
    patron = r"^\+?[1-9]\d{1,14}$"
    if not re.match(patron, telefono):
        raise InvalidPhoneError(telefono)