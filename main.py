from abc import ABC, abstractmethod
import logging

# Configuración del archivo de errores
logging.basicConfig(
    filename='errores.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Clase abstracta
class Servicio(ABC):

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# Clase Cliente
class Cliente:

    def __init__(self, nombre, correo):

        if not nombre:
            raise ValueError("Nombre inválido")

        if "@" not in correo:
            raise ValueError("Correo inválido")

        self.__nombre = nombre
        self.__correo = correo

    def mostrar_info(self):
        return f"Cliente: {self.__nombre}"


# Servicio 1
class ReservaSala(Servicio):

    def __init__(self, horas):

        if horas <= 0:
            raise ValueError("Horas inválidas")

        self.horas = horas

    def calcular_costo(self):
        return self.horas * 50000

    def descripcion(self):
        return "Reserva de sala"


# Servicio 2
class AlquilerEquipo(Servicio):

    def __init__(self, dias):

        if dias <= 0:
            raise ValueError("Días inválidos")

        self.dias = dias

    def calcular_costo(self):
        return self.dias * 30000

    def descripcion(self):
        return "Alquiler de equipos"


# Servicio 3
class Asesoria(Servicio):

    def __init__(self, sesiones):

        if sesiones <= 0:
            raise ValueError("Sesiones inválidas")

        self.sesiones = sesiones

    def calcular_costo(self):
        return self.sesiones * 80000

    def descripcion(self):
        return "Asesoría especializada"


# Clase Reserva
class Reserva:

    def __init__(self, cliente, servicio):

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def confirmar(self):

        try:

            costo = self.servicio.calcular_costo()

            self.estado = "Confirmada"

            print("Reserva confirmada")
            print(self.cliente.mostrar_info())
            print("Servicio:", self.servicio.descripcion())
            print("Costo:", costo)

        except Exception as e:

            logging.error(str(e))

            print("Error al confirmar reserva")

        finally:

            print("Proceso finalizado\n")


# Lista de pruebas
try:

    cliente1 = Cliente("Andrea", "andrea@gmail.com")
    servicio1 = ReservaSala(3)
    reserva1 = Reserva(cliente1, servicio1)
    reserva1.confirmar()

    cliente2 = Cliente("Carlos", "carlos@gmail.com")
    servicio2 = AlquilerEquipo(2)
    reserva2 = Reserva(cliente2, servicio2)
    reserva2.confirmar()

    cliente3 = Cliente("María", "maria@gmail.com")
    servicio3 = Asesoria(4)
    reserva3 = Reserva(cliente3, servicio3)
    reserva3.confirmar()

except Exception as e:

    logging.error(str(e))

    print("Error general:", e)
