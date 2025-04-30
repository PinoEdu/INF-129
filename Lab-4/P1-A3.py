"""
    Actividad 3: Operaciones y funciones comunes sobre strings

    1. ¿Qué imprime el siguiente código?

    texto = "Hola"
    resultado = texto * 2
    print(resultado)

    R: Imprimirá 'HolaHola'

    2. ¿Qué imprime?

    nombre = "Ana"
    print("n" in nombre)

    R: Imprimirá 'True'

    3. Completa el código para que imprima la cantidad de caracteres del string:

    mensaje = "Hola mundo"
"""

mensaje = "Hola mundo"
contador = 0
for letra in mensaje:
    contador += 1
print("La cantidad de caracteres que tiene el string es de", contador)


"""
    4. Crea un programa que reciba un string ingresado por el usuario, y luego:

    - Si el string contiene la palabra “ito” o “ita” debe imprimir el mensaje “Es una palabra chiquitita”.
    - En caso contrario, debe imprimir “Es una palabra grande”.
"""

palabra = input("Ingrese una palabra: ")
if 'ito' in palabra or 'ita' in palabra:
    print("Es una palabra chiquita")
else:
    print("Es una palabra grande")


