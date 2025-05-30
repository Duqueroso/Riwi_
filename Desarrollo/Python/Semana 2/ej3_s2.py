a = "*"
asteriscos = int(input("De cuantos asteriscos es la torre: "))

for i in range(asteriscos):
    print(a)
    a = a+"*"

cantidad = 0
a = "*"
while cantidad != asteriscos:
    cantidad += 1
    print(a)
    a = a+"*"

