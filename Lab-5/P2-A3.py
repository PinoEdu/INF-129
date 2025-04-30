"""
    Desafío 3: Carreras
"""
from random import randint

def lanzar_dado():
    return randint(1,12)

def multiplo_6(n):
    return n%6 == 0

def primo(n):
    if n <= 1:
        return False
    
    divisor = 2
    while divisor < n/2: # Debe ser hasta n/2 ya que si es mayor, nunca podrá dividir a n
        if n%divisor == 0:
            return False
        divisor += 1
    return True

posicion1 = 0
posicion2 = 0
punto_poder1 = 0
punto_poder2 = 0
while posicion1 <= 100 and posicion2 <= 100:
    print("-------------------------------------")
    print("Turno de jugador 1: ")
    jugada = input("Apreta enter para lanzar los dados!")
    dado = lanzar_dado()
    posicion1 += dado
    print("Te ha salido", dado)
    if multiplo_6(posicion1): #utilizar función multiplo_6 para verificar si posicion1 es múltiplo de 6:
        print("Quedas en la posición", posicion1)
        posicion1 -= 2
        print("Caes en un múltiplo de 6, retrocedes 2 casillas.")
        print("Quedas en la posición", posicion1)
    elif primo(posicion1): #utilizar función primo para ver si posicion1 es primo:
        punto_poder1 += 1
        print("Quedas en la posición", posicion1)
        print("Caes en un primo, acumulas 1 punto de poder. Tienes", punto_poder1, "puntos")
        if punto_poder1 == 3:
            punto_poder1 = 0
            print("Has acumulado 3 puntos de poder, tiras los dados nuevamente") 
            jugada = input("Apreta enter para lanzar los dados!")
            dado = lanzar_dado() #utilizar función lanzar_dados para lanzar los dados
            posicion1 += dado
            print("Te ha salido", dado)
            print("Quedas en la posición", posicion1)
    else:
        print("Quedas en la posicion", posicion1)
        
    if posicion1 <= 100:
        print("-------------------------------------")
        print("Turno de jugador 2: ")
        jugada = input("Apreta enter para lanzar los dados!")
        dado = lanzar_dado() #utilizar función lanzar_dados para lanzar los dados
        posicion2 += dado
        print("Te ha salido", dado)
        if multiplo_6(posicion2): #utilizar función multiplo_6 para verificar si posicion2 es múltiplo de 6:
            print("Quedas en la posición", posicion2)
            posicion2 -= 2
            print("Caes en un múltiplo de 6, retrocedes 2 casillas.")
            print("Quedas en la posición", posicion2)
        elif primo(posicion2): #utilizar función primo para ver si posicion2 es primo:
            punto_poder2 += 1
            print("Quedas en la posición", posicion2)
            print("Caes en un primo, acumulas 1 punto de poder. Tienes", punto_poder2, "puntos")
            if punto_poder2 == 3:
                punto_poder2 = 0
                print("Has acumulado 3 puntos de poder, tiras los dados nuevamente") 
                jugada = input("Apreta enter para lanzar los dados!")
                dado = lanzar_dado() #utilizar función lanzar_dados para lanzar los dados
                posicion2 += dado
                print("Te ha salido", dado)
                print("Quedas en la posición", posicion2)
        else:
            print("Quedas en la posición", posicion2)

print("-------------------------------------")
print("FIN DEL JUEGO")
if posicion1 > 100:
    print("Jugador 1 gana")
else:
    print("Jugador 2 gana")