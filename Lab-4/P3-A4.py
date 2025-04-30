"""
    Desafío 4: El arte de mezclar colores
"""

combinaciones = input("Ingrese las combinaciones: ")
color_deseado = input("Que color deseas: ")

if color_deseado in combinaciones:
    i = 0
    while i < len(combinaciones):
        if combinaciones[i] == ";":
            if color_deseado in combinaciones[:i]:
                j = i - 1
                while j > 0 and combinaciones[j] != "=":
                    j -= 1

                print(combinaciones[j + 1:i])
                i = len(combinaciones)  # Me aseguro de no seguir iterando
        i += 1
else:
    print("No puedes obtener este color :(")
