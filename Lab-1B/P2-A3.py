"""
    Actividad 3: Parte entera y decimal de un número

    Vamos a aplicar lo aprendido hasta ahora realizando
    un pequeño programa.

    Escribe un programa que entregue la parte entera y
    la parte decimal de un número real ingresado por el usuario.
"""

numero = float(input("Ingrese un numero real: "))
parte_entera = int(numero)      # Truncamos el numero para solo tener la parte entera
parte_decimal = abs(numero - parte_entera)  # Le aplicamos la funcion valor absoluto 'abs()'

print("La parte entera es: " + str(abs(parte_entera)))
print("La parte decimal es:", parte_decimal)