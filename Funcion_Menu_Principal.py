from Funcion_Modos_de_Juego import modo_solitario, modo_2_jugadores
from Funcion_Guardar_Estadisticas import mostrar_resultados

def Menu_Principal_Juego():
    seguir_jugando = True
    while seguir_jugando:
        print('JUEGO ADIVINA NÚMEROS\nMenú principal:')
        print("1. Partida modo solitario")
        print("2. Partida 2 jugadores")
        print("3. Estadísticas")
        print("4. Salir")

        try:
            opcion=(int(input("Introduzca el número de la opción deseada: ")))
        except ValueError:
            print("Debe introducir un número del 1 al 4, en función de la opción que desee elegir.")
            continue
        if opcion ==1:
            modo_solitario()
        elif opcion ==2:
            modo_2_jugadores()
        elif opcion ==3:
            mostrar_resultados()
        elif opcion ==4:
            seguir_jugando = False
        elif int(opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4):
            print("La opción no es válida, inténtelo de nuevo.")
    else:
        print("Juego cerrado")