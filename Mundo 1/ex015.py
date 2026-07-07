dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos km rodados? "))

aluguel = (60 * dias) + (0.15 * km)

print(f"O total a pagar é de R${aluguel:.2f}")