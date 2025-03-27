"""
    Actividad 2: Comprendiendo los Operadores Lógicos

    1. Analizando el operador 'and':

        a. ¿Qué valor tendrá la expresión True and True? Responde y explica por qué.

        R: La expresión True and True tendrá un valor de True. Esto se debe a que el
        operador 'and' evalúa si ambos operandos son verdaderos, en este caso 
        ambos operandos son True, por lo que la expresión completa es verdadera.

        b. Completa la tabla de verdad para el operador and:

        A       B       A and B
        True    True    True
        True    False   False
        False   True    False
        False   False   False

        c. Prueba en Python: utiliza la consola de Python para verificar los resultados
        de la tabla de verdad. Puedes usar print, por ejemplo:

        print(True and True)    -> True
    
    2. Analizando el operador 'or':
        a. ¿Qué valor tendrá la expresión 'False or True'? Responde y explica por qué.

        R: La expresión False or True tendrá un valor de True. Esto se debe a que el operador or
        evaluá si al menos uno de los operadores es verdadero, en este caso el segundo operador es
        True, por lo que la expresión completa es verdadera.

        b. Completa la tabla de verdad para el operador 'or':
        
        A       B       A or B
        True    True    True
        True    False   True
        False   True    True
        False   False   False
    
    3. Analizando el operador 'not':
        a. ¿Qué valor tendrá la expresión not True? Responde y explica por qué.

        R: La expresión not True tendrá un valor de False. Esto se debe a que el operador
        not invierte el valor de la expresión, en este caso la expresión es True, por lo que
        al invertirlo el resultado es False.

        b. Completa la tabla de verdad para el operador 'not':

        A       not(A)
        True    False
        False   True

    4. Casos "Extraños"

        a. ¿Qué ocurre si usamos números en lugar de valores booleanos? Evalúa estas expresiones:

        0 and 1     -> 0
        1 or 0      -> 1
        not 0       -> True

        b. ¿Qué pasa si usamos strings en lugar de valores booleanos? Evalúa estas expresiones:

        "Hola" and ""       -> ""
        "" or "Python"      -> "Python"
        not("Mundo")        -> False

        c. Verifica con la consola de Python si tus respuestas acertaron el resultado
        en los casos anteriores.
"""