def analizar_productos(nombre_archivo_tiendas):
    # Abrir el archivo que contiene el listado de tiendas
    archivo_tiendas = open(nombre_archivo_tiendas, "r")
    productos = {}  # Diccionario para almacenar productos encontrados en todas las tiendas

    # Recorrer cada línea del archivo de tiendas
    for linea in archivo_tiendas:
        linea = linea.strip().split(";")
        nombre_tienda = linea[0]

        # Abrir el archivo de productos correspondiente a la tienda actual
        tienda = open(nombre_tienda + ".txt", "r")
        for linea in tienda:
            linea = linea.strip().split(";")
            nombre_producto = linea[0]
            valor_producto = int(linea[1])
            stock_producto = int(linea[2])

            # Si hay stock del producto, lo agregamos al diccionario
            if stock_producto > 0:
                if nombre_producto not in productos:
                    productos[nombre_producto] = []  # Creamos la lista si no existe
                # Guardamos el valor y la tienda donde se encuentra ese producto
                productos[nombre_producto].append([valor_producto, nombre_tienda])
        tienda.close()
    archivo_tiendas.close()
    
    contador = 0  # Para contar la cantidad de productos diferentes

    # Para cada producto registrado
    for nombre_producto in productos:
        # Ordenar la lista de precios de ese producto, del menor al mayor
        productos[nombre_producto].sort()

        promedio = 0
        # Abrimos un archivo con el nombre del producto para escribir información
        archivo_producto = open(nombre_producto + ".txt", "w")
        for sublista in productos[nombre_producto]:
            valor_producto = sublista[0]
            nombre_tienda = sublista[1]

            promedio += valor_producto
            # Escribimos en el archivo el la tienda y el precio correspondiente
            archivo_producto.write("{}: ${}\n".format(nombre_tienda, valor_producto))

        # Calculamos el precio promedio de ese producto (redondeado a entero)
        promedio = int(promedio / len(productos[nombre_producto]))
        archivo_producto.write("Precio promedio para {}: ${}".format(nombre_producto, promedio))
        archivo_producto.close()
        
        contador += 1  # Sumamos uno al contador por cada producto

    # Retornamos la cantidad de productos
    return contador

print(analizar_productos('tiendas.txt'))