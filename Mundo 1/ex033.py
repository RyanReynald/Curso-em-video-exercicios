#Maior e menor valores

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))

lista = [n1, n2, n3]
lista.sort()

print(f"Maior número é {lista[2]} e o menor número é {lista[0]}")

#outra maneira de fazer:

menor = n1

if n2 < n1 and n2 < n3:
    menor = n2

if n3 < n1 and n3 < n2:
    menor = n3

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2

if n3 > n2 and n3 > n1:
    maior = n3

print(f"Maior número é {maior} e o menor número é {menor}")