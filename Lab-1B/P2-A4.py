"""
    Actividad 4: Pseudo-Fibonacci
    
    En 1843 el matemático francés Jacques Philippe Marie Binet publicó
    su trabajo acerca de la Fórmula de Binet, que permite calcular el
    enésimo elemento de la sucesión de Fibonacci.

    Escribe un programa en Python que solicite un número n y calcule
    la enésima sucesión de Fibonacci usando la Fórmula de Binet. 
    Debe mostrar el resultado por pantalla.
"""
import math

n = int(input("Ingrese un número n: "))

numerador = ((1 + math.sqrt(5))**n) - ((1 - math.sqrt(5))**n)
denominador = (2**n)*math.sqrt(5)
f_n = numerador/denominador

print("El n-ésimo número de Fibonacci es:", round(f_n))

