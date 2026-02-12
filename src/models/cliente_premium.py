from src.models.cliente import Cliente

class ClientePremium(Cliente):
    """
    Representa un cliente VIP con beneficios adicionales.
    Incluye un atributo extra 'descuento'.
    """

    def __init__(self, uid: int, nombre: str, email: str, telefono: str, descuento: float = 0.10):
        super().__init__(uid, nombre, email, telefono)
        self.descuento = descuento  # Atributo específico de esta subclase

    def mostrar_info(self) -> str:
        """
        Implementación polimórfica para cliente premium.
        Destaca el estatus VIP y el descuento activo.
        """
        return (f"⭐️ [PREMIUM] {self.nombre} | "
                f"Email: {self.email} | "
                f"Descuento: {int(self.descuento * 100)}%")

    def to_dict(self) -> dict:
        """
        Sobrescribe el método to_dict para incluir el descuento
        en la persistencia y exportación.
        """
        data = super().to_dict()
        data['descuento'] = self.descuento
        return data
    