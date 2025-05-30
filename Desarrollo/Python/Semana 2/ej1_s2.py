numeros = []

for i in range(0, 50, 1):
    numeros.append(i)

print("PARES")
print("-"*20)
for i in numeros:
    if i%2==0:
        print(i)

i=0
print("IMPARES")
print("-"*20)
while i<50:
    if i%2!=0:
        print(i)
        i=i+1
    else:
        i=i+1

