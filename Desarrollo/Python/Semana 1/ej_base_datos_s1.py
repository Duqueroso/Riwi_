url = "www.riwi.com/BD/=3080/Prueba1/NombreDeUsuario=Brayan&Contraseña=Ingreso20*"
puerto = "3080"
nom_base = "Prueba1"
User_Name = "Brayan"
Password = "Ingreso20*"
server = "www.riwi.com/BD"

#Solicitamos informarción

server2 = input("Ingrese el servidor donde quieres acceder: ")
puerto2 = input("Ingresa el puerto de acceso: ")
nom_base2 = input("Ingresa el nombre de la base de datos: ")
User_Name2 = input("Ingresa tu nombre de usuario: ")
Password2 = input("Ingresa tu contraseña: ")

url2 = (f"{server2}/={puerto2}/{nom_base2}/NombreDeUsuario={User_Name2}&Contraseña={Password2}")

if url == url2:
    print("Acceso concedido, bienvenido")
else:
    print("Tus credenciales no coinciden")
