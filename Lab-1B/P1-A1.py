"""
    1. Analiza el siguiente código y responde: ¿si lo ejecutamos funcionará? ¿por qué?

        y = x + 5   -> 'y' requiere del valor de 'x'
        x = 10
        print(y)
    
    No funcionará, ya que en Python el código se ejecuta de forma secuencial,
    y la variable 'x' se define después de que intentamos usarla para calcular 'y'.
"""

# Codigo corregido
x = 10
y = x + 5 
print(y)