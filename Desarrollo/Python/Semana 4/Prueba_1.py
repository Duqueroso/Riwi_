#We declare the global variable
list_:list  = []

#We create a main function
def main():
    menu()

#Function to show the menu
def menu():
    print("="*30,"\n| Riwi-Shop")
    print("="*30,"\n| GESTIÓN DE INVENTARIO")
    print("="*30)
    print("| OPCIONES DISPONIBLES")
    print("="*30)
    print("| 1. Añadir un producto")
    print("| 2. Buscar producto")
    print("| 3. Actualizar precio")
    print("| 4. Eliminar producto")
    print("| 5. Calcular valor total de inventario")
    print("| 6. Mostrar inventario actual")
    print("| 7. Salir del sistema")
    print("="*30)
    option:str = input("| Que opción deseas realizar: ") #Data is requested from the user
    match option: #According to the option we enter the indicated function
        case "1":
            add()
        case "2":
            search()
        case "3":
            update()
        case "4":
            delete()
        case "5":
            total()
        case "6":
            show()
        case "7":
            exit_()
        case _:
            print("="*30)
            print("| Opcion Incorrecta, intentelo nuevamente")
            menu()

#Function to add product
def add():
    validate:bool = True
    while validate:
        print("="*30)
        print('| REGISTRAR PRODUCTO')
        print("="*30)
        name:str = input('| Ingrese el nombre del producto: ').upper() #Data is requested from the user
        if name == "": #validate the name is not empty, if it is empty ask again
            print("| Error, no puede estar vacio el nombre.")
        elif len(name) < 3: #validate the name is not less than 3 characters, if it is less than 3 ask again
            print('| Error, el nombre debe tener al menos 3 caracteres')
        elif len(name) > 20: #validate the name is not more than 20 characters, if it is more than 20 ask again
            print('| Error, el nombre no puede tener mas de 20 caracteres')
        else: #If the name is valid break the loop
            validate = False
    
    validate = True
    while validate:
        price:float = float(input('| Ingrese el precio del producto: ')) #Data is requested from the user
        if price == '': #validate the price is not empty, if it is empty ask again
            print('| Error, el precio no puede estar vacio')
        elif not price.__float__(): #validate the price is number, if it is not a number ask again
            print('| Error, el precio solo puede contener numeros')
        elif float(price) < 0: #validate the price is not negative, if it is negative ask again
            print('| Error, el precio no puede ser negativo')
        else: #If the price is valid break the loop
            validate = False

    validate = True
    while validate:
        quantity:int = int(input('| Ingrese la cantidad del producto: ')) #Data is requested from the user
        if quantity == '': #validate the quantity is not empty, if it is empty ask again
            print('| Error, la cantidad no puede estar vacia')
        elif not quantity.is_integer(): #validate the quantity is number, if it is not a number ask again
            print('| Error, la cantidad solo puede contener numeros')
        elif int(quantity) < 0: #validate the quantity is not negative, if it is negative ask again
            print('| Error, la cantidad no puede ser negativa')
        else: #If the quantity is valid break the loop
            validate = False 

    #We add the entries to a dictionary
    dict_:dict = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    #We add the dictionary to the list
    list_.append(dict_)
    print("="*30)
    print(f"| Producto agregado correctamente\n| Nombre: {name}\n| Precio: {price}\n| Cantidad: {quantity}")
    print("="*30)

    #validate option to enter another product
    validate:bool = True
    while validate:
        option:str = input("| Quieres agregar otro producto: (S/N)").upper()
        if option == "S":
            add()
        elif option == "N":
            exit_()
            break
        else:
            print("| Error, opción incorrecta")

#Function to search product
def search():
    validate = True
    while validate:
        print('='*30)
        print('| BUSCAR PRODUCTO')
        print('='*30)
        name = input('| Ingrese el nombre del producto a buscar: ').upper() #Data is requested from the user
        if name == '': #validate the name is not empty, if it is empty ask again
            print('| Error, el nombre no puede estar vacio')
        elif len(name) < 3: #validate the name is not less than 3 characters, if it is less than 3 ask again
            print('| Error, el nombre debe tener al menos 3 caracteres')
        elif len(name) > 20: #validate the name is not more than 20 characters, if it is more than 20 ask again
            print('| Error, el nombre no puede tener mas de 20 caracteres')
        else: #If the name is valid break the loop
            validate = False

    for i in list_: #search for the product in the list
        if i['name'] == name: 
            print('='*30)
            print(f"| Detalles del producto encontrado:\n| Nombre: {i['name']}\n| Precio: {i['price']}\n| Cantidad: {i['quantity']}")
            print('='*30)
            break
    else: #If the product is not found in the list
        print('| Producto no encontrado')

    #validate option to search for another product
    validate:bool = True
    while validate:
        option:str = input("| Quieres buscar otro producto: (S/N)").upper()
        if option == "S":
            search()
        elif option == "N":
            exit_()
            break
        else:
            print("| Error, opción incorrecta")

    exit_()

#Function to update product
def update():
    validate = True
    while validate:
        print('='*30)
        print('| ACTUALIZAR PRODUCTO ')
        print('='*30)
        name = input('| Ingrese el nombre del producto a actualizar: ').upper()
        if name == '': #validate the name is not empty, if it is empty ask again
            print('| Error, el nombre no puede estar vacio')
        elif len(name) < 3: #validate the name is not less than 3 characters, if it is less than 3 ask again
            print('| Error, el nombre debe tener al menos 3 caracteres')
        elif len(name) > 20: #validate the name is not more than 20 characters, if it is more than 20 ask again
            print('| Error, el nombre no puede tener mas de 20 caracteres')
        else: #If the name is valid break the loop
            validate = False

    for i in list_: #search for the product in the list
        if i['name'] == name:
            print('='*30)
            print(f"| Detalles actuales del producto:\n| Nombre: {i['name']}\n| Precio: {i['price']}\n| Cantidad: {i['quantity']}")
            print('='*30)
            validate = True
            while validate:
                i["price"] = float(input('| Ingrese el nuevo precio del producto: '))
                if i["price"] == '': #validate the price is not empty, if it is empty ask again
                    print('| Error, el precio no puede estar vacio')
                elif not i["price"].__float__(): #validate the price is number, if it is not a number ask again
                    print('| Error, el precio solo puede contener numeros')
                elif float(i["price"]) < 0: #validate the price is not negative, if it is negative ask again
                    print('| Error, el precio no puede ser negativo')
                else: #If the price is valid break the loop
                    validate = False
            validate = True
            while validate:
                i["quantity"] = int(input('| Ingrese la nueva cantidad del producto: '))
                if i["quantity"] == '': #validate the quantity is not empty, if it is empty ask again
                    print('| Error, la cantidad no puede estar vacio')
                elif not i["quantity"].is_integer(): #validate the quantity is number, if it is not a number ask again
                    print('| Error, la cantidad solo puede contener numeros')
                elif int(i["quantity"]) < 0: #validate the quantity is not negative, if it is negative ask again
                    print('Error la cantidad no puede ser negativa')
                else: #If the quantity is valid break the loop
                    validate = False
            print('='*30)
            print(f"| Detalles actualizados del producto:\n| Nombre: {i['name']}\n| Precio: {i['price']}\n| Cantidad: {i['quantity']}")
            print('='*30)

    #validate option to update another product     
    validate:bool = True
    while validate:
        option:str = input("| Quieres actualizar otro producto: (S/N)").upper()
        if option == "S":
            update()
        elif option == "N":
            exit_()
            break
        else:
            print("| Error, opción incorrecta")
    
    exit_()

#Function to delete product
def delete():
    validate = True
    while validate:
        print('='*30)
        print('| ELIMINAR PRODUCTO')
        print('='*30)
        name = input('| Ingrese el nombre del producto a eliminar: ').upper()
        if name == '': #validate the name is not empty, if it is empty ask again
            print('| Error, el nombre no puede estar vacio')
        elif len(name) < 3: #validate the name is not less than 3 characters, if it is less than 3 ask again
            print('| Error, el nombre debe tener al menos 3 caracteres')
        elif len(name) > 20: #validate the name is not more than 20 characters, if it is more than 20 ask again
            print('Error, el nombre no puede tener mas de 20 caracteres')
        else: #If the name is valid break the loop
            validate = False
            break
        

    for i in list_: #search for the product in the list
        if i['name'] == name:
            print('='*30)
            print(f"| PRODUCTO ENCONTRADO\n| Detalles:\n| Nombre:{i["name"]}\n| Precio: {i["price"]}\n| Cantidad: {i["quantity"]}")
            print('='*30)
            #We confirm product deletion
            validate:bool = True
            while validate:
                option = input("| Quieres eliminar el producto (S/N): ").upper()
                if option == "S":
                    list_.remove(i) #remove the product from the list
                    print(f"| Producto eliminado: {i['name']}")
                    validate = False
                elif option == "N":
                    exit_()
                else:
                    print("| Error, opción incorrecta")
            break
        
    else:
        print("| Producto no encontrado")

    #validate option to delete another product
    validate:bool = True
    while validate:
        print('='*30)
        option:str = input("| Quieres eliminar otro producto: (S/N)").upper()
        if option == "S":
            delete()
        elif option == "N":
            exit_()
            break
        else:
            print("| Error, opción incorrecta")

#Function to show total inventory
def total():
    total = 0
    for i in list_: #calculate the total value of the inventory
        total += i['price'] * i['quantity'] #multiply the price by the quantity of each product
    print('='*30)
    print(f'| El valor total del inventario es: {total:.2f}')
    exit_()

#Function to show inventory
def show():
    print("="*30)
    print("| INVENTARIO ")
    print("="*30)
    #we go through the list showing one by one of the products with their details
    for i in list_: 
        print(f"| Nombre: {i["name"]} / Precio: {i["price"]} / Cantidad: {i["quantity"]}")
    exit_()

#Function to ask if you want to exit the system
def exit_():
    validate:bool = True
    while validate:
        print("="*30)
        option:str = input("| Deseas salir del sistema: (S/N)").upper()
        if option == "S":
            print("| Saliendo del sistema...")
            exit()
        elif option == "N":
            print("| Regresando al menú...")
            main()
        else:
            print("| Error, opción incorrecta")

main()