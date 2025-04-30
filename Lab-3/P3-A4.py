"""
    Desafío 4: La tienda de Doña Lucía
"""

num_clientes = 0
monto_total_ganado = 0
promedio_gasto_clientes = 0

nombre_cliente = str(input("Ingrese cliente: "))

while nombre_cliente != "cerrar" and monto_total_ganado < 200000:
    num_clientes += 1

    contador_articulos = 0
    cantidad_articulos = int(input("Ingrese cantidad de artículos: "))
    while contador_articulos < cantidad_articulos:
        precio = int(input("Ingrese precio: "))
        monto_total_ganado += precio
        contador_articulos += 1
    
    print("-----------------------------")
    if monto_total_ganado < 200000:
        nombre_cliente = str(input("Ingrese cliente: "))

        if nombre_cliente == "cerrar":
            print("-----------------------------")

print("Total del día:", monto_total_ganado)
print("Promedio gastado por cliente:", int(monto_total_ganado/num_clientes))