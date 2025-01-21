from Funcion_Modos_de_Juego import modo_solitario, modo_2_jugadores
from Funcion_Guardar_Estadisticas import mostrar_resultados
from IPython.display import display, HTML

def Menu_Principal_Juego(): # Función del menú principal del juego
    seguir_jugando = True
    while seguir_jugando:
        display(HTML('<span style="font-size:20px; font-weight:bold;">JUEGO ADIVINA NÚMEROS</span>')) # Permite cambiar tamaño, color y formato del mensaje que se muestra
        print('\nMenú principal:\n1. Partida modo solitario\n2. Partida 2 jugadores\n3. Estadísticas\n4. Salir\n') # Con saltos de líneas para evitar llamar a print() repetidas veces

        try:
            opcion=(int(input("Introduzca el número de la opción deseada: ")))
        except ValueError: # Por si se introduce string, float... cuando se espera un integer
            display(HTML('<span style="color:red; font-weight:bold;"><br>Debe introducir un número del 1 al 4, en función de la opción que desee elegir.</span>'))
            continue
        if opcion ==1: # Modo solitario
            modo_solitario()
        elif opcion ==2: # Modo dos jugadores
            modo_2_jugadores()
        elif opcion ==3: # Menú estadísticas
            mostrar_resultados()
        elif opcion ==4: # Cierra el juego al cambiar la condición y salir del bucle. Conduce a else
            seguir_jugando = False
        elif int(opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4): # Evalúa si el número introducido es diferente al número de las opciones dadas.
            display(HTML('<span style="color:red; font-weight:bold;"><br>La opción no es válida, inténtelo de nuevo.</span>'))
            
    else:
        display(HTML('<span style="font-size:16px; font-weight:bold;"><br>Juego cerrado</span>'))