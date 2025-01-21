from IPython.display import display, HTML

def Opcion_valida(minimo,maximo): # En el módulo Funcion_Modos_de_Juego.py se definen el mínimo y máximo de Opcion_valida()
    display(HTML('<span style="font-size:16px; font-weight:bold;"><br>Dificultad:</span>'))
    print("\n1. Fácil (20 intentos)\n2. Medio (12 intentos)\n3. Difícil (5 intentos)\n4. Dificultad personalizada\n")
    opcion=0
    while opcion<minimo or opcion>maximo: # Bucle hasta que se introduzca un número válido
        try:
            opcion=int(input(f"\nSeleccione modo de dificultad entre {minimo} y {maximo}: "))
        except ValueError:
            error_str=f"Debe introducir un número del {minimo} al {maximo} para seleccionar la dificultad."
            display(HTML(f'<span style="font-weight:bold;"><br>{error_str}</span>'))

    intentos=0 # En función de la opción elegida la variable intentos tomará otro valor
    if opcion == 1:
        intentos=20
    elif opcion == 2:
        intentos=12
    elif opcion == 3:
        intentos=5
    elif opcion == 4: # Permite al jugador introducir el número de intentos que desee
        funcionamiento_opcion_4=True
        while funcionamiento_opcion_4: # Bucle hasta que se introduzca un número válido
            try:
                intentos= int(input("Introduzca el número de intentos con el que quiera jugar: "))
                if intentos <= 0:
                    print("Debe seleccionar un número positivo mayor a 0.\n")
                    continue
                funcionamiento_opcion_4=False
            except ValueError: # No se introduzca un integer y como está dentro del bucle, vuelve a pedir que se introduzca un número válido
                error_str_intentos="Debe introducir el número de intentos que desea tener."
                display(HTML(f'<span style="font-weight:bold;"><br>{error_str_intentos}</span>'))
    print(f"\nHa seleccionado la opción {opcion} con {intentos} intentos.\n")
    return intentos # Permite usar la variable actualizada de intentos