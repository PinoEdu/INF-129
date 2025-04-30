"""
    1. Completa el código para hacer una cuenta regresiva antes de un despegue del 10 al 1.
"""

contador = 10
while contador > 0:
    print("Despegue en...", contador)
    contador -= 1
print("¡Despegue! 🚀")

"""
    2. Vamos a crear un ciclo que pida las calificaciones de 5 estudiantes, y luego calcule el promedio de todas las 
    calificaciones. La cantidad de calificaciones es fija (5), por lo que el ciclo se debe repetir 5 veces.

        a. Completa el siguiente código para que calcule correctamente el promedio:
"""

calificaciones_totales = 0
num_estudiantes = 0

while num_estudiantes < 5:
    calificacion = int(input("Ingrese la calificación del estudiante: "))
    calificaciones_totales += calificacion
    num_estudiantes += 1

promedio = calificaciones_totales/num_estudiantes
print("El promedio de calificaciones es:", promedio)

"""
    b. Modifica el código anterior para que, si el usuario ingresa una calificación inválida (que sea menor a 0 o mayor a 100),
    se le avise por consola con el mensaje “Calificación inválida. Debe estar entre 0 y 10.”, y pueda ingresar la nota nuevamente.
"""
calificaciones_totales = 0
num_estudiantes = 0

while num_estudiantes < 5:
    calificacion = int(input("Ingrese la calificación del estudiante: "))

    while calificacion < 0 or calificacion > 100:
        print("Calificación inválida")
        calificacion = int(input("Ingrese la calificación del estudiante: "))
        
    calificaciones_totales += calificacion
    num_estudiantes += 1

promedio = calificaciones_totales/num_estudiantes
print("El promedio de calificaciones es:", promedio)