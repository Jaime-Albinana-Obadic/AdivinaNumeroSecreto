from Funcion_Guardar_Estadisticas import registrar
from Funcion_Menu_Dificultad_Intentos import Opcion_valida
from IPython.display import display, HTML
import random
import getpass

def modo_solitario(): # Modo solitario, el número a adivinar se genera aleatoriamente entre 1-1000
    intentos=Opcion_valida(1,4) # Rango de Opcion_valida() de 1 a 4
    numero_a_adivinar = random.randint(1, 1000) # Genera un número aleatorio
    jugar(intentos , numero_a_adivinar , modo="solitario")

def modo_2_jugadores(): # Modo dos jugadores, librería getpass para ocultar visualización de número introducido. Bucle y try/except para asegurar que se introduce un número en rango
    intentos=Opcion_valida(1,4)
    numero_a_adivinar = 0

    while not 1<= numero_a_adivinar <=1000:
        try:
            numero_a_adivinar = int(getpass.getpass("Jugador 1 por favor introduzca un valor entre 1 y 1000: "))
        except ValueError:
            print("Debe introducir un número entre el 1 y el 1000.")                        
    jugar(intentos , numero_a_adivinar , modo="2 jugadores")

def jugar(intentos , numero_a_adivinar , modo): # Función compartida por ambos modos de juego. Mensaje de advertencia al introducir string, pero no al introducir número fuera de rango.
    for i in range(1, intentos+1): # Dejará introducir intentos en función del valor dado a la variable intentos
        prueba= None
        try:
            prueba=int(input("Introduzca su número: "))
        except ValueError:
            display(HTML('<span style="color:red; font-weight:bold;"><br>Debe introducir un número entre el 1 y el 1000.</span>'))
            continue
            
        if prueba == numero_a_adivinar: 
            mensaje_victoria= f"¡Enhorabuena! Ha adivinado el número en {i} intentos.\n" # f'string para mostrar mensajes con variables incluidas
            display(HTML(f'<span style="color:green;font-size:16px; font-weight:bold;"><br>{mensaje_victoria}</span>')) 
            registrar(modo, "Ganada") # Guardar los datos de la partida
            return
        elif prueba > numero_a_adivinar:
            print("El número secreto es menor.\n")
        elif prueba < numero_a_adivinar:
            print("El número secreto es mayor.\n")
            
    mensaje_derrota= f"Lo siento ha perdido. El número secreto era {numero_a_adivinar}."
    display(HTML(f'<span style="font-size:16px; font-weight:bold;">{mensaje_derrota}</span>'))
    registrar(modo, "Perdida") # Guardar los datos de la partida