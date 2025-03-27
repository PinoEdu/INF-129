"""
    Desafío 1: League of Python

    - Bronce: si la suma es menor o igual que 300 pts.
    - Plata: si la suma es mayor que 300 y menor o igual que 500 pts.
    - Oro: si la suma es mayor que 500 y menor o igual que 700 pts.
    - Platino: si la suma es mayor que 700 y menor o igual que 1000 pts.
    - Diamante: si la suma es mayor que 1000 pts.
"""

primer_puntaje = int(input("Ingrese el puntaje de la primera partida: "))
segundo_puntaje = int(input("Ingrese el puntaje de la segunda partida: "))

suma_puntajes = primer_puntaje + segundo_puntaje

if suma_puntajes <= 300:
    print("Tu division es Bronce")
elif 300 < suma_puntajes and suma_puntajes <= 500:
    print("Tu division es Plata")
elif 500 < suma_puntajes and suma_puntajes <= 700:
    print("Tu division es Oro")
elif 700 < suma_puntajes and suma_puntajes <= 1000:
    print("Tu division es PLatino")
else:
    print("Tu division es Diamante")