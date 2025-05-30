#Import
from datetime import date

#Variables Globales
title_books = []
authors = []
genres =[]
years = []
quantity_books = []
price = []

def main():
    menu()

#Una funcion que muestra el menú
def menu():
    print("="*30)
    print("GESTION DE LIBROS")
    print("="*30)
    print("OPCIONES DISPONIBLES")
    print("="*30)
    print("1. Registrar nuevos libros")
    print("2. Buscar libros")
    print("3. Actualizar información")
    print("4. Eliminar libros obsoletos")
    print("5. Generar reportes")
    print("6. Salir")
    print("="*30)
    opcion = int(input("QUE DESEAS REALIZAR: "))
    match opcion:
        case 1:
            add()
        case 2:
            search()
        case 3:
            update()
        case 4:
            delete()
        case 5:
            report()
        case 6:
            exit_()
        case _:
            print("OPCION NO VALIDA")
            menu()
    
def add():
    print("="*30)
    print("REGISTRAR LIBRO")
    print("="*30)
    validate = True
    while validate:
        title = input("Ingrese el titulo del libro: ")
        if title == '':
            print("El titulo no puede estar vacio")
        else:
            title_books.append(title)
            validate = False

    validate = True
    while validate:
        author = input("ingresa el autor del libro: ")
        if author == "":
            print("El autor no puede estar vacio.")
        else:
            authors.append(author)
            validate = False

    validate = True
    while validate:
        genre = input("ingresa el genero del libro: ")
        if genre == "":
            print("El genero no debe de estar vacio")
        else:
            genres.append(genre)
            validate = False
    
    validate = True
    while validate:
        year = int(input("Ingresa el año de publicación: "))
        today = date.today()
        year_now = int(format(today.year))
        if year < 1500 or year > year_now:
            print("Ingresa un año correcto despues de 1500 hasta el año actual")
        elif not year.is_integer():
            print("Ingresa solo numeros para el año")
        else:
            years.append(year)
            validate = False

    validate = True
    while validate:
        quantity = int(input("Ingrese la cantidad de libros: "))
        if quantity < 0:
            print("Ingrese una cantidad positiva de libros")
        elif not quantity.is_integer():
            print("Ingrese solo numeros para la cantidad.")
        else:
            quantity_books.append(quantity)
            validate = False

    validate = True
    while validate:
        price_reposition = float(input("Cual seria el costo de reposicion por libro: "))
        if price_reposition < 0:
            print("Ingrese solo numeros positivos")
        elif not price_reposition.is_integer():
            print("El precio debe ser superior a 0")
        else:
            price.append(price_reposition)
            validate = False
    
    print("="*30)
    opcion = input("Quieres ingresar otro libro (S/N): ")
    opcionf = opcion.upper()
    if opcionf == "S":
        add()
    elif opcionf == "N":
        salida = input("Quieres salir del sistema (S/N): ")
        salidaf = salida.upper()
        if salidaf == "S":
            print("Saliste del sistema, chao...\n")
        elif salidaf == "N":
            menu()
        else:
            print("OPCION INVALIDA")
    else:
        print("OPCION INVALIDA")

def search():
    print("="*30)
    print("BUSCAR LIBRO")
    print("="*30)
    validate = True
    while validate:
        search = input("Ingrese el nombre del libro que desea buscar: ")
        for i in title_books:
            if search == title_books[i]:
                print(f"El libro {title_books[i]} ha sido encontrado\nSus detalles son\nTitulo: {title_books[i]}\nAutor: {authors[i]}\nGenero: {genres[i]}\nAño de publicación: {years[i]}")
                validate = False
                break
            else:
                print("Libro no encontrado")
                option = input("Quieres hacer otra busquedad (S/N): ")
                optionF = option.lower()
                if optionF == 's':
                    search()
                elif optionF == 'n':
                    exit_()
                else: 
                    print("Opcion Incorrecta")

def update():
    pass

def delete():
    pass

def report():
    pass

def exit_():
    validate = True
    while validate:
        option = input('Quieres salir del programa (S/N): ').lower
        if option == 's':
            print('Saliendo del programa...')
            validate = False
            break
        elif option == 'n':
            print('Regresando al menu')
            menu()
        else:
            print('Opcion Incorrecta')
    pass
                       


menu()
