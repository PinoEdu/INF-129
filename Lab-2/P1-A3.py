"""
    Actividad 3: Explorando Combinaciones de operadores

    1. Dado los siguientes códigos, ¿qué valores (True o False) devolverán las expresiones?
"""

edad = 25
tiene_licencia = False
print(edad >= 18 and tiene_licencia)    # False

temperatura = 30
print(temperatura < 0 or temperatura > 25)    # True

a = 10
b = 5
print(not (a < b or b == 5))    # False

x = 12
y = 7
print(x % 2 == 0 and y % 2 != 0)    # True