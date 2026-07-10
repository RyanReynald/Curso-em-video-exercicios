#Primeira e última ocorrência de uma string

frase = str(input("Digite um frase: ")).upper().strip()
print(f"A leta A aparece {frase.count("A")} Vezes na frase")
print(f"A primeira letra A foi encontrada na posição {frase.find("A")+1}")
print(f"A ultima letra A apareceu na posição {frase.rfind("A")+1}")
