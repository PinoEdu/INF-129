def mas_pedidos(nombre_archivo):
    # Abre el archivo con los pedidos en modo lectura
    archivo_pedidos = open(nombre_archivo, "r")
    diccionario_juguetes = {}  # Diccionario para contar cuántas veces se pide cada juguete

    # Recorre cada línea (pedido) en el archivo
    for linea in archivo_pedidos:
        # Elimina saltos de línea y separa los campos por ":"
        linea = linea.strip().split(":")
        # Obtiene el listado de juguetes pedidos
        listado_juguetes = linea[2]
        # Separa los juguetes por ","
        listado_juguetes = listado_juguetes.split(",")

        # Cuenta cuántas veces aparece cada juguete
        for juguete in listado_juguetes:
            if juguete not in diccionario_juguetes:
                diccionario_juguetes[juguete] = 1  # Primer pedido de este juguete
            else:
                diccionario_juguetes[juguete] += 1  # Ya se había pedido antes, suma uno

    archivo_pedidos.close()  # Cierra el archivo de pedidos

    # Prepara una lista con pares [cantidad, nombre_juguete] para ordenar fácilmente
    juguetes_contadores = []
    for nombre_juguete in diccionario_juguetes:
        juguetes_contadores.append([diccionario_juguetes[nombre_juguete], nombre_juguete])

    # Ordena la lista por cantidad de mayor a menor
    juguetes_contadores.sort()
    juguetes_contadores.reverse()
    # Toma solo los tres juguetes más pedidos
    juguetes_contadores = juguetes_contadores[:3]

    cantidad_juguetes = 0  # Lleva la suma total de los pedidos de los tres juguetes más pedidos
    # Abre el archivo de salida para escribir los resultados
    archivo_mas_pedidos = open("mas_pedidos.txt", "w")
    for sublista in juguetes_contadores:
        cantidad = sublista[0]
        nombre_juguete = sublista[1]
        # Escribe en el archivo la cantidad de pedidos y el nombre del juguete
        archivo_mas_pedidos.write("Se pidio {} veces {}\n".format(cantidad, nombre_juguete))
        cantidad_juguetes += cantidad  # Suma la cantidad al total

    archivo_mas_pedidos.close()  # Cierra el archivo de salida

    return cantidad_juguetes  # Devuelve el total de pedidos de los 3 juguetes más pedidos

print(mas_pedidos("cartas.txt"))
