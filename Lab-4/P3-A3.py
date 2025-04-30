"""
    Desafío 3: KiwiAirlines
"""

cadena = input("Ingrese la cadena: ")
total = 0

# Chequeo de que el avión siga con asientos disponibles
asientos_disponibles = 0

for boleto in cadena:
    if boleto == "v":
        asientos_disponibles += 1

if asientos_disponibles > 0: 
    clase = input("Ingrese la clase: ")

    while clase != "Salir":

        asiento = int(input("Ingrese el número de asiento: "))
        while cadena[asiento - 1] != "v":
            print("Ocupado!")
            asiento = int(input("Ingrese el número de asiento: "))

        if clase == "Economico":
            cadena = cadena[:asiento - 1] + 'e' + cadena[asiento:]
        else:
            cadena = cadena[:asiento - 1] + 'b' + cadena[asiento:]

        print("Asignado!")
        clase = input("Ingrese la clase: ")

        # Chequeo de que el avión siga con asientos disponibles
        asientos_disponibles = 0

        for boleto in cadena:
            if boleto == "v":
                asientos_disponibles += 1

        if asientos_disponibles == 0:
            print("Avión lleno!")
            clase = "Salir"
else:
    print("Avión lleno!")

print("--------Reporte de ventas--------")
for boleto in cadena:
    if boleto == "e":
        total += 10000
    elif boleto == "b":
        total += 30000

print("Total: $", total)