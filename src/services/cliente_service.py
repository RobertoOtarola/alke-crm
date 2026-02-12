from typing import List, Dict, Any
from src.models.cliente import Cliente
from src.models.cliente_regular import ClienteRegular
from src.models.cliente_premium import ClientePremium
from src.models.cliente_corporativo import ClienteCorporativo
from src.persistence.repository import ClienteRepository
from src.core.exceptions import AlkeCRMException

class ClienteService:
    def __init__(self):
        self.repository = ClienteRepository()

    def crear_cliente(self, tipo: str, datos: Dict[str, Any]) -> Cliente:
        """
        Factory Method: Crea la instancia correcta según el tipo
        y la persiste en la base de datos.
        """
        cliente = None
        
        # Lógica de creación (Factory)
        if tipo == 'regular':
            cliente = ClienteRegular(
                uid=0, # El ID se asigna en BD
                nombre=datos['nombre'],
                email=datos['email'],
                telefono=datos['telefono']
            )
        elif tipo == 'premium':
            cliente = ClientePremium(
                uid=0,
                nombre=datos['nombre'],
                email=datos['email'],
                telefono=datos['telefono']
            )
        elif tipo == 'corporativo':
            cliente = ClienteCorporativo(
                uid=0,
                nombre=datos['nombre'],
                email=datos['email'],
                telefono=datos['telefono'],
                empresa=datos['empresa']
            )
        else:
            raise AlkeCRMException(f"Tipo de cliente '{tipo}' no válido.")

        # Persistir
        nuevo_uid = self.repository.guardar(cliente)
        return cliente

    def obtener_todos(self) -> List[Cliente]:
        """Recupera la lista completa de objetos Cliente."""
        return self.repository.listar_todos()
    