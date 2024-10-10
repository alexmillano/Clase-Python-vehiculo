from clases.vehiculo import Vehiculo

class AutomovilVolador(Vehiculo):
    def __init__(self, marca, aceleracion, color, velocidad):
        super().__init__(marca, aceleracion, color, velocidad)
        self.ruedas = 6
        self.esta_volando = False


    def vuela(self):
        if self.esta_volando == False:
            print("El automóvil está volando")
            self.esta_volando = True
        else:
            print("El automóvil ya está en vuelo")

    def aterriza(self):
        if self.esta_volando:
            print("El automóvil ha aterrizado")
            self.esta_volando = False
        else:
            print("El automóvil ya está en tierra")

    def conducir(self):
        print("El automóvil está conduciendo")

    def Datos(self):
        print("El modelo del auto es: ", self.get_marca)
        print("Ruedas: ", self.get_ruedas)