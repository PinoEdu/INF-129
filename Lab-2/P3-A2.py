"""
    Desafío 2: Cachipún
    
    - Papel le gana a Piedra
    - Piedra le gana a Tijera
    - Tijera le gana a Papel
"""

print("Bienvenid@ a Cachipun:\n", "- Presiona 1 para jugar piedra.\n", "- Presiona 2 para jugar papel.\n", "- Presiona 3 para jugar tijera.\n")

jugador1 = int(input("Jugador 1 ingresa tu opción: "))
jugador2 = int(input("Jugador 2 ingresa tu opción: "))

if jugador1 == jugador2:
    print("Ha sido un empate!")

elif jugador1 == 1: # Piedra
    if jugador2 == 2: # Papel
        print("El jugador 2 ha ganado. Thanos es el mejor villano.")
    else: # Tijera
        print("El jugador 1 ha ganado. Voldemort es el mejor villano.")

elif jugador1 == 2: # Papel
    if jugador2 == 1:   # Piedra
        print("El jugador 1 ha ganado. Voldemort es el mejor villano.")
    else:   # Tijera
        print("El jugador 2 ha ganado. Thanos es el mejor villano.")
        
elif jugador1 == 3: # Tijera
    if jugador2 == 1:   # Piedra
        print("El jugador 2 ha ganado. Thanos es el mejor villano.")
    else:   # Papel
        print("El jugador 1 ha ganado. Voldemort es el mejor villano.")