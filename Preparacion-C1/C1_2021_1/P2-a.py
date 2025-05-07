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

votos = "p3$p31$p4$p3$p1$p6$p4$p5$p310$p6$p8$p8$p4$p4$p2$p3"

print(votos_partido(votos, "p3"))
print(votos_partido(votos, "p6"))
print(votos_partido(votos, "p7"))