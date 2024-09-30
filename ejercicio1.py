from abc import ABC, abstractmethod

class Automovil:
    def __init__(self, marca, aceleracion, color, velocidad):
        self.marca = marca
        self.aceleracion = aceleracion
        self.color = color
        self.velocidad = velocidad
        self.ruedas = 4


    def mostrar_info(self):
        print(f"Marca: {self.marca}, Aceleración: {self.aceleracion}, Ruedas: {self.ruedas}")

    @abstractmethod
    def conducir(self):
        pass



class AutomovilVolador(Automovil):
    def __init__(self, marca, aceleracion, color, velocidad):
        super(). __init__(marca, aceleracion, color, velocidad)
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
