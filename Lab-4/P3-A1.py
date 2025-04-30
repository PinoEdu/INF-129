"""
    Desafío 1: Durante la época de las clases online
"""

correo = input("Ingrese su correo: ")
i = 0

while i < len(correo) and correo[i] != "@":
    i += 1

if correo[i:] == "@sansano.usm.cl" or correo[i:] == "@usm.cl":
    print("Correo valido!")
else:
    print("Dominio invalido!")