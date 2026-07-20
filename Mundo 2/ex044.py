#Gerenciador de Pagamentos

print(f'{"Loja ReynaldTech":=^40}')

preco = float(input("Preço das compras: R$"))

desconto = 0

print("""FORMA DE PAGAMENTO
      [ 1 ] à vista dinheiro / cheque
      [ 2 ] à vista cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão""")

opcao = int(input("Qual é a opção? "))

if opcao == 1:
    desconto = preco - (preco * 10 / 100)
    print(f"Sua compra de R${preco} vai custar R${desconto:.2f} no final")

elif opcao == 2:
    desconto = preco - (preco * 5 / 100)
    print(f"Sua compra de R${preco} vai custar R${desconto:.2f} no final")

elif opcao == 3:
    parcela = preco / 2
    print(f"Sua compra de R${preco} vai custar R${desconto:.2f} no final")
    print(f"Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS")

elif opcao == 4:
    desconto = preco + (preco * 20 / 100)
    totalparcelas = int(input("Quantas parcelas? "))
    parcela = desconto / totalparcelas
    print(f"Sua compra de R${preco} vai custar R${desconto:.2f} no final")
    print(f"Sua compra será parcelada em {totalparcelas}x de R${parcela:.2f}")

else:
    print("Opção invalida")