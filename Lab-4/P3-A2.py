"""
    Desafío 2: Telégrafo
"""

letras = "qwertyuioplkjhgfdsazxcvbnm"
caract_especiales = "ñáéíóú!#$%&/()=?¡!¨*][:_;/*-+.,-´¿']"
numeros = "0123456789"

mensaje = input("Ingrese su mensaje: ")
costo = 0

for letra in mensaje:
    letra = letra.lower()
    if letra in letras:
        costo += 10
    elif letra in caract_especiales:
        costo += 30
    elif letra in numeros:
        costo += 20
    elif letra == " ":
        costo += 0

print("El costo de su mensaje es $", costo)