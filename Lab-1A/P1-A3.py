"""
    Actividad 3: Precedencia de los Operadores

    1. Observa las siguientes expresiones y predice el resultado antes de ejecutarlas 
    en Python. Escribe tus respuestas y luego compáralas con los resultados reales:

    a. 5 + 2 * 3            -> 11
    b. (5 + 2) * 3          -> 21
    c. 20//3 + 2 * 4        -> 14
    d. 20//(3 + 2) * 4      -> 16
    e. 2 + 3 - 5 + 6        -> 6
    f. 3 * 4/5 + 1          -> 3.4

    2. Responde:

    a. ¿Qué sucede cuando usas paréntesis?

    R:  Los paréntesis cambian el orden en el que se evalúan las operaciones. Tienen
    mayor precedencia en Python, por lo que cualquier cálculo dentro de paréntesis se
    ejecuta primero.

    b. ¿Cuál operación tiene mayor precedencia: multiplicación, potencia o suma?

    R:  La operación potencia ( ** ) tiene mayor precedencia, seguida por la multiplicación
    ( * ), y por último la suma ( + ).

    c. ¿Qué pasa si dos operadores tienen la misma precedencia?

    R:  Si dos operadores tiene la misma precedencia, Python evalua de izquierda a derecha,
    excepto en el caso de potencia ( ** ), que se evalúa de derecha a izquierda.
    
"""