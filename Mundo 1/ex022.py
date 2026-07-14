# Analisador de textos

nome = str(input("Digite seu nome completo: ")).strip()

separa = nome.split()

print(f""" 
Anlisando seu nome...
Seu nome em maiúsculo é {nome.upper()}
Seu nome em minúsculo é {nome.lower()}
Seu nome tem ao todo {len(nome) - nome.count(" ")} letras
Seu nome tem ao todo {len(nome.replace(" ", ""))} Letras
Seu primeiro nome é {separa[0]} e ele {len(separa[0])} letras
""")
