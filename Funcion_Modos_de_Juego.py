from Funcion_Guardar_Estadisticas import registrar
from Funcion_Menu_Dificultad_Intentos import Opcion_valida
import random

def modo_solitario():
    intentos=Opcion_valida(1,3)
    numero_a_adivinar = random.randint(1, 1000)
    jugar(intentos , numero_a_adivinar , modo="solitario")

def modo_2_jugadores():
    intentos=Opcion_valida(1,3)
    numero_a_adivinar = 0

    while not 1<= numero_a_adivinar <=1000:
        try:
            numero_a_adivinar = int(input("Jugador 1 por favor introduzca un valor entre 1 y 1000: "))
        except ValueError:
            print("Debe introducir un número entre el 1 y el 1000.")                        
    jugar(intentos , numero_a_adivinar , modo="2 jugadores")

def jugar(intentos , numero_a_adivinar , modo):
    for i in range(1, intentos+1):
        try:
            prueba=int(input("Introduzca su número: "))
        except ValueError:
            print("Debe introducir un número entre el 1 y el 1000.")
        if prueba == numero_a_adivinar:
            print(f"¡Enhorabuena! Ha adivinado el número en {i}.")
            registrar(modo, "Ganada")
            return
        elif prueba > numero_a_adivinar:
            print("El número secreto es menor.")
        elif prueba < numero_a_adivinar:
            print("El número secreto es mayor.")
            
    print(f"Lo siento ha perdido. El número secreto era {numero_a_adivinar}")
    registrar(modo, "Perdida")