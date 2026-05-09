# excepciones/excepciones_personalizadas.py

class ErrorSistema(Exception):
    """Excepción base para el sistema"""
    pass


class ClienteError(ErrorSistema):
    """Excepciones relacionadas con clientes"""
    pass


class ServicioError(ErrorSistema):
    """Excepciones relacionadas con servicios"""
    pass


class ReservaError(ErrorSistema):
    """Excepciones relacionadas con reservas"""
    pass


class DatosInvalidosError(ClienteError):
    """Cuando los datos ingresados no son válidos"""
    def __init__(self, mensaje="Datos inválidos proporcionados"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class ClienteNoEncontradoError(ClienteError):
    """Cuando se busca un cliente que no existe"""
    def __init__(self, cliente_id):
        self.mensaje = f"No se encontró el cliente con ID: {cliente_id}"
        super().__init__(self.mensaje)


class ServicioNoDisponibleError(ServicioError):
    """Cuando un servicio no está disponible"""
    def __init__(self, nombre_servicio):
        self.mensaje = f"El servicio '{nombre_servicio}' no está disponible."
        super().__init__(self.mensaje)


class ReservaInvalidaError(ReservaError):
    """Cuando una reserva no cumple con las condiciones"""
    def __init__(self, mensaje="La reserva no es válida"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class SaldoInsuficienteError(ReservaError):
    """Cuando el cliente no tiene suficiente saldo o crédito"""
    pass
