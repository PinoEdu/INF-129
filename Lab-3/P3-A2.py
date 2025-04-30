"""
    Desafío 2: Clasificador de Ballenas
"""

num_ballenas_analizar = int(input("Cuantas ballenas quieres analizar? "))
num_ballenas_analizadas = 0

while num_ballenas_analizar > num_ballenas_analizadas:
    tamanio = int(input("Ingresa el tamaño de la ballena: "))

    if tamanio < 14:
        print("Es una ballena rorcual sol")
    elif tamanio <= 20:
        print("Es una ballena franca austral")
    elif tamanio <= 24:
        print("Es una ballena de aleta")
    elif tamanio <= 30:
        print("Es una ballena azul")

    num_ballenas_analizadas += 1

print("Fin de programa creado para J.C.Bodoque")