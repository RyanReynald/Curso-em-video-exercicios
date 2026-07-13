#Analisando Triângulo v1.0

print("=" * 20)
print("Analisando triângulos")
print("=" * 20)

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("os segmentos a cima podem forma um triângulo!")

else:
    print("Os segmentos a cima não podem forma um triângulo")