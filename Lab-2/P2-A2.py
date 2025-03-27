"""
    Actividad 2: Usando Condicionales 
    
    1. Escribe un programa que pida dos números e imprima cuál es mayor.
"""

x = int(input("Ingresa el primer número: "))
y = int(input("Ingresa el segundo número: "))

if x > y:
    print("El primero número es mayor que el segundo número")
elif x < y:
    print("El segundo número es mayor que el primer número")
else:
    print("Ambos números son iguales")

"""
    2. Escribe un programa que genere un número aleatorio entre 1 y 100.
    Si es par, debe imrpimir "Es par", y si es impar, "Es impar".
"""

from random import randint

numero = randint(1, 100)

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

"""
    3. Juego de adivinar un número

    Escribe un programa que:

    - Genere un número aleatorio entre 1 y 10 y permita que el usuario
    intente adivinarlo ingresando un número.
    - Si el usuario adivina, debe imprimir "¡Correcto!", y si no, "Intenta de nuevo".
"""

numero_secreto = randint(1, 10)
numero_usuario = int(input("Adivina el número secreto (entre 1 y 10): "))

if numero_secreto == numero_usuario:
    print("¡Correcto!")
else:
    print("Intenta de nuevo")

"""
    4. Calculadora de descuentos

    Escribe un programa que pida el precio de un producto en pesos,
    y luego calcule su descuento según las siguientes reglas:

    - Si cuesta más de **$100.000**, aplica 20% de descuento.
    - Si cuesta entre **$50.000 y $100.000**, aplica 10%.
    - Si cuesta menos de **$50.000**, no hay descuento.

    Al final, debe mostrar el monto total de descontado, y el precio final
    del producto. Ambos valores deben estar **redondeados**.
"""

precio = int(input("Ingresa el precio del producto: "))

if precio > 100000:
    descuento_porcentaje = 0.20
elif precio >= 50000 and precio <= 100000:
    descuento_porcentaje = 0.10
else:
    descuento_porcentaje = 0

descuento = round(precio * descuento_porcentaje)
print("Descuento aplicado:", round(descuento))

precio_final = round(precio - descuento)
print("Precio final:", precio_final)

"""
    5. Clasificador de Sismos

    Escribe un programa que permita clasificar un sismo ingresado
    por tu jefe según la escala de Richter, para salvar tu puesto
    de trabajo. Guíate con los siguientes ejemplos de ejecución:
"""

grado = float(input("Ingrese el grado: "))

if 0.0 < grado and grado < 2.0:
    print("Micro")
elif 2.0 <= grado and grado < 4.0:
    print("Menor")
elif 4.0 <= grado and grado < 5.0:
    print("Ligero")
elif 5.0 <= grado and grado < 6.0:
    print("Moderado")
elif 6.0 <= grado and grado < 7.0:
    print("Fuerte")
elif 7.0 <= grado and grado < 8.0:
    print("Mayor")
elif 8.0 <= grado and grado < 10.0:
    print("Épico")
elif grado >= 10.0:
    print("Legendario")
else:
    print("Grado invalido")