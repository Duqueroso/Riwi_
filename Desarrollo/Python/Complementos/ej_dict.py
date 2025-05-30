#Contar frecuencia de palabras​
#Dada una lista de palabras, crea un diccionario que muestre cuántas veces
# aparece cada palabra.​ Ejemplo: ["hola", "mundo", "hola"] → {"hola": 2, "mundo": 1}.​

def count_word():
    palabras = ['Hola','Como estas','Hola','Que','Tal','estas']
    contador = {}
    for palabra in palabras:
        if palabra not in contador:
            contador[palabra] = 1
        else:
            contador[palabra] += 1

    print(contador)

#Combinar diccionarios sumando valores​
#Dados dos diccionarios, combínalos sumando los valores de las claves comunes.​
#Ejemplo: {"a": 10, "b": 20} y {"a": 5, "c": 30} → {"a": 15, "b": 20, "c": 30}.​

def sum_dict():
    dict1 = {'a':2, 'b':5, 'c':10}
    dict2 = {'a':5, 'd':5, 'b':10}
    fusion = dict1.copy()
    for key, value in dict2.items():
        if key in dict1:
            fusion[key] = dict1[key] + value
        else:
            fusion[key] = value

    print(fusion)

#Clave con el valor máximo​
#Encuentra la clave que tenga el valor más alto en un diccionario.​
#Ejemplo: {"Juan": 85, "María": 92} → "María".​
def key_max():

    diccionario = {'Juan': 70, 'María': 92, 'Pedro': 78}
    max_key = max(diccionario, key=diccionario.get)
    print(max_key)
    
#Filtrar por valor mínimo​
#Crea un nuevo diccionario solo con las claves cuyos valores sean mayores que 
#un umbral dado. Ejemplo: {"manzana": 50, "banana": 20}, umbral=30 → {"manzana": 50}.​
def umbral():
    dict1 = {"manzana": 50, "banana": 20, "kiwi":40}
    umbral_min = 30
    umbral = {}
    for key, value in dict1.items():
        if value > umbral_min:
            umbral[key] = value
    print(umbral)    

#Invertir diccionario​
#Intercambia claves y valores (asume que los valores son únicos).​
#Ejemplo: {"a": 1, "b": 2} → {1: "a", 2: "b"}.​
def invert():
    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {}
    for key, value in dict1.items():
        dict2[value] = key
    print(dict2)

#Diccionario de listas a lista de diccionarios​
#Transforma un diccionario de listas en una lista de diccionarios (como una tabla).​
#Ejemplo: {"nombre": ["Ana", "Juan"], "edad": [25, 30]} 
#→ [{"nombre": "Ana", "edad": 25}, {...}].​
def convert():
    dict1 = {"nombre": ["Ana", "Juan", "Camilo"], "edad": [20, 25, 30]}
    lista = []
    for i in range(len(dict1["nombre"])):
        diccionario = {}
        for key in dict1:
            diccionario[key] = dict1[key][i]
        lista.append(diccionario)
    print(lista)

