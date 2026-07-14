#036 - Aprovando Empréstimo

casa = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador R$"))
anos = int(input("Quantos anos de financiamento? "))

presta = casa / (anos * 12)
minimo = salario * 30 / 100

print(f"""Para pagar uma casa de R${casa:.2f} em {anos:2f}anos
      a prestação será de {presta:.2f}""")

if presta <= minimo:
    print("Empréstimo APROVADO!")
else:
    print("Emprestimo \033[31mNEGADO!\033[m")

