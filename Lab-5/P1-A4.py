"""
    Actividad 4: Ejercitemos
"""

# 1. Completa la función para que retorne el promedio de 3 notas:
def promedio(n1, n2, n3):
    return (n1 + n2 + n3)/3

# 2. Completa la función para que se retorne True cuando se ingresa un número par, y False en caso contrario:
def es_par(n):
	if n%2 == 0:
		return True
	else:
		return False
	
# 3. Crea una función que retorne la cantidad de dígitos de un número. Por ejemplo, si como parámetro se le pasa 1982, debe retornar 4.
def cant_digitos(n):
	n = str(n)
	return len(n)

# 4. Imagina que estás haciendo un programa para ayudar al portero de un centro de eventos, 
# que debe decidir si pueden entrar los clientes a una fiesta, y hasta ahora va así:

# a. Crea una función llamada es_vip(nombre) que retorne True si el nombre es “Ana” o “Juan”.
def es_vip(nombre):
    return nombre == "Ana" or nombre == "Juan"

# b. Modifica el programa principal para que también pregunte el nombre del cliente, 
# y usando la función es_vip(nombre) verifique si los clientes mayores de edad son VIP o no. 
# Si es que el cliente es VIP debe imprimir “Es un cliente VIP”. 

def puede_entrar(edad):
    return edad >= 18

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese la edad: "))

if puede_entrar(edad):
    if es_vip(nombre):
        print("Es un cliente VIP")
    print("Puede entrar")
else:
    print("No puede entrar")

# 5. Una empresa quiere crear un sistema para saber si un jugo es saludable o no. Un jugo es saludable si:
def calorias_totales(porcion, cantidad):
    return porcion * cantidad

def es_saludable(azucar, calorias):
    if azucar == "sí":
        print("El jugo no es saludable")
    else:
        totales = calorias_totales(3, calorias)
        print("El jugo es saludable")
        print("Si tomas 3 porciones, serán", totales, "calorias en total.")


azucar_agregada = input("Ingrese si el jugo tiene azúcar agregada (sí/no): ")
calorias = int(input("Cuántas calorías tiene una porción: "))

es_saludable(azucar_agregada, calorias)

# 6. En una tienda se ofrecen los siguientes descuentos:
def calcular_descuento(precio):
    if precio < 10000:
        return 0.0
    elif precio <= 20000:
        return 0.1
    else:
        return 0.2

def precio_final(precio, descuento):
    return precio*(1 - descuento)

precio = int(input("Ingresa el precio del producto: "))
total = 0
while precio != -1:
    precio_actual = int(precio_final(precio, calcular_descuento(precio)))
    print("Precio final:", precio_actual)
    total += precio_actual
    precio = int(input("Ingresa el precio del producto: "))
print("Total a pagar:", total)

# 7. Aproximación del Seno y Coseno:
import math

def factorial_reciproco(n):
    return 1/math.factorial(n)

def signo(n):
    if n%2 == 0:
        return 1
    else:
        return -1

def seno_aprox(x, m):
    n = 0
    suma = 0
    while n < m:
        k = 2*n + 1 # Numeros impares
        suma += signo(n)*(x**k)*factorial_reciproco(k)
        n += 1
    return suma

def coseno_aprox(x, m):
    n = 0
    suma = 0
    while n < m:
        k = 2*n # Numeros pares
        suma += signo(n)*(x**k)*factorial_reciproco(k)
        n += 1
    return suma

# 8. Cadenas de ADN:
def valida(cadena):
    for caracter in cadena:
        if caracter not in "ACGT ":
            return False
    return True

def cantidad(cadena, base):
    contador = 0
    for caracter in cadena:
        if caracter == base:
            contador += 1
    return contador

cantidad_cadenas = int(input("Cantidad de cadenas de ADN: "))
contador = 1

cantidad_animal = 0
cantidad_vegetal = 0
cantidad_no_validas = 0

while contador <= cantidad_cadenas:
    cadena = input("Ingrese cadena " + str(contador) + ": ")
    if valida(cadena) != True:
        cantidad_no_validas += 1
    else:
        if cantidad(cadena, "C") + cantidad(cadena, "G") > cantidad(cadena, "A") + cantidad(cadena, "T"):
            cantidad_vegetal += 1
        else:
            cantidad_animal += 1
    contador += 1
    
print("Cantidad animales:", cantidad_animal)
print("Cantidad vegetales:", cantidad_vegetal)
print("Cantidad no validas:", cantidad_no_validas)