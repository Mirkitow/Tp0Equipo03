import Funciones

lst_identificadores = []
lst_montos = []
lst_distancias = []
lst_estados = []
lst_repartidores = []
lst_tiempo_estimado = []
lst_prioridades = []

def main():
    opcion = 0
    
    while opcion != 5:
        opcion = Funciones.menu(1, 5)
        if opcion == 1:
            Funciones.registrar_nuevo_pedido()
        elif opcion == 2:
            Funciones.eliminar_pedido()
        elif opcion == 3:
            Funciones.modificar_estado_o_repartidor()
        elif opcion == 4:
            Funciones.informe_general()
        elif opcion == 5:
            print("Saliendo del programa...")
    
main()
