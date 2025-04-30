"""
    Actividad 3: Prints vs Return

    1. Analiza:

    def saludar(nombre):
        print("Hola", nombre)

    mensaje = saludar("Martín")
    print("Mensaje guardado:", mensaje)


    a. ¿Qué imprime este programa?

    R: Imprime "Hola Martín, y luego imprime "Mensaje guardado: None"

    b. ¿Cuál es el valor de la variable `mensaje`?

    R: El valor es None, ya que la función no tiene retorno.

    c. Comprueba tus respuestas copiando y ejecutando el código.

    R: OK

    2. Este código da un error. ¿Por qué?

    def cuadrado(n):
        print(n * n)

    resultado = cuadrado(6)
    doble_resultado = resultado * 2

    R: Ya que resultado es None y doble_resultado multiplica None * 2, generando un error.

    a. Reescribe la función para que funcione bien usando return.

    def cuadrado(n):
        return n * n
    
    resultado = cuadrado(6)
    doble_resultado = resultado * 2
"""