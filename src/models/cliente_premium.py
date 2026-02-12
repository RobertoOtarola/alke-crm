from src.models.cliente import Cliente

class ClientePremium(Cliente):
    def __init__(self, uid: int, nombre: str, email: str, telefono: str, empresa: str):
        super().__init__(uid, nombre, email, telefono)
        self.empresa = empresa

    def mostrar_info(self) -> str:
        return f"🏢 [CORPORATIVO] {self.empresa} - Contacto: {self._nombre} ({self._email})"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data['empresa'] = self.empresa
        return data
    