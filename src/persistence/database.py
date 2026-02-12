import sqlite3
from src.core.constants import FilePaths

class DatabaseConnection:
    """Context Manager para manejar conexiones a SQLite de forma segura."""
    def __init__(self):
        self.db_path = FilePaths.DB_PATH
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row  # Permite acceder por nombre de columna
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            if exc_type:
                self.connection.rollback() # Rollback si hubo error
            else:
                self.connection.commit() # Commit si todo salió bien
            self.connection.close()
            