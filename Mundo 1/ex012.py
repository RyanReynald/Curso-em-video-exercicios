valor = float(input("Qual o preço do produto? R$"))

desconto = valor - (valor * 5 / 100)

print(f"O produto que custava R${valor}, na promoção com desconto de 5% vai custar R${desconto:.2f}")