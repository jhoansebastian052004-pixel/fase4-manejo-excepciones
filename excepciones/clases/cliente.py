# clases/cliente.py
from excepciones.excepciones_personalizadas import DatosInvalidosError, ClienteNoEncontradoError

class Cliente:
    """Clase que representa a un cliente de Software FJ"""
    
    def __init__(self, cliente_id: int, nombre: str, email: str, telefono: str):
        self._cliente_id = cliente_id
        self._nombre = nombre
        self._email = email
        self._telefono = telefono
        self._reservas_activas = 0
        
        # Validaciones al crear el cliente
        self._validar_datos()

    def _validar_datos(self):
        """Valida los datos del cliente"""
        if not self._nombre or len(self._nombre.strip()) < 3:
            raise DatosInvalidosError("El nombre debe tener al menos 3 caracteres")
        
        if "@" not in self._email or "." not in self._email:
            raise DatosInvalidosError("El email no es válido")
        
        if not self._telefono or len(self._telefono) < 7:
            raise DatosInvalidosError("El teléfono no es válido")

    # Getters
    @property
    def cliente_id(self):
        return self._cliente_id

    @property
    def nombre(self):
        return self._nombre

    @property
    def email(self):
        return self._email

    def agregar_reserva(self):
        """Incrementa el contador de reservas activas"""
        self._reservas_activas += 1

    def cancelar_reserva(self):
        """Decrementa el contador de reservas activas"""
        if self._reservas_activas > 0:
            self._reservas_activas -= 1

    def __str__(self):
        return f"Cliente[{self._cliente_id}] - {self._nombre} | Email: {self._email}"
