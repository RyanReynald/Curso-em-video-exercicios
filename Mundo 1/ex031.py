#Custo de viagem

viagem = float(input("Qual a distância da viagem? "))
print(f"Você Está preste a começar uma viagem de {viagem}Km")

if viagem <= 200:
    viagem = viagem * 0.50
    print(f"E o preço da sua passagem será de R${viagem}")

else:
    viagem = viagem * 0.45
    print(f"E o preço da sua passagem será de R${viagem}")