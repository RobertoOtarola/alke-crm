import re
from src.core.exceptions import InvalidEmailError

def validar_email(email: str) -> None:
    """Valida el formato del email usando Regex estándar."""
    patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(patron, email):
        raise InvalidEmailError(email)
    