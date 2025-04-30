"""
    Desafío 4: Ajedrez Mágico
"""

def color_casilla(fila, columna):
    if fila%2 == 0:
        if columna%2 == 0:
            print("Negro")
        else:
            print("Blanco")
    else:
        if columna%2 != 0:
            print("Negro")
        else:
            print("Blanco")
    
fila = int(input("Ingrese la fila: "))
columna = int(input("Ingrese la columna: "))

while fila != -1 and columna != 1:
    color_casilla(fila, columna)
    fila = int(input("Ingrese la fila: "))
    columna = int(input("Ingrese la columna: "))

print("Terminando!")