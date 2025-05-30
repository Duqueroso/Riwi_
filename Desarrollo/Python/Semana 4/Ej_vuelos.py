#Sistema de reservas de vuelos
from random import randint
from random import choice

letras = ['AV','MD','RT','ZL','WQ']
asientos = ['A1','A2','A3','B1','B2','B3','C1','C2','C3','1C']
vuelos = {}
code:str = ''

def main():
    menu()

def menu():
    print('='*30)
    print('| SISTEMA DE RESERVAS DE VUELO')
    print('='*30)
    print('| OPCIONES DISPONIBLES')
    print('='*30)
    print('| 1. Reserva de asientos')
    print('| 2. Calcular porcentaje de ocupacion de vuelo')
    print('| 3. Generar reporte de vuelos ordenados por horario')
    print('| 4. Salir')
    option = input('Que opcion deseas realizar: ')
    match option:
        case '1':
            reserva()
        case '2':
            porcentaje()
        case '3':
            reporte()
        case '4':
            exit_()
        case _:
            print('Opcion incorrecta, intente nuevamente.')
            menu()
    
def vuelo():
    xx = choice(letras)
    number = randint(100,999)
    codeFly = (f'{xx}-{number}')
    return codeFly

def reserva():
    print('='*30)
    print('| RESERVAR VUELO')
    print('='*30)
    origen = input('Ingrese el origen del vuelo: ').upper()
    destino = input('Ingrese el destino del vuelo: ').upper()
    print(f'Asientos disponibles:\n{asientos}\n')
    validate = True
    while validate:
        asiento = input('Que asiendo deseas elegir: ').upper()
        for i in asientos:
            if i == asiento:
                print('Asiendo reservado con exito')
                asientos.remove(i)
                validate = False
                break
        else:
            print('Asiento no disponible.')
    print('='*30)
    print('Horario en que desea viajar (24HRS)')
    print('='*30)
    
    validate = True
    while validate:
        hora = int(input('HORA: '))
        if hora < 0 or hora > 23:
            print('Hora no valida, intente nuevamente')
        else:
            print('Hora asignada correctamente')
            validate = False

    validate = True
    while validate:
        minuto = int(input('MINUTO: '))
        if minuto < 0 or minuto > 59:
            print('minuto no valido, intente nuevamente')
        else:
            print('minuto asignado correctamente')
            validate = False
    
    horario = (f'{hora}:{minuto}')

    code = vuelo()   
    vueloDict = {
        f'{code}': {
            'origen': origen,
            'destino': destino,
            'asiento': asiento,
            'horario': horario
        },
    }

    vuelos.update(vueloDict)
    print('='*30)
    print(f'Vuelo reservado correctamente, detalles:\n{vueloDict}')
    

    validate = True
    while validate:
        option = input('\n| Quieres reservar otro asiento (S/N): ').upper()
        if option == 'S':
            reserva()
            break
        elif option == 'N':
            menu()
            break
        else:
            print('Opcion incorrecta, reintentelo')
        
def porcentaje():
    porcentaje = (len(vuelos)*100) / 10
    print(f'La ocupación del vuelo es: {porcentaje}%')
    validate:bool = True
    while validate:
        print("="*30)
        option:str = input("| Deseas salir del sistema: (S/N)").upper()
        if option == "S":
            print("| Saliendo del sistema...")
            exit_()
        elif option == "N":
            print("| Regresando al menú...")
            main()
        else:
            print("| Error, opción incorrecta")
    
def reporte():
    report = open('report.txt', 'w')
    report.writelines(vuelos)
    report.close()

    print('| RESERVAS\n')
    print(vuelos)
    validate:bool = True
    while validate:
        print("="*30)
        option:str = input("| Deseas salir del sistema: (S/N)").upper()
        if option == "S":
            print("| Saliendo del sistema...")
            exit_()
        elif option == "N":
            print("| Regresando al menú...")
            main()
        else:
            print("| Error, opción incorrecta")

def exit_():
    validate:bool = True
    while validate:
        print("="*30)
        option:str = input("| Deseas salir del sistema: (S/N)").upper()
        if option == "S":
            print("| Saliendo del sistema...")
            exit_()
        elif option == "N":
            print("| Regresando al menú...")
            main()
        else:
            print("| Error, opción incorrecta")

main()