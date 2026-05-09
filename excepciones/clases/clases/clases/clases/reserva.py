# clases/reserva.py
from clases.cliente import Cliente
from clases.servicio import Servicio
from excepciones.excepciones_personalizadas import ReservaInvalidaError, ReservaError

class Reserva:
    """Clase que gestiona las reservas del sistema"""
    
    def __init__(self, reserva_id: int, cliente: Cliente, servicio: Servicio, duracion: float):
        self._reserva_id = reserva_id
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = "Pendiente"  # Pendiente, Confirmada, Cancelada
        
        self._validar_reserva()

    def _validar_reserva(self):
        """Validaciones al crear una reserva"""
        if self._duracion <= 0:
            raise ReservaInvalidaError("La duración debe ser mayor a 0")
        
        if not self._servicio.esta_disponible():
            raise ReservaInvalidaError(f"El servicio {self._servicio.nombre} no está disponible")

    def confirmar(self):
        """Confirma la reserva"""
        try:
            if self._estado == "Pendiente":
                costo = self._servicio.calcular_costo(self._duracion)
                self._estado = "Confirmada"
                self._cliente.agregar_reserva()
                print(f"✅ Reserva {self._reserva_id} confirmada. Costo total: ${costo:,.2f}")
                return costo
            else:
                raise ReservaInvalidaError("La reserva ya fue procesada")
        except Exception as e:
            raise ReservaError(f"Error al confirmar reserva: {e}")

    def cancelar(self):
        """Cancela la reserva"""
        try:
            if self._estado == "Confirmada":
                self._estado = "Cancelada"
                self._cliente.cancelar_reserva()
                print(f"❌ Reserva {self._reserva_id} cancelada correctamente.")
            else:
                raise ReservaInvalidaError("Solo se pueden cancelar reservas confirmadas")
        except Exception as e:
            raise ReservaError(f"Error al cancelar reserva: {e}")

    def __str__(self):
        return (f"Reserva[{self._reserva_id}] | Cliente: {self._cliente.nombre} | "
                f"Servicio: {self._servicio.nombre} | Duración: {self._duracion}h | "
                f"Estado: {self._estado}")
