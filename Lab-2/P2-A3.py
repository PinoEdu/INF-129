"""
    Actividad 3: Condicionales Anidados

    1. Escribe un programa que le permita al usuario ingresar su edad, y si tiene
    licencia de conducir, y vea si tiene o no permisos para manejar siguiendo estas reglas:

    - Si la edad es menor a 13, imprimir "Eres un niño".
    - Si está entre 13 y 17, imprimir "Eres un adolescente".
    - Si la edad es 18 o más:
        - Si tiene licencia, imprimir "Eres adulto y puedes conducir".
        - Si no tiene licencia, imprimir "Eres adulto, pero no puedes conducir".
"""

edad = int(input("Ingresa tu edad: "))

if edad < 13:
    print("Eres un niño")
elif 13 <= edad <= 17:
    print("Eres un adolescente")
elif edad >= 18:
    tiene_licencia = input("¿Tienes licencia de conducir? (s/n): ")
    if tiene_licencia == "s":
        print("Eres adulto y puedes conducir")
    else:
        print("Eres adulto, pero no puedes conducir")