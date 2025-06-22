def pedidos_por_nino(nombre_archivo):
    # Abre el archivo de pedidos en modo lectura
    archivo_pedidos = open(nombre_archivo, "r")
    diccionario_ninios = {}  # Diccionario para almacenar los pedidos de cada niño

    # Recorre cada línea (pedido) en el archivo
    for linea in archivo_pedidos:
        linea = linea.strip().split(":")  # Elimina saltos de línea y separa los campos
        anio = linea[0]                  # Año del pedido
        nombre_ninio = linea[1]          # Nombre del niño
        listado_juguetes = linea[2]      # Lista de juguetes pedidos (en texto, separados por coma)

        # Si el niño no está en el diccionario, lo agrega con su primer pedido (año y juguetes)
        if nombre_ninio not in diccionario_ninios:
            diccionario_ninios[nombre_ninio] = [[int(anio), listado_juguetes.split(",")]]
        else:
            # Si ya existe, agrega el nuevo pedido a la lista de ese niño
            diccionario_ninios[nombre_ninio].append([int(anio), listado_juguetes.split(",")])
    
    archivo_pedidos.close()  # Cierra el archivo de lectura

    # Ordena los pedidos de cada niño por año
    for nombre_ninio in diccionario_ninios:
        diccionario_ninios[nombre_ninio].sort()
    
    contador_ninios = 0  # Contador para saber cuántos niños hay

    # Abre el archivo de salida para escribir los resultados
    archivo_pedidos = open("pedidos_por_nino.txt", "w")
    for nombre_ninio in diccionario_ninios:
        archivo_pedidos.write("{}:\n".format(nombre_ninio))  # Escribe el nombre del niño

        # Recorre los pedidos ordenados por año
        for sublista in diccionario_ninios[nombre_ninio]:
            anio = sublista[0]               # Año del pedido
            listado_juguetes = sublista[1]   # Lista de juguetes en ese pedido
            for juguete in listado_juguetes:
                archivo_pedidos.write("\t\t{}:{}\n".format(anio, juguete))  # Escribe el año y el juguete

        contador_ninios += 1  # Suma uno por cada niño procesado

    archivo_pedidos.close()  # Cierra el archivo de salida

    return contador_ninios  # Retorna la cantidad total de niños

print(pedidos_por_nino("cartas.txt"))