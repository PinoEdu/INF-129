def obtener_columna(imagen, columna):
    largo = int(len(imagen)**(1/2))
    fila = ""
    columna_solicitada = ""

    for caracter in imagen:
        if len(fila) < largo:
            fila += caracter
        else:
            columna_solicitada += fila[columna - 1]
            fila = caracter

    columna_solicitada += fila[columna - 1]

    return columna_solicitada

def misterio(imagen,nf):
    sz = int(len(imagen)**0.5)
    i = (nf-1) * sz
    return imagen[i:(nf*sz)]

imagen= input("Ingrese imagen a procesar: ")
patron_buscar = input("Ingrese imagen a procesar: ")

largo = int(len(imagen)**0.5)
columna = 1

print("Imagen:")
while columna <= largo:
    print(misterio(imagen,columna))
    columna += 1

columna = 1
while columna <= largo:
    columna_obtenida = obtener_columna(imagen, columna)
    contador = 0
    auxiliar = ""

    for caracter in columna_obtenida:
        if len(patron_buscar) > len(auxiliar):
            auxiliar += caracter
        else:
            if patron_buscar == auxiliar:
                contador += 1
            
            auxiliar = auxiliar[1:] + caracter
            
    if patron_buscar == auxiliar:
        contador += 1
    
    if contador != 0:
        print("El patrón", patron_buscar, "aparece", contador, "veces en la columna", columna)

    columna += 1
    