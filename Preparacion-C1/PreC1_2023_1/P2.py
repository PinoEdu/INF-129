def desplazar(c, d):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    i = 0
    while i < len(alfabeto) and alfabeto[i] != c:
        i += 1
    if i < len(alfabeto):
        j = (i+d)%len(alfabeto)
        return alfabeto[j]
    return c

def desplazar_texto(texto, cantidad):
    texto_desplazado = ""

    for letra in texto:
        texto_desplazado += desplazar(letra, cantidad)
    
    return texto_desplazado

def codificar(texto):
    texto_codificado = ""
    auxiliar = ""
    for caracter in texto:
        if caracter != "#" and caracter != ";" and caracter not in "0123456789":
            auxiliar += caracter
        else:
            if caracter != "#" and caracter != ";":
                desplazamiento = int(caracter)

                texto_codificado += desplazar_texto(auxiliar, desplazamiento) + " "
                auxiliar = ""
    
    return texto_codificado

print(codificar("edad#1"))
print(codificar("hola#3;mundo#2"))