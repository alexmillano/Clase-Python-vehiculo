from clases.vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca, aceleracion, color, velocidad):
        super().__init__(marca, aceleracion, color, velocidad)

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Aceleración: {self.aceleracion}, Ruedas: {self.ruedas}")

    def get_marca(self):
        return self.marca

    def get_aceleracion(self):
        return self.aceleracion

    def get_color(self):
        return self.color

    def get_velocidad(self):
        return self.velocidad

    def get_ruedas(self):
        return self.ruedas

    def set_marca(self, marca):
        self.marca = marca

    def set_aceleracion(self, aceleracion):
        self.aceleracion = aceleracion

    def set_color(self, color):
        self.color = color

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def set_ruedas(self, ruedas):
        self.ruedas = ruedas

    def Datos(self):
        print(f"El modelo del auto es: {self.get_modelo()}")
        print(f"Ruedas: {self.get_ruedas()}")