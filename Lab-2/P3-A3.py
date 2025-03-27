"""
    Desafío 3: PyGic

    El programa debe recibir el nombre de la carta, su rareza (comun o rara), su ataque y su defensa. 
    Para obtener el precio en dólares de las cartas se utiliza el siguiente método:

    - Si la carta es común:
        - Si la suma de su ataque y defensa es mayor a 15, entonces su precio es: 2 * ataque + defensa
        - Si no, su precio es: ataque + defensa / 2
    - Si la carta es rara:
        - Si la multiplicación de su ataque con su defensa es mayor a 30, entonces su precio es: 2 * (ataque + defensa) + 1
        - Si no, su precio es: ataque + 2 * defensa + 1

    Finalmente, si el precio de la carta es menor a 20 dólares, entonces el programa debe imprimir 
    “Por ese precio me compro un mejor posavasos”. Si el precio de la carta es mayor o igual a 20, debe imprimir
    “Su carta [nombre] vale [precio], y me estoy arriesgando”.
"""

nombre = input("Ingrese el nombre de la carta: ")
rareza = input("Ingrese rareza (comun/rara): ")
ataque = int(input("Ingrese ataque: "))
defensa = int(input("Ingrese defensa: "))

if rareza == "comun":
    if ataque + defensa > 15:
        precio = 2 * ataque + defensa
    else:
        precio = ataque + defensa/2

elif rareza == "rara":
    if ataque * defensa > 30:
        precio = 2 * (ataque + defensa) + 1
    else:
        precio = ataque + 2 * defensa + 1

if precio < 20:
    print("Por este precio mejor me compro un posavasos.")
else:
    print("Su carta", nombre, "vale", precio, "y me estoy arriesgando.")