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


votos = "p3$p31$p4$p3$p1$p6$p4$p5$p310$p6$p8$p8$p4$p4$p2$p3"
print(votos_partido(votos, "p3"))
print(votos_partido(votos, "p6"))
print(votos_partido(votos, "p7"))