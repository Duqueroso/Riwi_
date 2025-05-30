#Calcular costo total de una compra

#Definimos las variables y solicitamos datos que necesitamos
print("="*40)
print()
subtotal = 0
total = 0

nom_producto = input("Ingresa el nombre del producto que vas a comprar: ")



#Comprobamos que sea numero positivo "Aplicando una forma de Do-While"
while True:
    print("="*40)
    try:
        precio_unidad = float(input("Ingresa el precio unitario: "))
        if precio_unidad > 0: 
            break
        print("El precio no puede ser negativo, valida nuevamente.")
    except ValueError:    
        print("Error, solo numeros.")
        
#Comprobamos que sea numero positivo "Aplicando un While"
print("="*40)
cantidad_productos = int(input("Ingresa la cantidad que deseas llevar: "))
while cantidad_productos < 0:
    print("La cantidad de productos no puede ser negativo, valida nuevamente.")
    cantidad_productos = int(input("Ingresa la cantidad que deseas llevar: "))

#Validamos descuentos
print("="*40)
descuento = int(input("Ingresa el descuento del producto: "))
while descuento < 0 or descuento > 100:
    print("="*40)
    print("El descuento no se puede aplicar porque no esta dentro del rango")
    print("="*40)
    descuento = int(input("Ingresa el descuento del producto: "))

#Operamos
subtotal = int(precio_unidad * cantidad_productos)
descuento_aplicado = subtotal * (descuento/100)
total = int(subtotal - descuento_aplicado)

#Mostramos información de compra
print("="*40)
print("||       INFORMACION DE LA COMPRA        ||")
print("="*40)
print(f"||      {nom_producto}  X {cantidad_productos} unidades     ||")
print(f"||      Subtotal = {subtotal}        ||")
print(f"||      Total = {total}      ||")
print("="*40)