from abc import ABC, abstractmethod
import logging

# Configuración del archivo de logs
logging.basicConfig(
    filename='errores.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# =========================
# EXCEPCIONES PERSONALIZADAS
# =========================

class ErrorReserva(Exception):
    pass

class ErrorServicio(Exception):
    pass

class ErrorCliente(Exception):
    pass


# =========================
# CLASE ABSTRACTA
# =========================

class Servicio(ABC):

    def __init__(self, nombre, tarifa):
        self.nombre = nombre
        self.tarifa = tarifa

    @abstractmethod
    def calcular_costo(self, horas):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# =========================
# SERVICIOS DERIVADOS
# =========================

class ReservaSala(Servicio):

    def calcular_costo(self, horas):
        if horas <= 0:
            raise ErrorServicio("Las horas deben ser mayores a 0")
        return self.tarifa * horas

    def descripcion(self):
        return f"Reserva de sala: {self.nombre}"


class AlquilerEquipo(Servicio):

    def calcular_costo(self, horas):
        if horas <= 0:
            raise ErrorServicio("Tiempo inválido")
        return (self.tarifa * horas) + 20000

    def descripcion(self):
        return f"Alquiler de equipo: {self.nombre}"


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, horas):
        if horas <= 0:
            raise ErrorServicio("Horas inválidas")
        return (self.tarifa * horas) * 1.19

    def descripcion(self):
        return f"Asesoría especializada: {self.nombre}"


# =========================
# CLASE CLIENTE
# =========================

class Cliente:

    def __init__(self, nombre, correo, telefono):

        if len(nombre) < 3:
            raise ErrorCliente("Nombre inválido")

        if "@" not in correo:
            raise ErrorCliente("Correo inválido")

        if len(telefono) < 7:
            raise ErrorCliente("Teléfono inválido")

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    def obtener_nombre(self):
        return self.__nombre

    def obtener_correo(self):
        return self.__correo

    def obtener_telefono(self):
        return self.__telefono


# =========================
# CLASE RESERVA
# =========================

class Reserva:

    def __init__(self, cliente, servicio, horas):

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

    def confirmar(self):

        try:

            costo = self.servicio.calcular_costo(self.horas)

            self.estado = "Confirmada"

            print("\n===== RESERVA CONFIRMADA =====")
            print("Cliente:", self.cliente.obtener_nombre())
            print("Servicio:", self.servicio.descripcion())
            print("Horas:", self.horas)
            print("Costo total:", costo)
            print("Estado:", self.estado)

        except Exception as e:

            logging.error(str(e))
            print("Error al confirmar reserva:", e)

        finally:

            print("Proceso de reserva finalizado.\n")

    def cancelar(self):

        try:

            if self.estado == "Cancelada":
                raise ErrorReserva("La reserva ya está cancelada")

            self.estado = "Cancelada"

            print("Reserva cancelada correctamente")

        except Exception as e:

            logging.error(str(e))
            print("Error:", e)


# =========================
# PRUEBAS DEL SISTEMA
# =========================

print("\n========== SISTEMA SOFTWARE FJ ==========\n")

# Lista de operaciones simuladas
operaciones = []

# Operación 1
try:
    cliente1 = Cliente("Hameth Hernandez", "hameth@gmail.com", "3001234567")
    sala1 = ReservaSala("Sala VIP", 50000)

    reserva1 = Reserva(cliente1, sala1, 3)
    operaciones.append(reserva1)

except Exception as e:
    logging.error(str(e))
    print(e)

# Operación 2
try:
    cliente2 = Cliente("Ana Torres", "ana@gmail.com", "3019876543")
    equipo1 = AlquilerEquipo("Computador Gamer", 40000)

    reserva2 = Reserva(cliente2, equipo1, 2)
    operaciones.append(reserva2)

except Exception as e:
    logging.error(str(e))
    print(e)

# Operación 3
try:
    cliente3 = Cliente("Luis Perez", "luis@gmail.com", "3125554444")
    asesoria1 = AsesoriaEspecializada("Python Avanzado", 70000)

    reserva3 = Reserva(cliente3, asesoria1, 4)
    operaciones.append(reserva3)

except Exception as e:
    logging.error(str(e))
    print(e)

# Operación inválida 4
try:
    cliente4 = Cliente("Jo", "correo_malo", "12")

except Exception as e:
    logging.error(str(e))
    print("Error cliente:", e)

# Operación inválida 5
try:
    sala2 = ReservaSala("Sala Básica", 30000)

    reserva4 = Reserva(cliente1, sala2, -5)
    operaciones.append(reserva4)

except Exception as e:
    logging.error(str(e))
    print("Error reserva:", e)

# Operación inválida 6
try:
    equipo2 = AlquilerEquipo("VideoBeam", 25000)

    reserva5 = Reserva(cliente2, equipo2, 0)
    operaciones.append(reserva5)

except Exception as e:
    logging.error(str(e))
    print("Error:", e)

# Operación 7
try:
    cliente5 = Cliente("Carlos Ruiz", "carlos@gmail.com", "3204445555")
    sala3 = ReservaSala("Sala Empresarial", 80000)

    reserva6 = Reserva(cliente5, sala3, 5)
    operaciones.append(reserva6)

except Exception as e:
    logging.error(str(e))
    print(e)

# Operación 8
try:
    cliente6 = Cliente("Maria Lopez", "maria@gmail.com", "3112223333")
    asesoria2 = AsesoriaEspecializada("Ciberseguridad", 90000)

    reserva7 = Reserva(cliente6, asesoria2, 2)
    operaciones.append(reserva7)

except Exception as e:
    logging.error(str(e))
    print(e)

# Operación 9
try:
    cliente7 = Cliente("Pedro Gomez", "pedro@gmail.com", "3157779999")
    equipo3 = AlquilerEquipo("Impresora 3D", 60000)

    reserva8 = Reserva(cliente7, equipo3, 1)
    operaciones.append(reserva8)

except Exception as e:
    logging.error(str(e))
    print(e)

# Operación inválida 10
try:
    cliente8 = Cliente("", "malcorreo", "1")

except Exception as e:
    logging.error(str(e))
    print("Error final:", e)

# =========================
# EJECUCIÓN DE RESERVAS
# =========================

for reserva in operaciones:

    try:

        reserva.confirmar()

    except Exception as e:

        logging.error(str(e))
        print("Error general:", e)

print("\n========== FIN DEL SISTEMA ==========")
