"""
    Desafío 3: Nuevo Calculador de Promedio Avanzado V1.0 de Goddard
"""

num_certamen = 1
promedio_certamenes = 0

while num_certamen <= 3:
    nota_certamen = int(input("Ingrese la nota del certamen " + str(num_certamen) + ": "))

    if num_certamen <= 2:
        promedio_certamenes += nota_certamen
    else:
        promedio_certamenes = nota_certamen*(promedio_certamenes/2)**2
    
    num_certamen += 1

promedio_certamenes = promedio_certamenes**(1/3)

num_tareas = 0
promedio_tareas = 0
nota_tarea = int(input("Ingresa la nota de la tarea: "))

while nota_tarea != -1:
    num_tareas += 1
    promedio_tareas += nota_tarea
    nota_tarea = int(input("Ingresa la nota de la tarea: "))

promedio_tareas = promedio_tareas/num_tareas

promedio_final = round(0.75*promedio_certamenes + 0.25*promedio_tareas, 2)
print("Nota final:", promedio_final)