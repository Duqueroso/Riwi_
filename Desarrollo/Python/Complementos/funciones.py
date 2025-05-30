def greeting(hello:str="Hello",name:str="")->str:
    name:str = input("Cual es tu nombre: ")
    greetingComplete:str = hello+" "+name
    return greetingComplete

def sum(num1:int=0,num2:int=0)->int:
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
    result = num1+num2
    return result

def circle_area(radio:float=0)->float:
    pi:float = 3.1416
    radio = float(input("Cual es el radio del circulo: "))
    area = pi*(radio**2)
    return area

def pair(value:bool=True)->bool:
    num = int(input("Ingresa un numero para saber si es par: "))
    if num%2!=0:
        value = False

    return value

def max(num1:float=0,num2:float=0,num3:float=0)->float:
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    num3 = float(input("Ingrese el tercer numero: "))

    if num1 > num2 and num1 > num3:
        result = num1
    elif num2 > num1 and num2 > num3:
        result = num2
    else:
        result = num3

    return result

def count_vowels(count:int=0)->str:
    word:str = input("Ingresa una palabra: ")
    i = 0
    while i < len(word):
        if word[i] in "aeiouAEIOU":
            count += 1
        i += 1

    print(f"La cantidad de vocales es: {count}")

def palindromo():
    word = input("Ingrese una palabra: ")
    word_invert = word[::-1]

    if word == word_invert:
        print("Si es un palindromo")
    else:
        print("No es palindromo")

def fibonnaci(num:int=0):
    num = int(input("Cuantos numeros de la serie de fibonnaci quieres: "))
    a, b = 0, 1
    for i in range(num):
        print(a)
        a, b = b, a + b
    return a

def 

fibonnaci()