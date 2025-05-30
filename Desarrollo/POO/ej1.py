class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando")


nombre = input("Cual es tu nombre: ")
edad = int(input("Cual es tu edad: "))
grado = input("Cual es tu grado: ")

estudiante1 = Estudiante(nombre,edad,grado)

print(f"El estudiante {estudiante1.nombre}, tiene {estudiante1.edad} años y esta en el grado {estudiante1.grado}")

while True:
    estudiar = input("Que quieres hacer: ")
    if estudiar.lower() == "estudiar":
        estudiante1.estudiar()
    