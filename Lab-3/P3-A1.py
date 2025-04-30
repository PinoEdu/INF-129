"""
    Desafío 1: Rayo que distingue entre los humanos y el pan integral
"""

aparaciones_T_G = 0
aparaciones_A_C = 0

base = input("Ingrese la base: ")

while base != "X":
    if base == "T" or base == "G":
        aparaciones_T_G += 1
    elif base == "A" or base == "C":
        aparaciones_A_C += 1
    else:
        print("La base ingresada es inválida")
    
    base = input("Ingrese la base: ")

if aparaciones_T_G > aparaciones_A_C:
    print("Resultado: el objeto analizado es un pan integral.")
elif aparaciones_A_C == aparaciones_T_G:
    print("Resultado: no tenemos idea de qué es el objeto analizado.")
else:
    print("Resultado: el objeto analizado es un humano.")