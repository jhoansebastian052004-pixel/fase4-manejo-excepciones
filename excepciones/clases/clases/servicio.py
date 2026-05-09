# clases/servicio.py
from abc import ABC, abstractmethod
from excepciones.excepciones_personalizadas import ServicioError, ServicioNoDisponibleError

class Servicio(ABC):
    """Clase abstracta que representa un servicio de Software FJ"""
    
    def __init__(self, servicio_id: int, nombre: str, precio_base: float):
        self._servicio_id = servicio_id
        self._nombre = nombre
        self._precio_base = precio_base
        self._disponible = True

    @abstractmethod
    def calcular_costo(self, duracion: float = None) -> float:
        """Método abstracto que deben implementar las clases hijas"""
        pass

    def describir(self) -> str:
        """Descripción base del servicio"""
        return f"Servicio: {self._nombre} - Precio base: ${self._precio_base:,.2f}"

    def esta_disponible(self) -> bool:
        return self._disponible

    def cambiar_disponibilidad(self, estado: bool):
        self._disponible = estado

    @property
    def nombre(self):
        return self._nombre

    @property
    def servicio_id(self):
        return self._servicio_id

    def __str__(self):
        estado = "Disponible" if self._disponible else "No disponible"
        return f"{self._nombre} (ID: {self._servicio_id}) - ${self._precio_base:,.2f} [{estado}]"
