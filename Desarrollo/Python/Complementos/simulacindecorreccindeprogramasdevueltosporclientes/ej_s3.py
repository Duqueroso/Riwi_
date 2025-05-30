"""El siguiente código intenta sumar los precios de un diccionario, pero no funciona.
Encuentra el error y corrígelo para que calcule correctamente el total. python"""

precios = {"manzana": 1.5, "banana": 0.8, "pera": 1.2}
precio = precios.values()
frutas = precios.keys()
total = 0
for valor in precio:
    total += valor
print(total)

#Corregir error
usuario = {"nombre": "Ana", "edad": 30}
print(usuario["nombre"])

#Corregir error
dic1 = {"a": 1, "b": 2}
dic2 = {"b": 3, "c": 4}
fusion = {**dic1, **dic2}
for i in fusion:
    if i in dic1 and i in dic2:
        fusion[i] = dic1[i] + dic2[i]
    else:
        fusion[i] = fusion[i]
print(fusion)

#Corregir error
inventario = {"laptop": 5, "mouse": 10}
inventario.update({"laptop": 2})
print(inventario)

"""Enunciado:
El siguiente código debería contar cuántas veces aparece cada palabra en una lista, 
pero no funciona correctamente. ¿Puedes encontrar el error y arreglarlo?
python"""

palabras = ["manzana", "banana", "manzana", "pera", "banana", "manzana"]
contador = {}

for palabra in palabras:
    if palabra not in contador:
        contador[palabra] = 1
    else:
        contador[palabra] += 1

print(contador)