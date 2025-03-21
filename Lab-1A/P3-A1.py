distancia_marte = 225000000
velocidad_nave = 50000

distancia_total = 2 * distancia_marte
tiempo_total = round(distancia_total/velocidad_nave, 1)

print("Tiempo total de viaje:", tiempo_total, "horas")