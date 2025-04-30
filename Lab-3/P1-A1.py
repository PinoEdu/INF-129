"""
    1. ¿Qué imprimirá este código en la consola? Responde, y luego copia y pega el código, y ejecútalo, para ver si acertaste o no. 

    R: El código printeará por consolas tres líneas con la palabra 'Hola'
"""

contador = 1
while contador <= 3:
    print("Hola")
    contador += 1

"""
    2. ¿Cuántas veces se ejecuta el siguiente ciclo? ¿Por qué?

    R: Se ejecutará 4 veces el ciclo, debido a que el contador va aumentando de 2 en 2, y la condición es que n sea menor a 8.
    En la primera instancia n = 0, segunda instancia n = 2, tercera instancia n = 4, cuarta instancia n = 6, y cuando n = 8, ya no se volverá a ejecutar,
    ya que n será igual a 8 y debe ser menor a 8 para que se vuelva a ejecutar.
"""

n = 0
while n < 8:
    print("Python")
    n += 2

"""
    3. ¿Qué pasará si ejecutamos este código?

        a. ¿Por qué no imprime el número 10?

    R: Se ejecutará solo 3 veces.
    Primera instancia x = 1,
    Segunda instancia x = 4,
    Tercera instancia x = 7,
    "Cuarta instancia" x = 10, haciendo que no se ejecute el cuerpo del while, ya que x debe ser distinto de 10.
"""

x = 1
while x != 10:
    print(x)
    x += 3

"""
    4. Analiza qué hace el siguiente código:

    R: Cuenta la cantidad de números positivos que se ingresan.
"""

contador = 0
contador_numeros_positivos = 0
num = int(input("Ingresa un número: "))

while num >= 0:
    contador += 1
    contador_numeros_positivos += num
    num = int(input("Ingresa otro número: "))

print("Ingresaste", contador, "números positivos, donde su suma es de", contador_numeros_positivos)

"""
    5. Completa el código para contar cuántos números entre 1 y 20 son múltiplos de 3.
"""

contador = 0
n = 1
while n <= 20:
    if n%3 == 0:      # (Completa la condición)
        contador += 1
    n += 1
print("Cantidad de múltiplos de 3:", contador)

"""
    6. Completa el siguiente código para que el jugador intente adivinar un número secreto.
    El ciclo debe continuar hasta que el jugador adivine correctamente.
"""

import random
numero_secreto = random.randint(1, 10)
intento = 0

while intento != numero_secreto:  # Completa la condición para que el ciclo termine cuando adivine
    intento = int(input("Adivina el número (1-10): "))

    if intento == numero_secreto:  # Completa la comparación
        print("¡Correcto! Has adivinado.")
    elif intento < numero_secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")

"""
    Analiza:

    a. ¿Por qué la variable `intento` se inicializa en 0?
    
    R: Se inicializa en 0 para tener un valor con cual iniciar el ciclo while,
    ya que en un comienzo intento siempre será distinto que numero_secreto, esto se debe a que
    randint nos dará un número entero en el rango [1, 10], por lo que 0 no pertenece a este rango.

    b. ¿Hubiese servido cualquier otro valor inicial?

    R: Mientras no pertenezca al rango [1, 10], no habría problema.

    c. ¿Que pasaría si en vez de darle un valor inicial a la variable `intento`, 
    le preguntáramos de inmediato al usuario una opción? ¿Habría que cambiar el resto del programa?

    R: Habría que modificar levemente el código, ya que puede caer en el caso que en un comienzo
    ingresemos un número y sea igual al numero_secreto, por lo que no se ejecutará el cuerpo del while,
    haciendo que no se printee nada por consola.
"""

"""
    7. Trabajas en el Registro Civil y tienes que verificar las edades de varias personas para determinar
    si son mayores de edad y pueden acceder a ciertos servicios. Tu jefe te indica al inicio del día la
    cantidad de personas que se atenderán hoy, y debes verificar cada edad ingresada para clasificar 
    si la persona es mayor o menor de edad.

    a. Escribe un programa que reciba la cantidad de personas que atenderás ese día, y por cada
    una pida ingresar la edad e indique si es mayor o menor de edad. Guíate con los siguentes 
    ejemplos de ejecución:
"""

personas_atendidas = 0
cantidad_personas = int(input("Ingrese la cantidad de personas: "))

while personas_atendidas < cantidad_personas:
    edad = int(input("Ingrese la edad de la persona: "))

    if edad < 18:
        print("Es menor de edad.")
    else:
        print("Es mayor de edad")
    
    personas_atendidas += 1

"""
    b. Modifica tu programa para que cuente cuántas personas fueron mayor de edad, 
    y al final muestre un mensaje con esa suma. Guíate por el siguiente ejemplo:
"""

personas_atendidas = 0
cantidad_personas = int(input("Ingrese la cantidad de personas: "))
cantidad_mayores_edad = 0

while personas_atendidas < cantidad_personas:
    edad = int(input("Ingrese la edad de la persona: "))

    if edad < 18:
        print("Es menor de edad.")
    else:
        cantidad_mayores_edad += 1
        print("Es mayor de edad")
    
    personas_atendidas += 1

print("El número de mayores de dad es:", cantidad_mayores_edad)

"""
    c. ¿Qué ocurre con tu programa si el usuario ingresa como cantidad de personas 
    inicial un número menor o igual a 0? 

    R: Se solicitarán más edades de las que se tiene prevista.

    d. Modifica tu programa para que, si el usuario ingresa un número inválido de personas,
    muestre un mensaje de error. Guíate por el siguiente ejemplo:
"""

personas_atendidas = 0
cantidad_personas = int(input("Ingrese la cantidad de personas: "))
cantidad_mayores_edad = 0

if cantidad_personas > 0:
    while personas_atendidas < cantidad_personas:
        edad = int(input("Ingrese la edad de la persona: "))

        if edad < 18:
            print("Es menor de edad.")
        else:
            cantidad_mayores_edad += 1
            print("Es mayor de edad")

        personas_atendidas += 1
else:
    print("ERROR: número de personas inválido")