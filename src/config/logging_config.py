import os
import logging
from logging.handlers import RotatingFileHandler
from src.core.constants import FilePaths

def setup_logging():
    """Configura el logging con rotación de archivos."""
    
    # Asegurar que el directorio logs existe
    log_dir = os.path.dirname(FilePaths.LOG_PATH)
    os.makedirs(log_dir, exist_ok=True)

    # Configurar Handler con Rotación (Max 5MB, guarda 3 archivos previos)
    handler = RotatingFileHandler(
        FilePaths.LOG_PATH, 
        maxBytes=5*1024*1024, 
        backupCount=3,
        encoding='utf-8'
    )
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    handler.setFormatter(formatter)

    # Logger raíz
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    # Evitar duplicidad de handlers si se llama varias veces
    if logger.hasHandlers():
        logger.handlers.clear()
        logger.addHandler(handler)
