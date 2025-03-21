nevarro_nummies = float(input("Nevarro Nummies consumidas (en unidades): "))
NM_GRASAS = 1.90
NM_CARBO = 6.00
NM_PROTE = 0.80
nm_factor = nevarro_nummies     # Como es por unidad, el factor es el mismo numero de unidades ingresadas

space_soup = float(input("Space Soup consumida (en [ml]): "))
SS_GRASAS = 10.0
SS_CARBO = 12.0
SS_PROTE = 11.0
ss_factor = space_soup/285      # Normalizar con respecto a 285 ml

carne_rana_ingerido = float(input("Carne de rana consumida (en [g]): "))
CR_GRASAS = 0.30
CR_CARBO = 0.00
CR_PROTE = 16.0
cr_factor = carne_rana_ingerido/100     # Normalizar con respecto a 100 g

grasas_totales = nm_factor*NM_GRASAS + ss_factor*SS_GRASAS + cr_factor*CR_GRASAS
carbo_totales = nm_factor*NM_CARBO + ss_factor*SS_CARBO + cr_factor*CR_CARBO
prote_totales = nm_factor*NM_PROTE + ss_factor*SS_PROTE + cr_factor*CR_PROTE

print("Grogu ha consumido:")
print(round(grasas_totales, 2), "[g] de grasas")
print(round(carbo_totales, 2), "[g] de carbohidratos")
print(round(prote_totales, 2), "[g] de proteinas")