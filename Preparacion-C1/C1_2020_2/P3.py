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

def local_votacion(letra):
    if letra.upper() in "ABCDEFG":
        return "Peumo"
    elif letra.upper() in "HIJKLMNO":
        return "Quillay"
    else:
        return "Canelo"

def numero_mesa(nombre):
    return len(nombre)%3 + 1

print("Datos del votante:")
rut_completo = input("RUT (con guión y dígito verificador): ")

dv = digito_verificador(int(rut_completo[0:-2]))

while rut_completo[-1] == str(dv):
    apellidos = input("Apellidos: ")
    nombre = input("Nombre: ")

    local = local_votacion(apellidos[0])
    numero = numero_mesa(nombre)

    print("Le toca votar en la mesa", local, "-", numero)

    print()
    print("Datos del votante:")
    rut_completo = input("RUT (con guión y dígito verificador): ")
    
    dv = digito_verificador(int(rut_completo[0:-2]))