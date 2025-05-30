#Definir e inicializar variables
nota1 = float(input("Ingrese la primer nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercer nota: "))

#Operación
notaf:float = (nota1+nota2+nota3)/3.0

#Logica y salida
if notaf >= 7:
    print("Promocionado")
elif notaf >= 4:
    print ("Regular")
elif notaf <= 4:
    print("Reprobado")

