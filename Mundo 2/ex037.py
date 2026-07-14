#Conversor de Bases Numéricas

n = int(input("Digite um número inteiro: "))

print("""Escolha uma das bases para conversão:
      [1] converte para BINÁRIO
      [2] converte para OCTAl
      [3] converte para HEXADECIMAL """)

opcao = int(input("Qual a sua opção: "))

if opcao == 1:
    print(f"{n} convertido pra BINÁRIO é igual a {bin(n)[2:]}")

elif opcao == 2:
    print(f"{n} convertido para OCTAL é igual a {oct(n)[2:]}")

elif opcao == 3:
    print(f"{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}")

else:
    print("opção inválida!")