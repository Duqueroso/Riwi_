#puntos en el plano cartesiano
n = int(input("Ingrese la cantidad de puntos a procesar: "))
cuadrante_I = 0
cuadrante_II = 0
cuadrante_III = 0
cuadrante_IV = 0
eje = 0

for i in range(n):
    x = float(input(f"Ingrese la coordenada x del punto {i+1}: "))
    y = float(input(f"Ingrese la coordenada y del punto {i+1}: "))
    
    if x == 0 or y == 0:
        eje += 1
    elif x > 0 and y > 0:
        cuadrante_I += 1
    elif x < 0 and y > 0:
        cuadrante_II += 1
    elif x < 0 and y < 0:
        cuadrante_III += 1
    elif x > 0 and y < 0:
        cuadrante_IV += 1

print(f"\nResultados:")
print(f"Puntos en el Cuadrante I: {cuadrante_I}")
print(f"Puntos en el Cuadrante II: {cuadrante_II}")
print(f"Puntos en el Cuadrante III: {cuadrante_III}")
print(f"Puntos en el Cuadrante IV: {cuadrante_IV}")
print(f"Puntos sobre los ejes: {eje}")