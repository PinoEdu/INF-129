import random # Biblioteca para generar numeros aleatorios
import math # Biblioteca de funciones matematicas

# 1: Guarde un numero aleatorio entre el 1 y el 5 en una variable
numero = random.randint(1,5)
print("Numero:", numero)

#2: Calcule e imprima la raiz cuadrada del numero, redondeada al 3er decimal
raiz_cuadrada = math.sqrt(numero)
raiz_redondeada = round(raiz_cuadrada, 3)
print("Raiz cuadrada (redondeada a 3 decimales):", raiz_redondeada)

# 3: Calcule e imprima la potencia de ese numero elevado a -6
potencia_numero = math.pow(numero, -6)
print("Potencia (-6):", potencia_numero)
# Tambien se puede utilizar el operador **

# 4: Calcule e imprima el valor exponencial de ese numero aproximado al entero mas cercano.
exp_numero = math.exp(numero)
exp_aprox = round(exp_numero)
print("Valor exponencial aproximado al entero mas cercano:", exp_aprox)

# 5: Calcule e imprima el valor exponencial de ese numero truncado
exp_trunc = int(exp_numero)
print("Valor exponencial truncado:", exp_trunc)
# Tambien se puede utilizar la funcion math.trunc()
