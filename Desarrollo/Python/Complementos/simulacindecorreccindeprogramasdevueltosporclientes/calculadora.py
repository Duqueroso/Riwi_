def calculadora():
    print("Opciones de calculadora")
    print("1. suma")
    print("2. Resta")
    opcion = input("Elige una opcion (1/2): ")

    num1 = float(input("primer numero: "))
    num2 = float (input("Segundo numero: "))

    if opcion == "1":
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    elif opcion =="2":
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")

calculadora()