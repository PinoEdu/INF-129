def suma_productos(rut):
    suma_n = 0
    i = 2   # constante a multiplicar, comenzando por la derecha: 2, 3, 4, 5, 6, 7, 2, 3
    while rut != 0:
        n = rut%10      # obtiene el dígito de mas a la derecha
        rut = rut//10   # elimina el dígito de mas a la derecha
        suma_n += n*i
        # A continuación, se actualiza la constante para la siguiente iteración
        i += 1
        if i == 8:  # después del 7, vuelve a 2
            i = 2
    return suma_n

def digito_verificador(rut):
    p = suma_productos(rut)
    r = p%11
    verificador = 11 - r

    if verificador == 11:
        verificador = 0
    elif verificador == 10:
        verificador = "k"
    
    return verificador

#print(digito_verificador(13252311)) # 8
#print(digito_verificador(15136120)) # k
#print(digito_verificador(15136125)) # 0

rut = int(input('Ingrese su RUT: '))
d = digito_verificador(rut)
rut_completo = str(rut) + '-' + str(d)
print(rut_completo)