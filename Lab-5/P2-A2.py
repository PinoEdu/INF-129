"""
    Desafío 2: El viaje de dominio interestelar de Reinhardt
"""
import math

def distancia_galactiva(x,y):
    numerador = 2*x**2 + 4*x**4 + 3*x**8
    denominador = y**2
    return round(math.sqrt(numerador/denominador), 3)

coor_x = int(input("Ingresa la coordenada x: "))
coor_y = int(input("Ingresa la coordenada y: "))

while coor_x != 0 or coor_y != 0:
    print("La distancia galáctica es:", distancia_galactiva(coor_x, coor_y))
    coor_x = int(input("Ingresa la coordenada x: "))
    coor_y = int(input("Ingresa la coordenada y: "))
print("¡Éxito en sus viajes!")