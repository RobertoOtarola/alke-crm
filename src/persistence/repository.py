from typing import List, Optional
from src.persistence.database import DatabaseConnection
from src.models.cliente import Cliente
from src.models.cliente_regular import ClienteRegular
from src.models.cliente_premium import ClientePremium
from src.models.cliente_corporativo import ClienteCorporativo
from src.core.exceptions import ClientAlreadyExistsError, ClientNotFoundError

class ClienteRepository:
    def __init__(self):
        self._inicializar_tabla()

    def _inicializar_tabla(self):
        with DatabaseConnection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    uid INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    telefono TEXT,
                    tipo TEXT NOT NULL,
                    empresa TEXT
                )
            """)

    def guardar(self, cliente: Cliente) -> int:
        data = cliente.to_dict()
        empresa = data.get('empresa') # None si no existe

        try:
            with DatabaseConnection() as conn:
                cursor = conn.cursor()
                # Verificar si es update o insert basado en UID
                if cliente.uid > 0: 
                    # Lógica de Update omitida por brevedad del MVP, asumimos Insert nuevo o manejo externo
                    pass 
                
                cursor.execute("""
                    INSERT INTO clientes (nombre, email, telefono, tipo, empresa)
                    VALUES (?, ?, ?, ?, ?)
                """, (data['nombre'], data['email'], data['telefono'], data['tipo'], empresa))
                return cursor.lastrowid
        except Exception as e:
            if "UNIQUE constraint failed" in str(e):
                raise ClientAlreadyExistsError(cliente.email)
            raise e

    def listar_todos(self) -> List[Cliente]:
        clientes = []
        with DatabaseConnection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM clientes")
            rows = cursor.fetchall()
            
            for row in rows:
                clientes.append(self._mapear_fila_a_objeto(row))
        return clientes

    def _mapear_fila_a_objeto(self, row) -> Cliente:
        """Factory method interno para reconstruir objetos desde SQL."""
        tipo = row['tipo']
        uid = row['uid']
        # Lógica de instanciación dinámica
        if tipo == 'ClienteCorporativo':
            return ClienteCorporativo(uid, row['nombre'], row['email'], row['telefono'], row['empresa'])
        elif tipo == 'ClientePremium':
            return ClientePremium(uid, row['nombre'], row['email'], row['telefono'])
        else:
            return ClienteRegular(uid, row['nombre'], row['email'], row['telefono'])
        