"""
    1. Analiza el siguiente código y responde:

    numero = int(input("Ingresa un número: "))
    cuadrado = numero ** 2
    print("El cuadrado de ", numero, " es ", cuadrado)

    a. ¿Qué ocurre si ingresas un número decimal? Ejecuta el código y verifica.

    El programa lanzará un error, ya que la función int() intenta convertir una
    cadena (string) en un número entero (int). Sin embargo, si se ingresa un
    número decimal, este contiene un punto (.), lo que hace que la conversión
    falle debido a la presencia de caracteres no numéricos.

    b. Modifica el programa para aceptar números decimales (float) en lugar de enteros.
    ¿Qué ocurre ahora si ingresas un número decimal? ¿y si ingresas un entero?
"""

# Codigo corregido
numero = float(input("Ingresa un número: "))    # Cambiamos el tipo de casteo
cuadrado = numero ** 2
print("El cuadrado de ", numero, " es ", cuadrado)

"""
    Ahora el código funciona tanto para números enteros (int) como para números decimales (float).
    Esto es porque float() convierte directamente el input en un número de punto flotante.
    Si se ingresa un número entero, este se representará con punto decimal, por ejemplo:

    (string) '5' -> (int) 5 -> (float) 5.0
"""


"""
    2. Analiza el siguiente código y responde:

    base = input("Ingresa la base del triángulo: ")
    altura = input("Ingresa la altura: ")
    area = base * altura / 2
    print("El área es:", area)

    a. Si se ejecuta el código, ¿qué ocurrirá?

    El programa no funcionará, ya que en la tercera línea se intentará realizar cálculos
    con valores de tipo string, lo que generará un error.

    area = string * string / 2

    b. Copia y pega el código, y ejecútalo para ver si se cumple tu predicción o no. 
    
    c. Arregla el código para que funcione correctamente. 
"""

# Codigo corregido
base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura: "))
area = base * altura / 2
print("El área es:", area)