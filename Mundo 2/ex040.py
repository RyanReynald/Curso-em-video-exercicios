#Aquele classico da media

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 +  nota2) / 2

print(f"Tirando {nota1} e {nota2}, a média do aluno é {media}")

if media >= 5 and media < 7:
    print(" aluno está de RECUPERAÇÃO ")

elif media >= 7:
    ("O aluno está APROVADO ")

else:
    print("Aluno está REPROVADO")