#Definimos variables

producto = []
precio = []
total = 0

#Solicitamos informacion

cantidad = int(input("Cuantos elementos desea agregar: "))

for i  in range(cantidad):
    elemento = input(f"Ingrese el elemento {i+1}: ")
    producto.append(elemento)
    valor = input(f"Ingrese el valor del elemento {i+1}: ")
    precio.append(valor)
    i=+1

total = sum(precio)


print (total)