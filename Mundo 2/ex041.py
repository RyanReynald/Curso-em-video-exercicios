#CLassificando atletas

from datetime import date

nasc = int(input("Ano de nascimento: "))

atual = date.today().year

idade = atual - nasc

print(f"O atleta tem {idade} Anos.")

if idade <= 9:
    print("Classificação: MIRIM")

elif idade <=14:
    print(f"Classificação: INFANTIL")

elif idade <=19:
    print(f"Classificação: JUNIOR")

elif idade <=25:
    print(f"Classificação: SÊNIOR")

else:
    print("Classificação: MASTER")