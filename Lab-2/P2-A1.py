"""
    Actividad 1: Experimentando con Condicionales

    1. Completa las siguientes condiciones rellenando el espacio en blanco (_____)
    según se requiera en cada expresión condicional:
"""

edad = int(input("Ingresa la edad "))
if edad >= 18:
    print("Puedes votar")

numero= int(input("Ingresa un número "))
if numero > 0:
    print("El número es positivo")
else:
    print("El número es negativo")

edad = int(input("Ingresa la edad "))
if edad < 18:
    print("Eres menor de edad")
elif edad >= 18 and edad < 60:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")


"""
    2. ¿Qué imprimirá este código si a = 7 y b = 10?
"""

a = 7
b = 10

if a > b:
    print("A es mayor que B")
elif a < b:
    print("A es menor que B")   # a es menor que b
else:
    print("A es igual a B")

"""
    3. Encuentra y corrige el error lógico en este código, para que los mensajes
    de los print se cumplan correctamente:
"""

x = int(input("Ingrese un número: "))

if x > 10 and x < 20:
    print("Entre 10 y 20")
elif x < 10 or x > 20:
    print("Fuera de rango")
else:
    print("Exactamente 10 o 20")