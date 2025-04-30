"""
    1. Cinco concursantes participan en una competencia de canto y reciben puntuaciones de 3 jueces 
    diferentes. Escribe un programa que por cada uno de los concursantes pida la puntuación de los 3 jueces, 
    y muestre el promedio de cada uno.
"""

numero_concursante = 1

while numero_concursante <= 5:
    print("Concursante", numero_concursante)

    numero_juez = 1
    promedio = 0

    while numero_juez <= 3:
        calificacion = int(input("Juez " + str(numero_juez) + ", ingrese la calificación (0-10): "))
        promedio += calificacion
        numero_juez += 1

    promedio = round(promedio/3, 2)
    print("Promedio del Concursante", numero_concursante, ":", promedio)

    numero_concursante += 1

print("\n¡Calificaciones registradas!")

"""
    2. Un cine vende boletos para 2 funciones del día. Cada función tiene 5 clientes que compran entre 1 y 3 boletos.
    Haz un programa que para cada función pida la cantidad de boletos de cada cliente, y al final muestre el total 
    de boletos vendidos.
"""

numero_funcion = 1
boletos_vendidos = 0

while numero_funcion <= 2:
    print("Función", numero_funcion, "- Venta de boletos")

    numero_cliente = 1
    while numero_cliente <= 5:
        cantidad_boletos = int(input("Cliente " + str(numero_cliente) + ", ¿cuántos boletos desea (1-3)? "))
        boletos_vendidos += cantidad_boletos
        numero_cliente += 1

    numero_funcion += 1

print("\nTotal de boletos vendidos en el día:", boletos_vendidos)


