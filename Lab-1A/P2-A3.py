"""
    Actividad 3: Conversión de Tipos de Datos

    1. Ejecuta el siguiente código y analiza qué ocurre:
"""

a = "15"
print(int(a))       # Convierte de string a entero

b = 567.98
print(str(b))       # Convierte de float a string

c = "34.98"
print(float(c))     # Convierte de string a float

d = 456.6763
print(int(d))       # Convierte de float a entero, teniendo que truncar el número


"""
    a. ¿Qué sucede cuando convertimos un string a un entero con int(a)?

    R:  Pueden ocurrir dos cosas, que el string que tratemos de converte no sea un entero,
    generando un error, o caso contrario, si sea un número entero, haciendo que se puedan
    aplicar operaciones a la variable 'a'.

    b. ¿Por qué la conversión de d = 456.6763 a un entero con int(d) pierde la parte 
    decimal? ¿Está aproximando el número al entero más cercano, o lo está truncando?

    R: Debido a que los enteros no consideran los números decimales, por lo que
    la función int(d) trunca el número para solo quedarse con la parte entera.

    c. ¿Qué ocurriría si intentamos convertir una cadena con letras o caracteres 
    especiales a un tipo numérico (por ejemplo, int("abc"))?

    R: Ocurriría un error, ya que los caracteres 'abc' no son aceptados dentro del sistema
    númerico en base 10.

    2. Analiza el siguiente código antes de ejecutarlo: ¿los valores de las variables 
    resultado1 y resultado2 serán iguales o diferentes? ¿por qué?
"""

numero1 = 14.56
numero2 = 6.9
resultado1 = int(numero1 * numero2)
print(resultado1)
resultado2 = int(numero1) * int(numero2)
print(resultado2)

"""
    R: Los valores serán distintos, ya que primero operamos sobre los valores con decimales
    y luego truncamos, caso contrario ocurre con resultado2, ya que primero truncamos ambos
    números y luego multiplicamos.

    3. Modifica el siguiente código para que el programa funcione y el resultado calculado en
    total se trunque:
"""

precio_unitario = "15.5"
cantidad = "10"
total = int(float(precio_unitario) * int(cantidad))
print("Total de la compra:", total)