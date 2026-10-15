piezas = ["tornillo", "tuerca", "tornillo", "arandela", "tornillo", "arandela"]

conteo = {}
for pieza in piezas:
    if pieza in conteo:
        conteo[pieza]+= 1
        
    else:
        conteo[pieza] = 1
        
print(conteo)