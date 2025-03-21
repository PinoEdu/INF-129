"""
    1. Escribe un programa que reciba dos números enteros como entrada,
    los sume y muestre el resultado. Guíate con el ejemplo a continuación,
    que muestra cómo se debería ver el resultado de la ejecución del programa en la consola:
"""

primer_numero = int(input("Ingresa el primer número: "))
segundo_numero = int(input("Ingresa el segundo número: "))

print("La suma resultante de ambos números es:", primer_numero + segundo_numero)

"""
    2. Escribe un programa que pregunte al usuario su nombre y edad,
    y luego muestre un mensaje saludando a la persona y mostrando
    su edad el próximo año. Guíate con el siguiente ejemplo de ejecución:
"""

nombre = str(input("Ingresa tu nombre: "))
edad = int(input("Ingresa tu edad actual: "))

print("¡Hola " + nombre + "!")
print("El próximo año tendrás", edad + 1, "años")

# Tambien se puede hacer de la siguiente forma
#print("¡Hola " + nombre + "!\n" + "El próximo año tendrás " + str(edad + 1) + " años")