class Vehiculo:
    def __init__(self, marca, aceleracion, color, velocidad):
        self.marca = marca
        self.aceleracion = aceleracion
        self.color = color
        self.velocidad = velocidad
        self.ruedas = 4
        self.anio = 'protegido'
        self.modelo = 'privado'

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

    def get_anio(self):
        return self.anio

    def get_modelo(self):
        return self.modelo

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

    def set_anio(self, anio):
        self.anio = anio

    def set_modelo(self, modelo):
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Aceleración: {self.aceleracion}, Ruedas: {self.ruedas}, Anio: {self.anio}, Modelo: {self.modelo}")
