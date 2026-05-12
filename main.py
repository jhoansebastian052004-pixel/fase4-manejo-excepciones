# ========================================================
# SISTEMA DE GESTIÓN SOFTWARE FJ - FASE 4
# Entrega Final - Todo en main.py
# ========================================================

import datetime

# ====================== EXCEPCIONES ======================
class ErrorSistema(Exception):
    pass

class DatosInvalidosError(ErrorSistema):
    def __init__(self, mensaje="Datos inválidos"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ServicioNoDisponibleError(ErrorSistema):
    def __init__(self, nombre):
        self.mensaje = f"El servicio '{nombre}' no está disponible"
        super().__init__(self.mensaje)

# ====================== CLASES ======================
class Cliente:
    def __init__(self, cliente_id, nombre, email, telefono):
        self.cliente_id = cliente_id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.reservas_activas = 0
        self._validar()

    def _validar(self):
        if len(self.nombre.strip()) < 3:
            raise DatosInvalidosError("El nombre debe tener mínimo 3 caracteres")
        if "@" not in self.email:
            raise DatosInvalidosError("Email inválido")

    def __str__(self):
        return f"Cliente[{self.cliente_id}] - {self.nombre} ({self.email})"


class Servicio:
    def __init__(self, servicio_id, nombre, precio_base):
        self.servicio_id = servicio_id
        self.nombre = nombre
        self.precio_base = precio_base
        self.disponible = True

    def calcular_costo(self, duracion=1):
        if not self.disponible:
            raise ServicioNoDisponibleError(self.nombre)
        return round(self.precio_base * duracion, 2)

    def __str__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"{self.nombre} - ${self.precio_base:,.0f} [{estado}]"


# ====================== PROGRAMA PRINCIPAL ======================
clientes = []
servicios = []
reservas = []

def menu():
    print("\n" + "="*60)
    print("   SISTEMA SOFTWARE FJ - FASE 4 (Entrega Final)")
    print("="*60)
    print("1. Registrar Cliente")
    print("2. Mostrar Servicios")
    print("3. Realizar Reserva")
    print("4. Pruebas de Excepciones")
    print("0. Salir")
    print("="*60)

def main():
    print("🚀 Iniciando Sistema...\n")
    
    # Servicios iniciales
    servicios.append(Servicio(1, "Sala de Reuniones", 45000))
    servicios.append(Servicio(2, "Alquiler Laptop", 85000))
    servicios.append(Servicio(3, "Asesoría Python", 120000))

    while True:
        menu()
        try:
            opcion = int(input("\nOpción: "))

            if opcion == 1:
                try:
                    cid = len(clientes) + 1
                    nombre = input("Nombre: ")
                    email = input("Email: ")
                    tel = input("Teléfono: ")
                    c = Cliente(cid, nombre, email, tel)
                    clientes.append(c)
                    print(f"✅ Cliente registrado: {c}\n")
                except Exception as e:
                    print(f"❌ Error: {e}")

            elif opcion == 2:
                print("\nServicios:")
                for s in servicios:
                    print(f"  {s}")

            elif opcion == 4:
                print("\n--- Prueba de Excepciones ---")
                try:
                    Cliente(99, "ab", "mal", "123")
                except Exception as e:
                    print(f"✅ Excepción controlada: {e}")

            elif opcion == 0:
                print("¡Hasta pronto!")
                break
        except:
            print("Ingrese un número válido.")

if __name__ == "__main__":
    main()
