arreglo = [22.5,23.0, 24.1, 23.8, 25.2]

print("Acceso por indice")

print(f"lectura inicial: {arreglo[0]}C tercera lectura inicial: {arreglo[2]}C")

print("\n recorrido secuencial")

for indice, temperatura in enumerate(arreglo):
    print(f"momento {indice} -> {temperatura}C")
    
print("\n modificando expancion")

arreglo[1] = 23.5
arreglo.append(26.0)
print(f"vector final: {arreglo}")