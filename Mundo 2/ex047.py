#Cotagem de pares

for n in range(1, 51):
    if n % 2 == 0:
        print(n, end=' ')
print("Acabou")

#Outro maneira de fazer

for n in range(2, 51, 2):
    print(n, end=" ")
print ("acabou")