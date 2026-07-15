#Alistamento militar

from datetime import date

atual = date.today().year

nasc = int(input("Em que ano você nasceu? "))

idade = atual - nasc

print(f"Quem nasceu em {nasc} tem {idade} anos em {atual}")

if idade < 18:
    print(f"ainda faltam {18 - idade} para o seu alistamento \n seu alistamento será em {atual + (18 - idade)}")

elif idade > 18:
    print(f"Você já deveria ter se alistado há {idade - 18} anos \n seu alistamento foi em {atual - (idade - 18)}")

else:
    print("Você tem que se alistar IMEDIATAMENTE!")