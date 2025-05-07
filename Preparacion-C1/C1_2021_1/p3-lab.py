def votos_partido(votos, partido):
    contador = 0
    auxiliar = ""
    for caracter in votos:
        if caracter != "$":
            auxiliar += caracter
        else:
            if auxiliar == partido:
                contador += 1
            auxiliar = ""
    if auxiliar == partido:
        contador += 1
    return contador

coaliciones = input("Ingrese coaliciones: ")
votos_partidos = input("Ingrese votos por partido: ")

coalicion = ""
auxiliar = ""
nombre_ganador = ""
cantidad_ganadora = -1
contador = 0

for caracter in coaliciones:
    if caracter != ":" and caracter != "-" and caracter != ";":
        auxiliar += caracter
    else:
        if caracter == ":":
            coalicion = auxiliar
        elif caracter == "-" or caracter == ";":
            cantidad_votos = votos_partido(votos_partidos, auxiliar)
            contador += cantidad_votos
            print(auxiliar, cantidad_votos)

            if caracter == ";":
                print(" Total coalición", coalicion, ":", cantidad_votos)

                if contador > cantidad_ganadora:
                    cantidad_ganadora = contador
                    nombre_ganador = coalicion
                
                contador = 0
                coalicion = ""

        auxiliar = ""

cantidad_votos += votos_partido(votos_partidos, auxiliar)
contador += cantidad_votos
print(auxiliar, cantidad_votos)
print(" Total coalición", coalicion, ":", cantidad_votos)

if contador > cantidad_ganadora:
    cantidad_ganadora = contador
    nombre_ganador = coalicion

print("La coalición ganadora es", nombre_ganador, "con", cantidad_ganadora ,"votos")