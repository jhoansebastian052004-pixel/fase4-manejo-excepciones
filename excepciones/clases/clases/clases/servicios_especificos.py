# clases/servicios_especificos.py
from clases.servicio import Servicio
from excepciones.excepciones_personalizadas import ServicioNoDisponibleError

class ReservaSala(Servicio):
    """Servicio de reserva de salas"""
    
    def __init__(self, servicio_id: int, nombre: str, precio_base: float, capacidad: int):
        super().__init__(servicio_id, nombre, precio_base)
        self._capacidad = capacidad
        self._tipo = "Sala"

    def calcular_costo(self, duracion: float = 1.0) -> float:
        """Costo = precio_base * duracion + cargo por capacidad"""
        if not self.esta_disponible():
            raise ServicioNoDisponibleError(self.nombre)
        return round(self._precio_base * duracion + (self._capacidad * 5000), 2)

    def describir(self) -> str:
        return f"🏠 {self._nombre} - Capacidad: {self._capacidad} personas | Precio por hora: ${self._precio_base:,.2f}"


class AlquilerEquipo(Servicio):
    """Servicio de alquiler de equipos"""
    
    def __init__(self, servicio_id: int, nombre: str, precio_base: float, equipo: str):
        super().__init__(servicio_id, nombre, precio_base)
        self._equipo = equipo
        self._tipo = "Equipo"

    def calcular_costo(self, duracion: float = 1.0) -> float:
        """Costo con recargo por equipo especializado"""
        if not self.esta_disponible():
            raise ServicioNoDisponibleError(self.nombre)
        return round(self._precio_base * duracion * 1.15, 2)  # 15% recargo

    def describir(self) -> str:
        return f"💻 {self._nombre} ({self._equipo}) | Precio por día: ${self._precio_base:,.2f}"


class AsesoriaEspecializada(Servicio):
    """Servicio de asesorías especializadas"""
    
    def __init__(self, servicio_id: int, nombre: str, precio_base: float, experto: str):
        super().__init__(servicio_id, nombre, precio_base)
        self._experto = experto
        self._tipo = "Asesoría"

    def calcular_costo(self, duracion: float = 1.0) -> float:
        """Costo por hora con especialista"""
        if not self.esta_disponible():
            raise ServicioNoDisponibleError(self.nombre)
        return round(self._precio_base * duracion, 2)

    def describir(self) -> str:
        return f"👨‍💼 {self._nombre} con {self._experto} | Precio por hora: ${self._precio_base:,.2f}"
