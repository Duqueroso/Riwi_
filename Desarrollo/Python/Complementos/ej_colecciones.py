#sumar elementos de una lista
def sum_list():
    list = [1,2,3,4]
    total = sum(list)
    print(total)

#Eliminar duplicados de una lista con for
def remove_duplicates():
    list = [1,2,3,4,5,1,2,3]
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    print(new_list)

#Invertir lista sin metodos bult-in sin crear nueva lista
def reverse_list():
    list = [1,2,3,4,5]
    for i in range(len(list)//2):
        list[i], list[len(list)-i-1] = list[len(list)-i-1], list[i]
    print(list)

#Contar palabras en una lista y hacer un diccionario
def count_words():
    list = ['hola', 'mundo', 'hola', 'python']
    dict = {}
    for i in list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)

#Combinar dos listas DE DIFERENTE LONGITUD en una sola lista ordenando los elementos de menor a mayor
def combine_lists():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6, 7]
    combined_list = list1 + list2
    combined_list.sort()
    print(combined_list)

#mayor y menor de una tupla en una nueva tupla
def min_max_tuple():
    tuple = (1, 2, 3, 4, 5)
    min_value = min(tuple)
    max_value = max(tuple)
    new_tuple = (min_value, max_value)
    print(new_tuple)

#Desempaquetando tuplas
def desem_tuple():
    tuple = (1, 2, 3,4)
    a, b, c, d = tuple
    print(f"a: {a}, b: {b}, c: {c}, d: {d}")

reverse_list()
