#Gestión de calificaciones

#Variables globales
nota:int
cantidad:int
mayores:int
validar:int
notas = []

#Definimos funciones

def uno():
    #Solicitar al usuario que ingrese una nota y saber si aprueba o no
    nota = int(input("Ingrese una nota (0-100) para validar si aprobo o reprobo: "))
    if nota >= 0 and nota <= 100:
        if nota >= 60:
            print("-"*30)
            print("APROBASTE")
            print("-"*30)
        else:
            print("-"*30)
            print("REPROBASTE")
            print("-"*30)
    else:
        print("Ingresa una nota correcta")
    return

def dos():
    #Calcular promedio de notas ingresadas
    cantidad = int(input("Cuantas notas quieres ingresar: "))
    for i in range (cantidad):
        nota = int(input(f"Ingresa la {i+1} nota de 0-100: "))
        if nota >= 0 and nota <= 100:
            notas.append(nota)
        else:
            print("Ingresaste una nota erronea")

    promedio = sum(notas)/len(notas)
    print(f"El promedio de tus notas es: {promedio} ")
    if promedio >= 60:
        print("-"*30)
        print("APROBASTE")
        print("-"*30)
    else:
        print("-"*30)
        print("REPROBASTE")
        print("-"*30)

def tres():
    #Contar notas mayores
    mayores = 0
    validar = int(input("Ingresa el valor a comparar: "))
    if not notas:
        print("-"*30)
        print("No tiene notas ingresadas para comparar")
        print("-"*30)
    else:
        for i in range(len(notas)):
            if notas[i] > validar:
                mayores = mayores+1

        print("-"*30)
        print(f"Tienes {mayores} notas por encima de tu valor ingresado.")
        print("-"*30)

def menu():

    print("-"*30)
    print("GESTION DE CALIFICACIONES")
    print("-"*30)
    print("1. Determinar estado de aprobación")
    print("2. Agregar notas a la lista y calcular promedio de calificaciones")
    print("3. Saber cuantas notas son mayores que")
    print("-"*30)
    valor = int(input("| Que quieres realizar: "))
    print("-"*30)
    match valor:
        case 1:
            while True:
                uno()
                opcion = input("Quires hacer algo mas? (S/N)")
                opcionr = opcion.upper()
                if opcionr == "S":
                    menu()
                    break
                elif opcionr == "N":
                    print("-"*30)
                    print("Hasta luego")
                    print("-"*30)
                    break
                else:
                    print("OPCION INCORRECTA")
                    break
        case 2:
            while True:
                dos()
                opcion = input("Quires hacer algo mas? (S/N)")
                opcionr = opcion.upper()
                if opcionr == "S":
                    menu()
                    break
                elif opcionr == "N":
                    print("-"*30)
                    print("Hasta luego")
                    print("-"*30)
                    break
                else:
                    print("OPCION INCORRECTA")
                    break
        case 3:
            while True:
                tres()
                opcion = input("Quires hacer algo mas? (S/N)")
                opcionr = opcion.upper()
                if opcionr == "S":
                    menu()
                    break
                elif opcionr == "N":
                    print("-"*30)
                    print("Hasta luego")
                    print("-"*30)
                    break
                else:
                    print("OPCION INCORRECTA")
                    break
        case _:
            while True:
                print("Error, ingresa una opción correcta ºººº")
                opcion = input("Quires hacer algo mas? (S/N)")
                opcionr = opcion.upper()
                if opcionr == "S":
                    menu()
                    break
                elif opcionr == "N":
                    print("-"*30)
                    print("Hasta luego")
                    print("-"*30)
                    break
                else:
                    print("OPCION INCORRECTA")
                    break

#Mostramos menú

menu()