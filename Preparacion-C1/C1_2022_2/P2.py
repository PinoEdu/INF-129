def obtener_columna(imagen, columna):
    largo = int(len(imagen)**(1/2))
    fila = ""
    columna_solicitada = ""

    for caracter in imagen:
        if len(fila) != largo:
            fila += caracter
        else:
            columna_solicitada += fila[columna - 1]
            fila = caracter

    columna_solicitada += fila[columna - 1]

    return columna_solicitada

print(obtener_columna("eeeSeSeSeSSSSeee", 1))
print(obtener_columna("eeeSeSeSeSSSSeee", 3))