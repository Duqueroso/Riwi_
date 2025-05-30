#Ingresar 10 numeros y sacar promedio, mostrarlos
'''sum=0
lista = []
for i in range(0,10,1):
    num = int(input(f"Ingrese el valor {i}: "))
    lista.append(num)
    sum = sum+num
    promedio = int(sum/10)

print(f"Los numeros que ingresaste son: {lista}")
print(f"El promedio es: {promedio}")'''


#Número mayores o iguales a 1000
'''mayores = []
print("="*20)
print("Ingresa 10 numeros")
print("="*20)
for i in range(0,10,1):
    num = int(input(f"Ingresa el {i+1} numero: "))
    if num >= 1000:
        mayores.append(num)

print(f"De los numeros que ingresaste estos son mayores o iguales a 1000: {len(mayores)}")
print(f"Los cuales son: {mayores}")

'''

#puntos en el plano cartesiano
'''n = int(input("Ingrese la cantidad de puntos a procesar: "))
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
print(f"Puntos sobre los ejes: {eje}")'''

#Calculo de areas de triangulo
n = int(input("Ingrese la cantidad de triángulos a procesar: "))

contador_superficie_mayor_12 = 0

print("\nResultados:")
print("Base\tAltura\tSuperficie")
print("-" * 30)

for i in range(n):
    base = float(input(f"Ingrese la base del triángulo {i+1}: "))
    altura = float(input(f"Ingrese la altura del triángulo {i+1}: "))
    print("-" * 30)
    
    superficie = (base * altura) / 2
    
    print(f"base:{base}\taltura:{altura}\tsuperficie:{superficie}")
    print("-" * 30)
    if superficie > 12:
        contador_superficie_mayor_12 += 1

print(f"\nCantidad de triángulos con superficie mayor a 12: {contador_superficie_mayor_12}")