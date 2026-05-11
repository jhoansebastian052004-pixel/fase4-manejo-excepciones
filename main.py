# main.py
from clases.cliente import Cliente
from clases.servicios_especificos import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from clases.reserva import Reserva
from excepciones.excepciones_personalizadas import *
import datetime

# Lista para almacenar los objetos
clientes = []
servicios = []
reservas = []

def registrar_log(mensaje: str):
    """Registra errores y eventos en un archivo de logs"""
    with open("logs/errores.log", "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {mensaje}\n")

def menu_principal():
    print("\n" + "="*60)
    print("   SISTEMA DE GESTIÓN SOFTWARE FJ - FASE 4")
    print("="*60)
    print("1. Registrar Cliente")
    print("2. Crear Servicios")
    print("3. Realizar Reserva")
    print("4. Cancelar Reserva")
    print("5. Mostrar Información")
    print("6. Pruebas con Errores (Demostración)")
    print("0. Salir")
    print("="*60)

def main():
    print("🚀 Iniciando Sistema de Gestión Software FJ...\n")
    
    # Crear algunos servicios iniciales
    servicios.append(ReservaSala(1, "Sala de Reuniones", 45000, 8))
    servicios.append(AlquilerEquipo(2, "Laptop Dell", 85000, "Laptop Gaming"))
    servicios.append(AsesoriaEspecializada(3, "Asesoría Python", 120000, "Juan Experto"))

    while True:
        menu_principal()
        try:
            opcion = int(input("\nSeleccione una opción: "))
            
            if opcion == 1:  # Registrar Cliente
                try:
                    cid = len(clientes) + 1
                    nombre = input("Nombre completo: ")
                    email = input("Email: ")
                    telefono = input("Teléfono: ")
                    
                    cliente = Cliente(cid, nombre, email, telefono)
                    clientes.append(cliente)
                    print(f"✅ Cliente registrado: {cliente}")
                    registrar_log(f"Cliente registrado: {cliente.nombre}")
                except Exception as e:
                    print(f"❌ Error: {e}")
                    registrar_log(f"ERROR Cliente: {e}")

            elif opcion == 0:
                print("👋 Gracias por usar el sistema. ¡Hasta pronto!")
                break

            # ... (puedo agregar más opciones después)

        except ValueError:
            print("❌ Por favor ingrese un número válido.")
            registrar_log("Error: Entrada no numérica en menú")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            registrar_log(f"ERROR GENERAL: {e}")

    # Pruebas finales de robustez
    print("\n🔍 Realizando pruebas de manejo de excepciones...")
    try:
        # Prueba de error
        cliente_error = Cliente(99, "", "mal@correo", "123")
    except DatosInvalidosError as e:
        print(f"✅ Excepción controlada correctamente: {e}")
        registrar_log(f"Prueba exitosa excepción: {e}")

if __name__ == "__main__":
    main()
