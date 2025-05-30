#Contar del 1 al 10

def uno():
    for i in range(1,11,1):
        print(i)


#Contar del 10 al 1
def dos():
    for i in range(10,0,-1):
        print(i)


#sumar los primeros 10 numeros
def tres():
    suma = 0
    for i in range(1,11,1):
        suma += i
    print(suma)

#Mostrar numeros pares del 1 al 20
def cuatro():
    for i in range(1,21,1):
        if i % 2 == 0:
            print(i)

#Mostrar multiplos de 3 entre 1 al 30
def cinco():
    for i in range(1,31,1):
        if i % 3 == 0:
            print(i)

#Contar letras a en una cadena
def seis():
    cadena = input("Ingrese una texto: ")
    contador = 0
    for i in cadena:
        if i == "a":
            contador += 1
    print(contador)

#Tabla de multiplicar de un numero
def siete():
    numero = int(input("Ingrese un numero: "))
    for i in range(1,11,1):
        print(f"{numero} x {i} = {numero*i}")

#Numeros positivos y negativos de una lista
def ocho():
    lista = [1, -2, 3, -4, 5, -6]
    positivos = []
    negativos = []
    for i in lista:
        if i > 0:
            positivos.append(i)
        else:
            negativos.append(i)
    print("Positivos: ", positivos)
    print("Negativos: ", negativos)

#Contar mayusculas y minusculas de una cadena
def nueve():
    cadena = input("Ingrese un texto: ")
    mayusculas = 0
    minusculas = 0
    for i in cadena:
        if i.isupper():
            mayusculas += 1
        elif i.islower():
            minusculas += 1
    print("Mayusculas: ", mayusculas)
    print("Minusculas: ", minusculas)

#simulacion de contraseña
def diez():
    contrasena = "python123"
    intentos = 3
    for i in range(intentos):
        ingreso = input("Ingrese la contraseña: ")
        if ingreso == contrasena:
            print("Acceso permitido")
            break
        else:
            print("Contraseña incorrecta")

