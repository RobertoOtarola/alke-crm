"""
Constantes globales del sistema Alke CRM.
Define rutas de archivos y configuraciones estáticas.
"""
import os

class FilePaths:
    """Rutas relativas para almacenamiento de datos y logs."""
    # Usamos os.path para asegurar compatibilidad entre Windows/Mac/Linux
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    DB_PATH = os.path.join(BASE_DIR, "data", "database.db")
    LOG_PATH = os.path.join(BASE_DIR, "logs", "app.log")
    EXPORT_JSON = os.path.join(BASE_DIR, "data", "clientes.json")
    EXPORT_CSV = os.path.join(BASE_DIR, "data", "clientes.csv")

class ClientType:
    """Tipos de clientes permitidos en el sistema."""
    REGULAR = "Regular"
    PREMIUM = "Premium"
    CORPORATE = "Corporativo"
    