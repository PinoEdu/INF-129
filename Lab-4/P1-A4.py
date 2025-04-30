""" 
    Actividad 4: Métodos upper() y lower()

    1. ¿Qué imprime?

    nombre = "Juan"
    print(nombre.upper())

    R: Imprime 'JUAN'

    2. ¿Qué imprime?

    grito = "AHHH"
    print(grito.lower())

    R: Imprime 'ahhh'

    3. ¿Cuál es el resultado de este código?

    saludo = "hola"
    print(saludo.upper() + " AMIGOS")

    R: Imprime 'HOLA AMIGOS'

    4. Identificador codificado:

    Un estudiante quiere generar un "identificador" con las 3 primeras letras de su nombre en mayúsculas, 
    seguidas de su edad repetida dos veces. Completa el siguiente programa para que haga lo solicitado:
"""

nombre = "Camila"
edad = "19"
print(nombre[:3].upper() + edad*2)


"""
    5. ¿Está en el saludo?:
    
    Escribe un programa que diga si la palabra "hola" está dentro de un mensaje, 
    sin importar si está en mayúsculas o minúsculas.
"""

mensaje = "¡HOLA AMIGOS!"
print('hola' in mensaje.upper() or 'hola' in mensaje.lower())

"""
    6. Mensaje cifrado simple:
    
    Completa el siguiente programa que contiene un mensaje, y debe devolver solo las letras 
    del medio (sin la primera ni la última), todo en mayúsculas.
"""

mensaje = "secreto"
print(mensaje[1:-1].upper())

"""
    7. Generador de contraseñas:

    Escribe un programa que reciba una palabra clave y:

    1. Le agregue tres * al inicio y final.
    2. La convierta a mayúsculas.
    3. Imprima su longitud final.

    Por ejemplo, si el usuario ingresa la palabra `"secreto”`, el programa debe imprimir:
"""

contrasena = input("Ingrese una palabra: ")
contrasena = "***" + contrasena + "***"
print("La contraseña es:", contrasena)
contador = 0
for caracter in contrasena:
    contador += 1
print("La longitud de la contraseña es", contador)


"""
    7. Primera y última letra:
    
    Escribe un programa que reciba un string y diga si su primera y 
    última letra son iguales (sin importar si son mayúsculas o minúsculas).
"""

palabra = input("Ingresa una palabra: ")
if palabra[0].lower() == palabra[-1].lower():
    print("La primera y última letra son iguales")
else:
    print("La primera y última letra son diferentes")