"""
    Actividad 3: Ejercitemos
    1. Contar vocales:
        a. Completa el código que cuenta cuántas vocales hay en un string utilizando un ciclo `while`:
        b. Escribe el mismo programa, pero esta vez utilizando un ciclo for en vez de un ciclo while. 
        Luego describe con tus palabras qué cambios tuviste que hacer. 
"""

texto = input("Ingresa un texto: ")
i = 0
vocales = 0
while i < len(texto):
    letra = texto[i]
    if letra.lower() in 'aeiou': 
        vocales += 1
    i += 1
print("Hay", vocales, "vocales.")

texto = input("Ingresa un texto: ")
vocales = 0
for letra in texto:
    if letra.lower() in 'aeiou': 
        vocales += 1
print("Hay", vocales, "vocales.")

"""
    2. Analizador de contraseñas

        Crea un programa que reciba una contraseña ingresada por el usuario y diga si es segura. Una contraseña es segura si:

        - Tiene al menos 8 caracteres
        - Contiene una letra mayúscula
        - Contiene al menos un número
"""

contrasena = input("Ingrese una contraseña: ")
letras = "QWERTYUIOPASDFGHJKLÑZXCVBNM"
numeros = "1234567890"
flag_letras = False
cont_numeros = 0

for letra in contrasena:
    if letra in letras:
        flag_letras = True

    elif letra in numeros:
        cont_numeros += 1

if len(contrasena) >= 8 and flag_letras == True and cont_numeros >= 1:
    print("La contraseña es segura")
else:
    print("La contraseña no es segura")


"""
    3. Detector de palabras espejo
    
    En un lenguaje secreto, las palabras espejo son aquellas que se leen igual al revés
    (como “oso”, “reconocer”, “ana”). Haz un programa que reciba una palabra y diga si es una palabra espejo o no.
    
    **Importante**: No puedes usar funciones como `[::-1]` ni métodos como `.reverse()`, debes hacerlo recorriendo el string con un ciclo.
    
"""

palabra = input("Palabra: ").lower()
i = len(palabra) - 1
palabra_reverse = ""

while i >= 0:
    palabra_reverse += palabra[i]
    i -= 1

if palabra == palabra_reverse:
    print("Resultado: ES PALABRA ESPEJO")
else:
    print("Resultado: NO ES PALABRA ESPEJO")


"""
    4. Comprimidor de letras consecutivas
    
    En un sistema de compresión, se quiere simplificar palabras largas repitiendo solo la letra 
    y cuántas veces seguidas aparece. Haz un programa que reciba un string, por ejemplo, `aaabbc` , 
    y cree uno nuevo que tenga la forma: `a3b2c1`
    
    Debe recorrer el string y contar cuántas veces seguidas aparece cada letra.
"""

palabra = input("Palabra: ")
compresion = ""
i = 0

while i < len(palabra):
    contador = 1
    while i + 1 < len(palabra) and palabra[i] == palabra[i + 1]:
        contador += 1
        i += 1
    
    compresion += palabra[i] + str(contador)
    i += 1

print("Resultado:", compresion)


"""
    5. Primer y último carácter
    
    Para un análisis de texto, necesitas saber la primera y la última vez que aparece cierta letra en un string. 
    Haz un programa que reciba una palabra y una letra, y diga en qué posiciones aparece por primera y última vez la letra.
"""

palabra = input("Palabra: ")
letra_palabra = input("Letra: ")
first = -1
last = -1

i = 0
while len(palabra) > i:
    if palabra[i] == letra_palabra:
        if first == -1:
            first = i
        else:
            last = i
    i += 1

print("Resultado:")
print("Primera aparición: índice", first)
print("Última aparición: índice", last)


"""
    6. Codificador de vocales
    
    Un sistema de codificación básico reemplaza cada vocal por un número:
    
    - a → 1
    - e → 2
    - i → 3
    - o → 4
    - u → 5
    
    Haz un programa que reciba un texto y genere una versión donde cada
    vocal haya sido reemplazada por su número. Todas las demás letras quedan igual. 
"""

texto = input("Texto: ")
resultado = ""
for letra in texto:
    if letra == "a":
        letra = "1"
    elif letra == "e":
        letra = "2"
    elif letra == "i":
        letra = "3"
    elif letra == "o":
        letra = "4"
    elif letra == "u":
        letra = "5"
    resultado += letra

print("Resultado:", resultado)