from ejercicio1 import Automovil, AutomovilVolador

def main():
    automovil1 = Automovil('Toyota',7.5,'Negro',250)
    automovil1.mostrar_info()

    automovil_volador = AutomovilVolador('Tesla', 9.0, 'Rojo', 300)
    automovil_volador.mostrar_info()
    automovil_volador.conducir()
    automovil_volador.vuela()
    automovil_volador.aterriza()

if __name__ == "__main__":
    main()
