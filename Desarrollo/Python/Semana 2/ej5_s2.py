saldo = 1000
estado = True
while estado:
    print("CAJERO AUTOMATICA\n1. Ver Saldo\n2. Depositar\n3. Retirar\n4. Salir")
    opcion = int(input("Ingresa una opcion:"))
    if opcion == 1:
        print(f"Tu saldo es: {saldo}")
    elif opcion == 2:
        print(f"Saldo actual: {saldo}")
        deposito = int(input(f"Cuanto dinero quieres depositar: "))
        saldo = saldo+deposito
        print(f"Saldo actual: {saldo}")
    elif opcion == 3:
        print(f"Saldo actual: {saldo}")
        retiro = int(input(f"Cuanto dinero quieres retirar: "))
        if retiro > saldo:
            print("Saldo insuficiente")
        else: 
            saldo = saldo - retiro
            print(f"Saldo actual: {saldo}")
    elif opcion == 4:
        print("Saliste, chao")
        estado = False
    else:
        print("OPCION INCORRECTA")