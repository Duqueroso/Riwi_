n = int(input("Ingresa un numero: "))
f = 1

for i in range(1,n+1):
    f *= i

print(f)

f=1
nn=1
while nn <= n:
    f *= nn    
    nn += 1

print(f)