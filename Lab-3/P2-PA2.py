"""
    1. En un sistema de autenticación, se le da al usuario 5 intentos para ingresar correctamente su contraseña. 
    Si se alcanzan los 5 intentos fallidos, el sistema debe bloquear al usuario.
    
    Escribe un programa que se comporte como el sistema descrito, asumiendo que la contraseña correcta es "12345”
    (la contraseña más segura, obvio). Guíate por los siguientes ejemplos de ejecución:
"""

intento_fallido_num = 0
contrasena_secreta = "12345"

while intento_fallido_num < 5:
    contrasena = str(input("Ingrese la contraseña: "))
    
    if contrasena == contrasena_secreta:
        print("Acceso permitido")
        intento_fallido_num = 5
    elif contrasena != contrasena_secreta and intento_fallido_num < 4:
        intento_fallido_num += 1
        print("Contraseña incorrecta: Intentos fallidos", intento_fallido_num)
    else:
        intento_fallido_num += 1
        print("Contraseña incorrecta: Intentos fallidos", intento_fallido_num)
        print("Se han alcanzado", intento_fallido_num,"intentos fallidos. El acceso está bloqueado.")