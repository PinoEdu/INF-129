"""
    1. Analiza los siguientes casos ¿Qué valor tendrá cada expresión?
    
        a. 5 == 5       -> True
        b. 10 != 7      -> True
        c. 3 < 8        -> True
        d. 7 >= 7       -> True
        e. 12 > 15      -> False
        f. 4 <= 3       -> False

    2. Completa la tabla evaluando las expresiones, indicando si el resultado es
    True (verdadero) o False (falso):

        5 == 10      -> False
        3 != 3       -> False
        7 < 12       -> True
        9 >= 9       -> True
        8 > 4        -> True
        2 <= 1       -> False

        a. ¿Qué ocurre si en la primera expresión 5 == 10 dejamos un solo signo igual
        (5 = 10)? Describe con tus palabras antes de probar en la consola.

        R: Se asigna el valor 10 a la variable 5, lo cual no tiene sentido en este contexto.

        b. Ahora prueba ejecutar la expresión 5 = 10 en la consola.
        ¿Qué ocurrió? ¿Era lo que esperabas?

        R: Se generó un error en sintaxis, ya que no se puede asignar un valor a un número.

        c. ¿Cuándo utilizamos = y cuándo ==?

        R: Utilizamos = para asignar un valor a una variable, y utilizamos == para comparar dos valores.

    3. ¿Qué ocurre si comparamos números de diferentes tipos? Evalúa estas expresiones y explica los resultados:

        a. 5 == 5.0         -> True
        b. 10 != 10.0       -> False
        c. 3 < 3.5          -> True

        R: Python convierte los números a un mismo tipo para poder compararlos.

        ¿Y si comparamos diferentes tipos de datos? Evalúa estas expresiones y explica los resultados:

        a. 5 == "5"         -> False
        b. 10 != "10"       -> True
        c. True == 1        -> True

        R: Python no puede comparar un número con un string, pero puede comparar un booleano con un número.
        Además, Python convierte el booleano True a 1 para poder compararlos, ya que True es equivalente a 1,
        y False es equivalente a 0.
"""