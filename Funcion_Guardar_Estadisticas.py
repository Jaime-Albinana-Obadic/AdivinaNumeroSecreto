import openpyxl

def registrar(modo,resultado):
    excel=openpyxl.load_workbook("C:\\Users\\Obadic\\Tabla_partidas.xlsx")
    hoja_excel=excel["Sheet1"]
    nombre=input("Nombre del jugador: ")
    datos_partida=[nombre,modo,resultado]
    hoja_excel.append(datos_partida)
    excel.save("C:\\Users\\Obadic\\Tabla_partidas.xlsx")

def mostrar_resultados():
    excel=openpyxl.load_workbook("C:\\Users\\Obadic\\Tabla_partidas.xlsx")
    hoja_excel=excel["Sheet1"]
    for fila in hoja_excel:
        for celda in fila:
            print(celda.value + " ", end="")
        print()