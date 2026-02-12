from src.models.cliente import Cliente

class ClienteRegular(Cliente):
    """
    Representa un cliente estándar del sistema.
    Hereda todos los atributos básicos de Cliente.
    """
    
    def __init__(self, uid: int, nombre: str, email: str, telefono: str):
        super().__init__(uid, nombre, email, telefono)

    def mostrar_info(self) -> str:
        """
        Implementación polimórfica para cliente regular.
        Muestra la información en formato estándar.
        """
        return f"👤 [REGULAR] {self.nombre} | Email: {self.email} | Tel: {self.telefono}"
    