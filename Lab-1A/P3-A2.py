import math

distancia_marte = 225000000
velocidad_nave = 50000

distancia_total = 2 * distancia_marte
tiempo_total = round(distancia_total/velocidad_nave, 1)

print("Tiempo total de viaje:", tiempo_total, "horas")

oxigeno_por_hora = 0.035
oxigeno_total = round(tiempo_total * oxigeno_por_hora * 4, 1)
tanques_necesarios = oxigeno_total/500

tanques_necesarios = math.ceil(tanques_necesarios)

print("Consumo total de oxigeno:", oxigeno_total, "kg")
print("Cantidad de tanques de oxigeno necesarios:", tanques_necesarios)
