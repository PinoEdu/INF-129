"""
    1. Corrige este ciclo para que se detenga cuando n llegue a 5:
"""

n = 1
while n <= 5:
    print(n)
    n += 1

"""
    2. Analiza el siguiente código:
"""

respuesta = "sí"
while respuesta == "sí":
    print("Sigues en el bucle...")

"""
    a. ¿Qué ocurre si se ejecuta?

    R: Caerá en un bucle infinito, debido a que respuesta siempre será igual a 'sí'.

    b. Corrige este ciclo para que termine cuando el usuario ingrese "no":
"""

respuesta = "sí"
while respuesta == "sí":
    respuesta = str(input("Debesa continuar en el ciclo (sí/no): "))