#1. Pide al usuario su nombre y edad, y muestra un mensaje que diga: "Hola [nombre],tienes [edad] años."

def uno ():
    print("="*40)
    nombre = input("Ingresa tu nombre completo: ")
    edad = int(input("Ingresa tu edad: "))
    return(f"Hola {nombre}, tienes {edad} años.")

#2. Pide dos números enteros y muestra la suma de ambos.

def dos ():
    print("="*40)
    num1 = int(input("Ingresa el primer numero entero: "))
    num2 = int(input("Ingresa el segundo numero entero: "))
    resultado = num1 + num2
    return(f"El resultado de la suma de los dos numeros que ingresaste es {resultado}")

#3. Pide dos números decimales (float) y muestra su multiplicación.

def tres ():
    print("="*40)
    num1 = float(input("Ingresa el primer numero con decimales: "))
    num2 = float(input("Ingresa el segundo numero con decimales: "))
    resultado = num1 * num2
    return(f"El resultado de la multiplicación de los dos numeros que ingresaste es {resultado}")

#4. Pide un número entero y muestra el doble y el triple de ese número, separados por coma.

def cuatro ():
    print("="*40)
    num1 = int(input("Ingresa un numero entero: "))
    doble = num1 * 2
    triple = num1 * 3
    return(f"El doble del numero que ingresaste es: {doble} y el triple es: {triple}")

#5. Pide al usuario una palabra y un número entero. Muestra la palabra repetida ese número de veces.

def cinco ():
    print("="*40)
    palabra = input("Ingresa una palabra: ")
    cantidad = int(input("Ingresa un numero de veces que quieres mostrarla: "))

    for i in range(cantidad):
        print(palabra)
        i=+1

#6. Pide al usuario dos números y muestra el resultado de dividir el primero entre el segundo.

def seis ():
    print("="*40)
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
    resultado = num1 / num2

    return(f"La division es: {resultado}")

#7. Pide al usuario su nombre y muestra cuántas letras tiene su nombre.

def siete():
    print("="*40)
    nombre = len(input("Ingresa tu nombre: "))

    return(f"La cantidad de letras que tiene tu nombre es: {nombre}")

#8. Pide al usuario dos números y muestra la división entera (//) y el módulo (%) entre ellos.

def ocho():
    print("="*40)
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
    div = num1 // num2
    mod = num1 % num2
    return(f"La division entera de los dos numeros es: {div} y El modulo de los dos numeros es: {mod}")

#9. Pide al usuario dos números y muestra la suma, resta, multiplicación y división (separadas por coma).

def nueve():
    print("="*40)
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
    sum = num1 + num2
    res = num1 - num2
    multi = num1 * num2
    div = num1 / num2
    return(f"La suma de los dos numeros es: {sum}, la resta es: {res}, la multiplicacion es: {multi}, la division es: {div}")

#10. Pide un número entero y muestra el número elevado a la 2 (al cuadrado) y a la 3(al cubo), usando f-strings.

def diez():
    print("="*40)
    num1 = int(input("Ingresa un numero entero: "))
    cuadrado = num1**2
    cubo = num1**3

    return(f"El numero que ingresaste elevado al cuadrado da: {cuadrado} y elevado al cubo da: {cubo}")

#11. Pide al usuario un número decimal y muestra solo la parte entera de ese número.

def once():
    print("="*40)
    num1 = int(float(input("Ingresa un numero decimal: ")))

    return(f"La parte entera de tu decimal es: {num1}")

#12. Pide al usuario su edad y muestra un mensaje que diga si su edad es mayor que 18 (usar operadores de comparación, sin condicionales).

def doce():
    print("="*40)
    edad = int(input("Ingresa tu edad: "))
    mensaje = 'Eres mayor de edad' * (edad > 18) + 'Eres menor de edad' * (edad <= 18)
    return(mensaje)

#13. Pide al usuario dos números enteros y muestra si son iguales (usar operadores de comparación, sin condicionales).

def trece():
    print("="*40)
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
    mensaje = "Son iguales" * (num1 == num2) + "Son diferentes" * (num1 != num2)
   
    return(mensaje)

#14. Pide dos números y muestra si el primero es mayor que el segundo (usar operador de comparación).

def catorce():
    print("="*40)
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
    mensaje = "El numero 1 es menor que el 2" * (num1 < num2) + "El numero 1 es mayor que el 2" * (num1 > num2)
   
    return(mensaje)

#15. Pide dos números y muestra si el primero es menor o igual que el segundo (usar operador de comparación).

def quince():
    print("="*40)
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
    mensaje = "El numero 1 es menor o igual que el 2" * (num1 <= num2) + "El numero 1 es mayor que el 2" * (num1 > num2)
   
    return(mensaje)

#16. Pide al usuario dos números y muestra si ambos son mayores que 10 (usar operador lógico and).

def dieciseis():
    print("="*40)
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
    if num1 > 10 and num2 > 10:
        print("Ambos numeros son mayores que 10")
    else:
        print("Algun numero es menor que 10 o ambos son menores que 10")
   
    return

#17. Pide al usuario dos números y muestra si al menos uno es mayor que 10 (usar operador lógico or).

def diecisiete():
    print("="*40)
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
    if num1 > 10 or num2 > 10:
        print("Al menos uno de los numeros es mayor que 10")
    else:
        print("Ninguno es mayor que 10")
   
    return

#18. Pide al usuario dos números y muestra si el primero NO es igual al segundo (usar operador lógico not combinado con comparación).

def dieciocho():
    print("="*40)
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
    if not num1 == num2:
        print("No son iguales")
    else:
        print("Son iguales")
   
    return

#19. Pide al usuario tres números, calcula el promedio y muestra el resultado.

def diecinueve():
    print("="*40)
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
    num3 = int(input("Ingresa el tercer numero: "))
    promedio = print(f"El promedio de los tres numeros equivale a: {(num1 + num2 + num3) / 3}")

    return(promedio)

#20. Pide al usuario un número entero y muestra si el número es divisible entre 5 (usar operador de módulo % y comparación).

def veinte():
    print("="*40)
    num1 = int(input("Ingresa un numero: "))

    if num1 % 5 == 0:
        print(f"el numero {num1} es divisible por 5")
    else:
        print(f"El numero {num1} no es divisible por 5")


veinte()