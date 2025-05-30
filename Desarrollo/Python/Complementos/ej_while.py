#Contar del 1 al 10
def uno():
    iniciador = 0
    while iniciador < 10:
        iniciador += 1
        print(iniciador)
    
#Contar del 10 al 1
def dos():
    iniciador = 11
    while iniciador > 1:
        iniciador -= 1
        print(iniciador)

#Suma los primeros 10 numeros
def tres():
    suma = 0
    iniciador = 0
    while iniciador < 11:
        suma += iniciador
        iniciador += 1
    print(suma)

#Solicitar numero positivo
def cuatro():
    numero = int(input("INGRESA UN NUMERO: "))
    opcion = True
    while opcion:
        if numero < 0:
            print("Ingresa un numero positivo")
            numero = int(input("INGRESA UN NUMERO: "))
        else:
            print("Ya ingresaste un positivo")
            opcion = False

#Menu interactivo
def cinco():
    opcion = True
    while opcion:
        print("\n1.Saludar\n2.Despedirse\n3.Salir\n")
        numero = int(input("Ingresa una opcion: "))
        if numero == 1:
            print("HOLA")
        elif numero == 2:
            print("CHAO")
        elif numero == 3:
            print("Saliste")
            opcion = False
        else:
            print("OPCION INVALIDA")

#Adivinar numero
def seis():
    numero = 5
    opcion = 0
    validador = True
    while validador:
        opcion = int(input("Ingresa un numero del 1 al 10: "))
        if opcion > 0 and opcion < 5:
            print("El numero es mayor")
        elif opcion > 5 and opcion < 10:
            print("El numero es menor")
        elif opcion == 5:
            print("Lo encontraste")
            validador = False
        else:
            print("Ingresa un numero valido")

#Contar vocales de una palabra
def siete():
    palabra = input("Ingresa una palabra: ")
    contador = 0
    i = 0
    while i < len(palabra):
        if palabra[i] in "aeiouAEIOU":
            contador += 1
        i += 1
    print("La cantidad de vocales es: ", contador)

#Validar contraseña
def ocho():
    contrasena = "python123"
    validador = True
    while validador:
        passw = input("Ingresa la contraseña: ")
        if passw == contrasena:
            print("Acceso concedido")
            validador = False
        else:
            print("Contraseña incorrecta, intenta nuevamente")

#Sumar hasta encontrar un cero
def nueve():
    suma = 0
    validador = True
    while validador:
        num = int(input("Ingrese un numero: "))
        if num != 0:
            suma += num
        else:
            print(f"La suma de los numeros es: {suma}")
            validador = False

#Numero entre 1 y 10
def diez():
    contador = 0
    validador = True
    while validador:
        num = int(input("Ingrese un numero entre 1 y 10: "))
        if num > 0 and num < 11:
            contador += 1
            print(f"El numero ingresado es: {num}")
            print(f"Numero de intentos: {contador}")
            validador = False
        else:
            contador += 1
            print("Intenta nuevamente")

