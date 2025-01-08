def Opcion_valida(minimo,maximo):
    print("1. Fácil (20 intentos)\n2. Medio (12 intentos)\n3. Difícil (5 intentos)")
    opcion=0
    while opcion<minimo or opcion>maximo:
        try:
            opcion=int(input(f"Seleccione nivel de dificultad entre {minimo} y {maximo}: "))
        except ValueError:
            print(f"Debe introducir un número del {minimo} al {maximo} para seleccionar la dificultad.")

    intentos=0
    if opcion == 1:
        intentos=20
    elif opcion == 2:
        intentos=12
    elif opcion == 3:
        intentos=5
    print(f"Ha seleccionado la opción {opcion} con {intentos} intentos.")
    return intentos