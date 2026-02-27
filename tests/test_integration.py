import pytest
import os
from src.services.cliente_service import ClienteService
from src.services.export_service import ExportService
from src.persistence.database import DatabaseConnection
from src.core.constants import FilePaths

# Usamos una BD temporal para testing
FilePaths.DB_PATH = "tests/test_db.sqlite"

@pytest.fixture(autouse=True)
def setup_teardown():
    # Setup: Eliminar BD previa
    if os.path.exists(FilePaths.DB_PATH):
        os.remove(FilePaths.DB_PATH)
    yield
    # Teardown: Limpiar
    if os.path.exists(FilePaths.DB_PATH):
        os.remove(FilePaths.DB_PATH)

def test_flujo_completo_mvp():
    service = ClienteService()
    
    # 1. Crear Cliente
    datos = {"nombre": "Test Integration", "email": "test@integration.com", "telefono": "+56911111111"}
    cliente = service.crear_cliente("regular", datos)
    
    assert cliente.uid > 0
    
    # 2. Recuperar y verificar persistencia
    clientes_db = service.obtener_todos()
    assert len(clientes_db) == 1
    assert clientes_db[0].email == "test@integration.com"
    
    # 3. Exportar
    json_path = ExportService.exportar_json(clientes_db, "tests/export_test.json")
    assert os.path.exists(json_path)
    
    # Limpieza archivo exportado
    if os.path.exists(json_path):
        os.remove(json_path)
