from clases.vehiculo import Vehiculo
from clases.automovil import Automovil
from clases.automovilvolador import AutomovilVolador
from base_datos.conexion import Conexion

#def main():
    #automovil1 = Automovil('Toyota',7.5,'Negro',250)
    #automovil1.mostrar_info()

    #automovil_volador = AutomovilVolador('Tesla', 9.0, 'Rojo', 300)
    #automovil_volador.mostrar_info()
    #automovil_volador.conducir()
    #automovil_volador.vuela()
    #automovil_volador.aterriza()

#if __name__ == "__main__":
    #main()

#def main():
    #automovil1 = Automovil('Toyota', 7.5, 'Negro', 250)
    
    #print("Marca:", automovil1.get_marca())
    #print("Aceleración:", automovil1.get_aceleracion())
    #print("Color:", automovil1.get_color())
    #print("Velocidad:", automovil1.get_velocidad())
    #print("Ruedas:", automovil1.get_ruedas())
    
    #print("Año:", automovil1.get_anio())
    #print("Modelo:", automovil1.get_modelo())
    
    #automovil1.set_anio(2024)
    #automovil1.set_modelo("Corolla")
    
    #print("\n--- Atributos modificados ---")
    #print("Año:", automovil1.get_anio())
    #print("Modelo:", automovil1.get_modelo())

    #automovil1.Datos()


def main():
    db = Conexion('base_datos/mi_bd.db')
    db.crear('Toyota', 7.5, 'Negro', 250, 4, '2024', 'Corolla')
    vehiculos = db.listar()
    for vehiculo in vehiculos:
        print(vehiculo)

    db.modificar(1, marca='Honda', color='Rojo')

    vehiculos_modificados = db.listar()
    for vehiculo in vehiculos_modificados:
        print(vehiculo)

    db.eliminar(1)

    vehiculos_despues_eliminacion = db.listar()
    for vehiculo in vehiculos_despues_eliminacion:
        print(vehiculo)

    db.cerrar_conexion()

if __name__ == "__main__":
    main()