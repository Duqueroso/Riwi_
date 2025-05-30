a = "*"
asteriscos = int(input("De cuantos asteriscos es la torre: "))

for i in range(asteriscos,0,-1):
    print(a*i)


cantidad = 0
a = "*"
while asteriscos != cantidad:
    print(a*asteriscos)
    asteriscos -= 1