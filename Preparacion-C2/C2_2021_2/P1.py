def tienda_mas_cercana(nombre_archivo_tiendas, x, y):
    # Abrir el archivo con la información de las tiendas en modo lectura
    archivo_tiendas = open(nombre_archivo_tiendas, "r")
    
    # Inicializar la distancia más cercana con un valor muy grande
    distancia_mas_cercana = 1000000000
    # Variable para almacenar el nombre de la tienda más cercana
    nombre_tienda_mas_cercana = ""

    # Recorrer cada línea del archivo
    for linea in archivo_tiendas:
        # Limpiar la línea y separar el nombre de la cadena del listado de tiendas
        linea = linea.strip().split(";")
        nombre_tienda = linea[0] # Nombre de la cadena
        listado_tiendas = linea[1].split(":") # Lista de tiendas (separadas por ':')

        # Recorrer cada tienda de la cadena
        for tienda in listado_tiendas:
            tienda = tienda.split(",") # tienda[0]: ubicación, tienda[1]: x, tienda[2]: y
            ubicacion_tienda = tienda[0]
            coordenada_x = int(tienda[1])
            coordenada_y = int(tienda[2])

            # Calcular la distancia euclidiana entre el punto dado (x, y) y la tienda
            distancia_actual = ((x - coordenada_x)**2 + (y - coordenada_y)**2)**(1/2)
            
            # Si la distancia calculada es menor a la más cercana encontrada hasta ahora, actualizar valores
            if distancia_actual < distancia_mas_cercana:
                distancia_mas_cercana = distancia_actual
                nombre_tienda_mas_cercana = nombre_tienda + " " + ubicacion_tienda

    # Cerrar el archivo después de terminar la búsqueda
    archivo_tiendas.close()

    # Retornar el nombre de la tienda más cercana encontrada
    return nombre_tienda_mas_cercana

print(tienda_mas_cercana('tiendas.txt', 10, 5))
