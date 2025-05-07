def votos_partido(votos, partido):
    contador = 0
    p = "" # Creamos una variable auxiliar para ir concatenando los caracteres correspondiente a un voto
    for caracter in votos:
        if caracter != "$":
            p += caracter
        else:
            if p == partido:
                contador += 1
            p = ""  # Reiniciamos la variable auxiliar para pasar a otro voto
    
    if p == partido:
        contador += 1

    return contador

coaliciones = input("Ingrese coaliciones: ")
votos = input("Ingrese votos por partido: ")

coalicion = ""
auxiliar = ""
nombre_ganador = ""
cantidad_ganador = -1
contador = 0

for caracter in coaliciones:
    if caracter != ":" and caracter != "-" and caracter != ";":
        auxiliar += caracter
    else:
        if caracter == ":":
            coalicion = auxiliar
            print("Coalición:", coalicion)

        elif caracter == "-" or caracter == ";":
            cantidad_votos = votos_partido(votos, auxiliar)
            contador += cantidad_votos
            print(auxiliar, cantidad_votos)

            if caracter == ";":
                print("Total coalición", coalicion, ":", contador)

                if contador > cantidad_ganador:
                    cantidad_ganador = contador
                    nombre_ganador = coalicion
                
                contador = 0
                coalicion = ""

        auxiliar = ""

cantidad_votos = votos_partido(votos, auxiliar)
contador += cantidad_votos
print(auxiliar, cantidad_votos)
print("Total coalición", coalicion, ":", contador)

if contador > cantidad_ganador:
    cantidad_ganador = contador
    nombre_ganador = coalicion

print("La coalición ganadora es", nombre_ganador, "con", cantidad_ganador, "votos")
